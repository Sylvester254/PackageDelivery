import csv
from .package import Package


def loadPackageData(hashTable):
    """
    This function loads package data from a CSV file into a hash table.
    Each row in the CSV file represents a package with its details.
    """
    with open('data/packageCSV.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            id, address, city, state, zip, deliveryTime, weight, specialNotes = row
            package = Package(id, address, city, state, zip, deliveryTime, weight, specialNotes)
            hashTable.insert(id, package)
            # print(f"Loaded package {id} into hash table.")


distanceData = []


def loadDistanceData(distanceData):
    """
    This function loads distance data from a CSV file into a list.
    Each row in the CSV file represents a list of distances.
    """
    with open('data/distanceCSV.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distanceData.append([float(i) if i else 0.0 for i in row])



addressData = []


def loadAddressData(addressData):
    """
    This function loads address data from a CSV file into a list.
    Each row in the CSV file represents an address.
    """
    with open('data/addressCSV.csv', 'r') as file:
        reader = csv.reader(file)
        # For each row in the CSV file, add the address to the list
        for row in reader:
            address = row[2]
            addressData.append(address)
