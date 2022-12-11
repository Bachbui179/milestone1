# this function use stack algorithm to load and unload parcels to a 1 door truck
import json
from bin_packing import parcelBinList

f = open('data.json')
data = json.load(f)

parcels = parcelBinList(data)
truckBins = []


def load_truck(bins, truck):
    bins.reverse()
    if len(truck) == 0:
        for i in range(len(bins)):
            print("Load bin : {}".format(bins[i]))
            truck.append(bins[i])
    else:
        unload_truck(bins, truck)

    return truck


def unload_truck(bins, truck):

    if len(truck) != 0:
        truck.reverse()
        for i in range(len(truck), 0):
            print("Unload bin : {}".format(bins[i]))
            # truck.pop(0)
    else:
        load_truck(bins, truck)

        return truck

print(parcels)
