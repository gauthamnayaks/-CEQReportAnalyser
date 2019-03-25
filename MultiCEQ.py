import SingleCEQ as CEQ
import os

try:
    os.makedirs("Results/Regler")
except FileExistsError:
    # directory already exists
    pass

filepath = 'URLs/Regler.txt'
with open(filepath) as fp:
    each_url = fp.readline().rstrip('\n')
    CEQ.SingleCEQ(each_url)
    while each_url:
        each_url = fp.readline().rstrip('\n')
        if(each_url==''):
            continue
        CEQ.SingleCEQ(each_url)