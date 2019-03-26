Courses = []
#Enter courses of the form Course_code, termin, start_year, end_year, LP, Student_group

Courses.append(["BLT015", "VT", "17", "10", "LP1", "all"])

Courses.append(["BMEF01", "VT", "18", "16", "LP2", "all"])

Courses.append(["BMEF05", "VT", "18", "18", "LP2", "all"])

Courses.append(["BMEF10", "HT", "18", "18", "LP1", "all"])

Courses.append(["BMEF15", "HT", "18", "18", "LP1", "all"])

Courses.append(["BMEN01", "VT", "18", "15", "LP2", "all"])

Courses.append(["BMEN05", "HT", "17", "15", "LP1", "all"])

Courses.append(["BMEN10", "HT", "17", "15", "LP2", "all"])

Courses.append(["EDA011", "VT", "17", "09", "LP2", "all"])

Courses.append(["EDA016", "HT", "15", "09", "LP2", "all"])

Courses.append(["EDA017", "VT", "17", "10", "LP1", "all"])

Courses.append(["EDA031", "VT", "17", "10", "LP2", "all"])


i=0
url = [] # Store the urls

for course in Courses:
    Course_code = course[0]
    termin = course[1]
    start_year = course[2]
    end_year = course[3]
    LP = course[4]
    program = course[5]

    for year in range(int(end_year),int(start_year)):
        if(program=="all"):
            url.append("http://www.ceq.lth.se/rapporter/20"+str("{0:0=2d}".format(year))+"_"+termin+"/"+LP+"/"+Course_code+"_20"+str("{0:0=2d}".format(year))+"_"+termin+"_"+LP+"_slutrapport_en.html")
        else:
            url.append("http://www.ceq.lth.se/rapporter/20"+str("{0:0=2d}".format(year))+"_"+termin+"/"+LP+"/"+Course_code+"_20"+str("{0:0=2d}".format(year))+"_"+termin+"_"+LP+"_"+program+"_slutrapport_en.html")
        i+=1

with open('bme_urls.txt', 'w') as f:
    for item in url:
        f.write("%s\n" % item)
