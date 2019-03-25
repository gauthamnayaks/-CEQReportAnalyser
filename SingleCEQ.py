
import requests #To read URLS
import csv # To write CSVs
import lxml.html as lh
#import pandas as pd

def SingleCEQ(url):
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
    #Course info starts from 2. Used to make a dictionary
    for i in range(1,23,2):
        #print(i,"= ",all_Course_info[i].text_content())
        Course_info.append([all_Course_info[i].text_content().replace(u'\xa0', u' '), all_Course_info[i+1].text_content().replace(u'\xa0', u' ').split('\n', 1)[0]])
        i+=2

    #print("Course info = ", Course_info)

    Course_time = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(25,35,2):
        #print(i,"= ",all_Course_info[i].text_content())
        Course_time.append([all_Course_info[i].text_content(), all_Course_info[i+1].text_content()])
        i+=2

    #print("Course time = ", Course_time)

    Attendance = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(36,47,3):
        #print(i,"= ",all_Course_info[i].text_content())
        Attendance.append([all_Course_info[i].text_content(), all_Course_info[i+1].text_content(), all_Course_info[i+2].text_content()])
        i+=2

    #print("Attendance =", Attendance)

    Feedback = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(48,71,3):
        #print(i,"= ",all_Course_info[i].text_content())
        if(i==63): # Skip an empty line
            continue
        Feedback.append([all_Course_info[i].text_content(), all_Course_info[i+1].text_content(), all_Course_info[i+2].text_content()])
        i+=2

    #print("Feedback =", Feedback)

    Happiness = []
    #Course info starts from 2. Used to make a dictionary
    for i in range(79,90,3):
        #print(i,"= ",all_Course_info[i].text_content())
        Happiness.append([all_Course_info[i].text_content(), all_Course_info[i+1].text_content(), all_Course_info[i+2].text_content()])
        i+=2

    #print("Happiness =", Happiness)

    Happiness_dist = []
    #Course info starts from 2. Used to make a dictionary
    Happiness_dist.append([all_Course_info[92].text_content(), all_Course_info[93].text_content()])
    Happiness_dist.append([all_Course_info[94].text_content(), all_Course_info[95].text_content()])
    Happiness_dist.append([all_Course_info[97].text_content(), all_Course_info[98].text_content()])
    Happiness_dist.append([all_Course_info[100].text_content(), all_Course_info[101].text_content()])

    #print("Happiness_dist =", Happiness_dist)

    #Relevence = []
    #Course info starts from 2. Used to make a dictionary
    #Relevence.append([all_Course_info[106].text_content(), all_Course_info[107].text_content()])
    #Relevence.append([all_Course_info[108].text_content(), all_Course_info[109].text_content()])

    #print("Relevence =", Relevence)
    filename =("Results/Regler/"+Course_info[1][1]+"_"+Course_info[3][1]+"_"+Course_info[4][1]+"_"+Course_info[5][1]+".csv")

    with open(filename, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(Course_info)
        writer.writerows(Course_time)
        writer.writerows(Attendance)
        writer.writerows(Feedback)
        writer.writerows(Happiness)
        writer.writerows(Happiness_dist)
        #writer.writerows(Relevence)

    csvFile.close()
