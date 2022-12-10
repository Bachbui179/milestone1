# this function use the best fit algorithm to arrange all the parcel to bins
import json
from arrange_parcel import sortParcel
from best_fit_algorithm import bestFit

f = open('data.json')
data = json.load(f)
parcelList = sortParcel(data)
maxSize = 10

parcelSizeData = []

for items in parcelList:
    listSize = []
    for i in items:
        s = i['size']
        listSize.append(s)
    parcelSizeData.append(listSize)

parcelBin = []

for weight in parcelSizeData:
	n = len(weight)
	index = parcelSizeData.index(weight)
	#arrange items using best fit algorithm
	storeItems = [[] for i in range(n)]

	res = 0

	bin_rem = [0]*n

	for i in range(n):
		j = 0
		min = maxSize + 1
		bi = 0
		for j in range(res):
			if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):				
				bi = j
				min = bin_rem[j] - weight[i]
				storeItems[j].append(parcelList[index][i])
			else:
				continue
		if (min == maxSize + 1):
			bin_rem[res] = maxSize - weight[i]
			storeItems[res].append(parcelList[index][i])
			# storeItems[res].append(parcelList[1][1])
			res += 1
		else: 
			bin_rem[bi] -= weight[i]

	while True:
		if storeItems[len(storeItems)-1] == []:
			storeItems.pop(len(storeItems)-1)
		else: 
			break
	
	parcelBin.append(storeItems)
# print(parcelSizeData)
print(parcelBin)
# print(parcelList)