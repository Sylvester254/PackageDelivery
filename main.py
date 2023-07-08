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

    # Load packages into the trucks
    loadPackages(truck1, hashTable)
    loadPackages(truck2, hashTable)

    # Print out some information about the loaded packages for testing purposes
    print(f"Truck 1 has {len(truck1.packages)} packages:")
    for package in truck1.packages:
        print(f"Package {package.id} to {package.address}")

    print(f"Truck 2 has {len(truck2.packages)} packages:")
    for package in truck2.packages:
        print(f"Package {package.id} to {package.address}")


    # # Print the packages loaded onto each truck for verification
    # print("Packages loaded onto Truck 1:")
    # for package in truck1.packages:
    #     print(package.id)
    #
    # print("\nPackages loaded onto Truck 2:")
    # for package in truck2.packages:
    #     print(package.id)
    #
    # # Test the distanceBetween function
    # print("\nDistance between the first two addresses:")
    # print(distanceBetween(addressData[0], addressData[1]))
    #
    # # Test the minDistanceFrom function
    # print("\nClosest package to Truck 1's current location:")
    # print(minDistanceFrom(truck1))

if __name__ == "__main__":
    main()
