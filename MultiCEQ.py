import SingleCEQ as CEQ
import os

try:
    os.makedirs("Results/")
except FileExistsError:
    # directory already exists
    pass

filepath = 'urls.txt'
with open(filepath) as fp:
    each_url = fp.readline().rstrip('\n')
    CEQ.SingleCEQ(each_url)
    while each_url:
        each_url = fp.readline().rstrip('\n')
        if(each_url==''):
            break
        CEQ.SingleCEQ(each_url)