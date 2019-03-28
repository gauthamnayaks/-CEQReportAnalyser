Courses = []
#Enter courses of the form Course_code, termin, start_year, end_year, LP, Student_group
Courses.append(["MMTA02", "HT", "17", "09", "LP2", "all"])

Courses.append(["MMTA05", "HT", "17", "09", "LP1", "all"])

Courses.append(["MMTF01", "HT", "17", "09", "LP2", "all"])

Courses.append(["MMTF05", "VT", "18", "11", "LP2", "all"])

Courses.append(["MMTF10", "VT", "18", "18", "LP2", "all"])

Courses.append(["MMTF15", "VT", "18", "14", "LP2", "all"])
Courses.append(["MMTF15", "HT", "17", "16", "LP2", "all"])
Courses.append(["MMTF15", "HT", "14", "13", "LP2", "all"])

Courses.append(["MMTF20", "VT", "18", "18", "LP2", "all"])

Courses.append(["MMTF25", "VT", "18", "18", "LP2", "all"])

Courses.append(["MMTN05", "VT", "18", "13", "LP2", "all"])

Courses.append(["MMTN10", "HT", "17", "16", "LP2", "all"])

Courses.append(["MMTN15", "VT", "18", "17", "LP2", "all"])
Courses.append(["MMTN15", "HT", "17", "16", "LP2", "all"])
Courses.append(["MMTN15", "HT", "17", "16", "LP1", "all"])

Courses.append(["MMTN20", "HT", "17", "17", "LP1", "all"])

Courses.append(["MMTN25", "HT", "17", "17", "LP1", "all"])

Courses.append(["MMTN30", "VT", "18", "18", "LP1", "all"])

Courses.append(["MMTN35", "HT", "17", "17", "LP1", "all"])

i=0
url = [] # Store the urls

for course in Courses:
    Course_code = course[0]
    termin = course[1]
    start_year = course[2]
    end_year = course[3]
    LP = course[4]
    program = course[5]

    #for year in range(int(end_year),int(start_year)):
    year = int(start_year)
    while(True):
        if(program=="all"):
            url.append("http://www.ceq.lth.se/rapporter/20"+str("{0:0=2d}".format(year))+"_"+termin+"/"+LP+"/"+Course_code+"_20"+str("{0:0=2d}".format(year))+"_"+termin+"_"+LP+"_slutrapport_en.html")
        else:
            url.append("http://www.ceq.lth.se/rapporter/20"+str("{0:0=2d}".format(year))+"_"+termin+"/"+LP+"/"+Course_code+"_20"+str("{0:0=2d}".format(year))+"_"+termin+"_"+LP+"_"+program+"_slutrapport_en.html")
        year=year-1
        if(year<=int(end_year)):
            break


with open('mec_urls.txt', 'w') as f:
    for item in url:
        f.write("%s\n" % item)
