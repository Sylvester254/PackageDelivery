from PackageDelvery.src.deliver_packages import truckDeliverPackages
from PackageDelvery.src.distance import distanceBetween, minDistanceFrom
from PackageDelvery.src.hashtable import HashTable
from PackageDelvery.src.load_data import loadPackageData, loadDistanceData, loadAddressData, addressData, distanceData
from PackageDelvery.src.load_packages import loadPackages
from PackageDelvery.src.truck import Truck


def main():
    hashTable = HashTable(40)  # Adjust the size according to your data
    loadPackageData(hashTable)
    loadDistanceData(distanceData)
    loadAddressData(addressData)

    # Create two trucks
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)

    # Create a list of packages that need to be loaded
    # packagesToLoad = [item for sublist in hashTable.table for key, item in sublist if item.status == "At hub"]

    packagesToLoad = [item for sublist in hashTable.table for key, item in sublist if item.status == "At hub"]

    packagesToLoad = loadPackages(truck1, packagesToLoad, hashTable)
    packagesToLoad = loadPackages(truck2, packagesToLoad, hashTable)
    packagesToLoad = loadPackages(truck3, packagesToLoad, hashTable)

    print("Truck 1 has the following packages:")
    for package in truck1.packages:
        print(package)
    print("Truck 2 has the following packages:")
    for package in truck2.packages:
        print(package)
    print("Truck 3 has the following packages:")
    for package in truck3.packages:
        print(package)

    addy1 = addressData[0]
    addy2 = addressData[3]

    # Test the distanceBetween function
    # print(f"\nDistance between the first two addresses:{addy1} and {addy2}")
    # print(distanceBetween(addy1, addy2))


    # # Create a Truck object
    # truck = Truck(1)
    #
    # # def printHashTable(hashTable):
    # #     for index in range(hashTable.size):
    # #         for key, value in hashTable.table[index]:
    # #             print(f"Key: {key}, Value: {value}")
    #
    # # Print the contents of the hash table
    # #printHashTable(hashTable)
    #
    # packagesTobeLoaded = [hashTable.retrieve(str(i)) for i in range(1, 40)]
    #
    # closest_package = minDistanceFrom(truck, packagesTobeLoaded)
    #
    # # Print the address of the closest package
    # print(
    #     f"The package that is closest to the truck's current delivery location is package {closest_package.id} to {closest_package.address}")

    # loadSameTruckPackages(truck1, hashTable)
    # print("Truck 1 has the following packages:")
    # for package in truck1.packages:
    #     print(package)

    truckDeliverPackages(truck1)

if __name__ == "__main__":
    main()
