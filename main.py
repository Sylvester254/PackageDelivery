from PackageDelvery.src.deliver_packages import manageTrucks, delivered_packages
from PackageDelvery.src.hashtable import HashTable
from PackageDelvery.src.load_data import loadPackageData, loadDistanceData, loadAddressData, addressData, distanceData
from PackageDelvery.src.load_packages import loadPackages
from PackageDelvery.src.truck import Truck
import datetime


def get_all_delivered_packages():
    deliveredPackages = delivered_packages
    return deliveredPackages


def get_package_status_at_time(package_id, time, hashTable):
    # Get the package from the hash table
    package = hashTable.retrieve(package_id)
    # Convert the input time to a datetime object
    input_time = datetime.datetime.strptime(time, "%H:%M %p")
    # Check if the input time is before 9:05 AM
    if input_time < datetime.datetime.strptime("09:05 AM", "%H:%M %p"):
        return "At hub"
    # Check if the package has been delivered by the given time
    elif datetime.datetime.strptime(package.deliveryTime, "%H:%M:%S") <= input_time:
        return "Delivered"
    else:
        return "In transit"


def get_all_package_status_at_time(time, hashTable):
    # Get all the packages from the hash table
    all_packages = [item for sublist in hashTable.table for key, item in sublist]
    # Get the status of each package at the given time
    package_statuses = {package.id: "Delivered" if datetime.datetime.strptime(package.deliveryTime, "%H:%M:%S") <= datetime.datetime.strptime(time, "%H:%M %p") else "In transit" for package in all_packages}
    return package_statuses


def get_truck_by_id(truck_id, truck1, truck2, truck3):
    # Get the truck by its ID
    if truck_id == "1":
        return truck1
    elif truck_id == "2":
        return truck2
    elif truck_id == "3":
        return truck3
    else:
        return None


def main():
    hashTable = HashTable(40)
    loadPackageData(hashTable)
    loadDistanceData(distanceData)
    loadAddressData(addressData)

    # Create three trucks
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
        print("4. Check packages loaded in a truck")
        print("5. Get truck mileage")
        print("6. Exit")

        option = input("> ")

        if option == "1":
            deliveredPackages = get_all_delivered_packages()
            total_mileage = sum([truck.totalMileage for truck in [truck1, truck2, truck3]])
            print(f"Total mileage: {total_mileage} miles")
            for package in deliveredPackages:
                print(f"Package ID: {package.id}, Delivery time: {package.deliveryTime}")
        elif option == "2":
            package_id = input("Enter the package ID: ")
            time = input("Enter the time (HH:MM AM/PM): ")
            package_status = get_package_status_at_time(package_id, time, hashTable)
            print(f"Package ID: {package_id}, Status at {time}: {package_status}")
        elif option == "3":
            time = input("Enter the time (HH:MM AM/PM): ")
            package_statuses = get_all_package_status_at_time(time, hashTable)
            for package_id, status in package_statuses.items():
                print(f"Package ID: {package_id}, Status at {time}: {status}")

        elif option == "4":
            truck_id = input("Enter the truck ID: ")
            truck = get_truck_by_id(truck_id, truck1, truck2, truck3)
            if truck:
                print(f"Truck {truck_id} has the following packages before its departure time:")
                for package in truck.packages:
                    print(package)
            else:
                print("Truck not found.")

        elif option == "5":
            truck_id = input("Enter the truck ID: ")
            truck = get_truck_by_id(truck_id, truck1, truck2, truck3)
            if truck:
                print(f"Total mileage for truck {truck.id} is now {truck.totalMileage} miles")
            else:
                print("Truck not found.")
        elif option == "6":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
