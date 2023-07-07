import csv
from .package import Package


def loadPackageData(hashTable):
    with open('data/packageCSV.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            id, address, city, state, zip, deliveryTime, weight, specialNotes = row
            package = Package(id, address, city, state, zip, deliveryTime, weight, specialNotes)
            hashTable.insert(id, package)
            # print(f"Loaded package {id} into hash table.")


distanceData = []


def loadDistanceData(distanceData):
    with open('data/distanceCSV.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distanceData.append([float(i) if i else 0.0 for i in row])
        print(f"Loaded {len(distanceData)} rows into distanceData.")


addressData = []


def loadAddressData(addressData):
    with open('data/addressCSV.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            location_name, street_address = row[1], row[2]
            addressData.append((location_name, street_address))
        print(f"Loaded {len(addressData)} addresses into addressData.")
        # print(addressData)
