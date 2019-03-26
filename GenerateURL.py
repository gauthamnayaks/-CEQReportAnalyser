Courses = []
#Enter courses of the form Course_code, termin, start_year, end_year, LP, Student_group
Courses.append(["FRT010", "VT", "17", "10", "LP1", "F"]) #AK Courses
Courses.append(["FRT010", "VT", "17", "10", "LP1", "I"])  #AK Courses
Courses.append(["FRT010", "VT", "17", "10", "LP1", "PI"]) #AK Courses
Courses.append(["FRT010", "HT", "17", "10", "LP2", "C"]) #AK Courses
Courses.append(["FRT010", "HT", "17", "10", "LP2", "M"]) #AK Courses
Courses.append(["FRT010", "HT", "17", "10", "LP2", "MD"]) #AK Courses
Courses.append(["FRT010", "HT", "17", "10", "LP2", "N"]) #AK Courses

Courses.append(["FRTF05", "VT", "18", "18", "LP1", "F"]) #AK Courses
Courses.append(["FRTF05", "VT", "18", "18", "LP1", "I"])  #AK Courses
Courses.append(["FRTF05", "VT", "18", "18", "LP1", "PI"]) #AK Courses
Courses.append(["FRTF05", "HT", "17", "17", "LP2", "C"]) #AK Courses
Courses.append(["FRTF05", "HT", "17", "17", "LP2", "M"]) #AK Courses
Courses.append(["FRTF05", "HT", "17", "17", "LP2", "MD"]) #AK Courses
Courses.append(["FRTF05", "HT", "17", "17", "LP2", "N"]) #AK Courses

Courses.append(["FRT041", "HT", "16", "14", "LP2", "all"])
Courses.append(["FRT041", "VT", "14", "10", "LP2", "all"])

Courses.append(["FRT090", "HT", "16", "14", "LP2", "all"])
Courses.append(["FRT090", "VT", "14", "10", "LP2", "all"])

Courses.append(["FRT095", "VT", "17", "15", "LP1", "all"])
Courses.append(["FRT095", "VT", "14", "09", "LP2", "all"])

Courses.append(["FRT100", "VT", "13", "12", "LP2", "all"])

Courses.append(["FRT110", "VT", "17", "09", "LP2", "all"])

Courses.append(["FRT130", "VT", "17", "10", "LP1", "all"])

Courses.append(["FRT602", "VT", "17", "10", "LP2", "all"])

Courses.append(["FRTF01", "HT", "17", "13", "LP2", "all"])

Courses.append(["FRTN01", "VT", "18", "15", "LP2", "all"])
Courses.append(["FRTN01", "HT", "14", "09", "LP2", "all"])

Courses.append(["FRTN05", "HT", "17", "14", "LP2", "all"])
Courses.append(["FRTN05", "VT", "14", "11", "LP1", "all"])

Courses.append(["FRTN10", "HT", "17", "10", "LP1", "all"])

Courses.append(["FRTN15", "HT", "18", "09", "LP2", "all"])

Courses.append(["FRTN20", "VT", "16", "10", "LP2", "all"])

Courses.append(["FRTN25", "VT", "18", "13", "LP2", "all"])

Courses.append(["FRTN30", "VT", "18", "15", "LP2", "all"])

Courses.append(["FRTN35", "HT", "17", "17", "LP2", "all"])

Courses.append(["FRTN40", "HT", "17", "17", "LP2", "all"])

Courses.append(["FRTN45", "VT", "18", "18", "LP1", "all"])

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


with open('generated_urls.txt', 'w') as f:
    for item in url:
        f.write("%s\n" % item)