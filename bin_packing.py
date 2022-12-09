# this function use the best fit algorithm to arrange all the parcel to bins
import json
from arrange_parcel import sortParcel
from best_fit_algorithm import bestFit

f = open('data.json')
data = json.load(f)
parcelList = sortParcel(data)
binMaxSize = 10

parcelSizeData = []

for items in parcelList:
    for i in items:
        s = i['size']
        print(s, end =' ')

print(parcelList)