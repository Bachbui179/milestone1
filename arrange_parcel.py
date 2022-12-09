#this function find all parcels that come to the same city
import json

f = open('data.json')
parcel = json.load(f)

def sortParcel(data):
    data.sort(key = lambda x: x['destination'])

    parcelList = []

    while len(data) != 0:
        items = []
        
        for i in data:
            if i['destination'] == data[0]['destination']:
                items.append(i)   
            else:
                continue 
        for i in items:
            data.remove(i)

        parcelList.append(items)
    
    return parcelList