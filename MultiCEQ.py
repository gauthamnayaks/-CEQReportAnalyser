import SingleCEQ as CEQ
import os

try:
    os.makedirs("Results/Regler/Incomplete")
except FileExistsError:
    # directory already exists
    pass

try:
    os.makedirs("Results/BME/Incomplete")
except FileExistsError:
    # directory already exists
    pass

try:
    os.makedirs("Results/Mec/Incomplete")
except FileExistsError:
    # directory already exists
    pass

regler = 'bme_urls.txt'
with open(regler) as fp:
    each_url = fp.readline().rstrip('\n')
    CEQ.SingleCEQ(each_url, "Results/Regler/")
    while each_url:
        each_url = fp.readline().rstrip('\n')
        if(each_url==''):
            continue
        CEQ.SingleCEQ(each_url, "Results/Regler/")

bme = 'bme_urls.txt'
with open(bme) as fp:
    each_url = fp.readline().rstrip('\n')
    CEQ.SingleCEQ(each_url, "Results/BME/")
    while each_url:
        each_url = fp.readline().rstrip('\n')
        if(each_url==''):
            continue
        CEQ.SingleCEQ(each_url, "Results/BME/")
