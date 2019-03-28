import os
import requests #To read URLS
import csv # To write CSVs
import lxml.html as lh


def SingleCEQ(url, result_folder):
    #Create a handle, page, to handle the contents of the website
    print("url =", url)
    page = requests.get(url)
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')

    #Create empty list
    col=[]
    i=0

    #print(tr_elements[0].text_content())
    all_Course_info = tr_elements[0].xpath('//td')

    for t in all_Course_info:
        i+=1
        name=t.text_content()
        #print(i,name)
        col.append((name,[]))

    ### Final vairables to store all the information
    Course_info = []
    info_column = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(1,23,2):
        #print(i,"= ",all_Course_info[i].text_content())
        Course_info.append([all_Course_info[i+1].text_content().replace(u'\xa0', u'').split('\n', 1)[0]])
        info_column.append([all_Course_info[i].text_content().replace(u'\xa0', u'')])
        i+=2

    Course_time = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(25,35,2):
        try: # Exit if not enough students exist
            Course_info.append(str([all_Course_info[i+1].text_content().strip()]))
            info_column.append([all_Course_info[i].text_content()])
        except IndexError:
            filename =("Results/Regler/Incomplete/"+Course_info[1][0]+"_"+Course_info[2][0]+"_"+Course_info[3][0]+"_"+Course_info[4][0]+".csv")
            with open(filename, 'w') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(Course_info)
                #writer.writerows(Relevence)
            csvFile.close()
            return
        i+=2

    #print("Course time = ", Course_time)

    Attendance = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(36,47,3):
        #print(i,"= ",all_Course_info[i].text_content())
        try:
            appended = all_Course_info[i+1].text_content()+"/" +all_Course_info[i+2].text_content()
            Course_info.append([appended])
            info_column.append([all_Course_info[i].text_content()])
        except IndexError:
            filename =("Results/Regler/Incomplete/"+Course_info[1][1]+"_"+Course_info[3][1]+"_"+Course_info[4][1]+"_"+Course_info[5][1]+".csv")

            with open(filename, 'w') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(Course_info)
                writer.writerows(Course_time)
                #writer.writerows(Relevence)
            csvFile.close()
            return
        i+=2

    #print("Attendance =", Attendance)

    Feedback = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(48,71,3):
        #print(i,"= ",all_Course_info[i].text_content())
        appended =  all_Course_info[i+1].text_content()+"/"+ all_Course_info[i+2].text_content()
        if(i==63): # Skip an empty line
            continue
        Course_info.append([appended])
        info_column.append([all_Course_info[i].text_content()])
        i+=2

    #print("Feedback =", Feedback)

    Happiness = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(79,90,3):
        appended = all_Course_info[i+1].text_content()+ "/" + all_Course_info[i+2].text_content()
        #print(i,"= ",all_Course_info[i].text_content())
        Course_info.append([appended])
        info_column.append([all_Course_info[i].text_content()])
        i+=2

    #print("Happiness =", Happiness)

    #Happiness_dist = []
    #Course info starts from 2. Used to make a dictionary
    #Course_info.append([all_Course_info[93].text_content()])
    #info_column.append([all_Course_info[92].text_content()])
    #Course_info.append([all_Course_info[95].text_content()])
    #info_column.append([all_Course_info[94].text_content()])
    #Course_info.append([all_Course_info[98].text_content()])
    #info_column.append([all_Course_info[97].text_content()])
    #Course_info.append([all_Course_info[101].text_content()])
    #info_column.append([all_Course_info[100].text_content()])

    #print("Happiness_dist =", Happiness_dist)

    #Relevence = []
    #Course info starts from 2. Used to make a dictionary
    #Relevence.append([all_Course_info[106].text_content(), all_Course_info[107].text_content()])
    #Relevence.append([all_Course_info[108].text_content(), all_Course_info[109].text_content()])

    #print("Relevence =", Relevence)
    #filename =(result_folder+Course_info[1][1]+"_"+Course_info[3][1]+"_"+Course_info[4][1]+"_"+Course_info[5][1]+".csv")
    filename =(result_folder+Course_info[1][0]+".csv")

    exists = os.path.isfile(filename)
    if exists:
        pass
    else: #If file doesnt exist fill it with the first coulumn with information
        with open(filename, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(info_column)
    # Keep presets

    f = open(filename)
    data = [item for item in csv.reader(f)]
    f.close()

    new_data = []

    for i, item in enumerate(data):
        try:
            item.append(Course_info[i])
        except IndexError:
            item.append("placeholder")
        new_data.append(item)

    f = open(filename, 'w')
    csv.writer(f).writerows(new_data)
    f.close()
