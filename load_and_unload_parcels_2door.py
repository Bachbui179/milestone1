# this function use queue algorithm to load and unload parcels to a 2 door truck
import json
from bin_packing import parcelBinList

f = open('data.json')
data = json.load(f)

parcels = parcelBinList(data)
truckBins = []