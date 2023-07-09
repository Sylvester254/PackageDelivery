"""
This script is the main entry point for the WGUPS package delivery system.
It provides a CLI for users to interact with the system and check the status of packages and trucks.
"""

from PackageDelvery.src.deliver_packages import manageTrucks, delivered_packages
from PackageDelvery.src.hashtable import HashTable
from PackageDelvery.src.load_data import loadPackageData, loadDistanceData, loadAddressData, addressData, distanceData
from PackageDelvery.src.load_packages import loadPackages
from PackageDelvery.src.truck import Truck
import datetime


def get_all_delivered_packages():
    """
    This function returns all packages that have been delivered.
    """
    deliveredPackages = delivered_packages
    return deliveredPackages


def get_package_status_at_time(package_id, time, hashTable):
    # Get the package from the hash table
    package = hashTable.retrieve(package_id)
    # Check if the package has been delivered by the given time
    if package.deliveryTime == 'EOD':
        package_delivery_time = datetime.datetime.strptime('23:59:59', "%H:%M:%S")
    else:
        package_delivery_time = datetime.datetime.strptime(package.deliveryTime, "%H:%M:%S")
    user_time = datetime.datetime.strptime(time, "%H:%M %p")
    if package_delivery_time <= user_time:
        return "Delivered"
    else:
        return "In transit"



def get_all_package_status_at_time(time, hashTable):
    """
    This function returns the status of all packages at a given time.
    """
    all_packages = [item for sublist in hashTable.table for key, item in sublist]
    input_time = datetime.datetime.strptime(time, "%H:%M %p")
    package_statuses = {}
    for package in all_packages:
        if input_time < datetime.datetime.strptime("09:05 AM", "%H:%M %p"):
            package_statuses[package.id] = "At hub"
        elif datetime.datetime.strptime(package.deliveryTime, "%H:%M:%S") <= input_time:
            package_statuses[package.id] = "Delivered"
        else:
            package_statuses[package.id] = "En route"
    return package_statuses


def get_truck_by_id(truck_id, truck1, truck2, truck3):
    """
    This function returns a truck object based on its ID.
    """
    if truck_id == "1":
        return truck1
    elif truck_id == "2":
        return truck2
    elif truck_id == "3":
        return truck3
    else:
        return None


def main():
    """
    This is the main function that runs the WGUPS package delivery system.
    It initializes the system and provides a CLI for users to interact with the system.
    """
    hashTable = HashTable(40)
    loadPackageData(hashTable)
    loadDistanceData(distanceData)
    loadAddressData(addressData)

    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)

    packagesToLoad = [item for sublist in hashTable.table for key, item in sublist if item.status == "At hub"]

    packagesToLoad = loadPackages(truck1, packagesToLoad, hashTable)
    packagesToLoad = loadPackages(truck2, packagesToLoad, hashTable)
    packagesToLoad = loadPackages(truck3, packagesToLoad, hashTable)

    manageTrucks(truck1, truck2, truck3, hashTable)

    while True:
        print("\nWelcome to the WGUPS package delivery system!")
        print("Please select an option:")
        print("1. Get all package status and total mileage")
        print("2. Get a single package status with time")
        print("3. Get all package status with time")
        print("4. Get a truck's mileage")
        print("5. Exit")

        option = input("> ")

        try:
            if option == "1":
                deliveredPackages = get_all_delivered_packages()
                if deliveredPackages:
                    total_mileage = sum([truck.totalMileage for truck in [truck1, truck2, truck3]])
                    print(f"Total mileage: {total_mileage} miles")
                    for package in deliveredPackages:
                        print(
                            f"Package ID: {package.id}, Address: {package.address}, {package.city}, {package.state} {package.zip}, Delivery time: {package.deliveryTime}")
                else:
                    print("No packages have been delivered yet.")
            elif option == "2":
                package_id = input("Enter the package ID: ")
                time = input("Enter the time (HH:MM AM/PM): ")
                package_status = get_package_status_at_time(package_id, time, hashTable)
                if package_status:
                    package = hashTable.retrieve(package_id)
                    print(
                        f"Package ID: {package.id}, Address: {package.address}, {package.city}, {package.state} {package.zip}, Status at {time}: {package_status}")
                else:
                    print("Package not found.")
            elif option == "3":
                time = input("Enter the time (HH:MM AM/PM): ")
                package_statuses = get_all_package_status_at_time(time, hashTable)
                if package_statuses:
                    for package_id, status in package_statuses.items():
                        package = hashTable.retrieve(package_id)
                        print(
                            f"Package ID: {package.id}, Address: {package.address}, {package.city}, {package.state} {package.zip}, Status at {time}: {status}")
                else:
                    print("No packages found.")
            elif option == "4":
                truck_id = input("Enter the truck ID: ")
                truck = get_truck_by_id(truck_id, truck1, truck2, truck3)
                if truck:
                    print(f"Total mileage for truck {truck.id} is now {truck.totalMileage} miles")
                else:
                    print("Truck not found.")
            elif option == "5":
                break
            else:
                print("Invalid option. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e} \n Enter expected inputs")


if __name__ == "__main__":
    main()
