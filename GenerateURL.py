Course1 = ["FTN01"]
termin = "VT"
start_year = 17
end_year = 10
LP = "LP1"

"http://www.ceq.lth.se/rapporter/2010_HT/LP1/FRTN10_2010_HT_LP1_slutrapport_en.html"
i=0
url = []

for year in range(end_year,start_year):
    url.append("http://www.ceq.lth.se/rapporter/20"+str(year)+"_"+termin+"/"+Course_code+"_20"+str(year)+"_"+termin+"_"+LP+"_slutrapport_en.html")
    i+=1

with open('generated_urls.txt', 'w') as f:
    for item in url:
        f.write("%s\n" % item)

print(url)