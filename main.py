"""
This script is the main entry point for the WGUPS package delivery system.
It provides a CLI for users to interact with the system and check the status of packages and trucks.
"""

from src.deliver_packages import manageTrucks, delivered_packages, package_to_truck
from src.hashtable import HashTable
from src.load_data import loadPackageData, loadDistanceData, loadAddressData, addressData, distanceData
from src.load_packages import loadPackages
from src.truck import Truck
import datetime


def get_all_delivered_packages():
    """
    This function returns all packages that have been delivered.
    """
    deliveredPackages = delivered_packages
    return deliveredPackages


def get_package_status_at_time(package_id, time, hashTable, package_to_truck):
    # Get the package from the hash table
    package = hashTable.retrieve(package_id)
    # Determine the departure time based on the truck delivering the package
    if package_to_truck[package.id] == 1:
        departure_time = datetime.datetime.strptime("08:00 AM", "%H:%M %p")
    else:
        departure_time = datetime.datetime.strptime("09:05 AM", "%H:%M %p")
    # Check if the package has been delivered by the given time
    if package.deliveryTime == 'EOD':
        package_delivery_time = datetime.datetime.strptime('23:59:59', "%H:%M:%S")
    else:
        package_delivery_time = datetime.datetime.strptime(package.deliveryTime, "%H:%M:%S")
    user_time = datetime.datetime.strptime(time, "%H:%M %p")
    if user_time < departure_time:
        status = "At hub"
    elif package_delivery_time <= user_time:
        status = "Delivered"
    else:
        status = "In transit"
    # Check if the package is package #9 and if the given time is before 10:20 AM
    if package_id == "9" and user_time < datetime.datetime.strptime("10:20 AM", "%H:%M %p"):
        address = "Third District Juvenile Court"
        zip = "84103"
    else:
        address = package.address
        zip = package.zip
    return status, address, zip


def get_all_package_status_at_time(time, hashTable, package_to_truck):
    all_packages = [item for sublist in hashTable.table for key, item in sublist]
    input_time = datetime.datetime.strptime(time, "%H:%M %p")
    package_statuses = {}
    for package in all_packages:
        # Determine the departure time based on the truck delivering the package
        if package_to_truck[package.id] == 1:
            departure_time = datetime.datetime.strptime("08:00 AM", "%H:%M %p")
        else:
            departure_time = datetime.datetime.strptime("09:05 AM", "%H:%M %p")
        if input_time < departure_time:
            package_statuses[package.id] = "At hub"
        elif datetime.datetime.strptime(package.deliveryTime, "%H:%M:%S") <= input_time:
            package_statuses[package.id] = "Delivered"
        else:
            package_statuses[package.id] = "En route"
        # Check if the package is package #9 and if the given time is before 10:20 AM
        if package.id == "9" and input_time < datetime.datetime.strptime("10:20 AM", "%H:%M %p"):
            package.address = "Third District Juvenile Court"
            package.zip = "84103"
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
                package_status, address, zip = get_package_status_at_time(package_id, time, hashTable, package_to_truck)
                if package_status:
                    package = hashTable.retrieve(package_id)
                    print(
                        f"Package ID: {package.id}, Address: {address}, {package.city}, {package.state} {zip}, Status at {time}: {package_status}")
                else:
                    print("Package not found.")
            elif option == "3":
                time = input("Enter the time (HH:MM AM/PM): ")
                package_statuses = get_all_package_status_at_time(time, hashTable, package_to_truck)
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
