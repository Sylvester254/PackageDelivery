"""
This script manages the delivery of packages by trucks.
It includes functions to manage the delivery of packages by multiple trucks, deliver packages by a single truck, and deliver a single package.
"""

from PackageDelvery.src.distance import minDistanceFrom, distanceBetween
import datetime

delivered_packages = []


def manageTrucks(truck1, truck2, truck3, hashTable):
    """
      This function manages the delivery of packages by three trucks.
      It determines the order in which the trucks should deliver their packages based on the delivery deadlines of the packages.
      """
    # Convert the truck's departure time to a datetime object
    current_time = datetime.datetime.strptime("09:05 AM", "%H:%M %p")

    # Deliver packages for Truck 1
    delivered_packages1 = truckDeliverPackages(truck1, hashTable, current_time)

    # Check if the current time is before 9:05 AM
    if current_time < datetime.datetime.strptime("09:05 AM", "%H:%M %p"):
        current_time = datetime.datetime.strptime("09:05 AM", "%H:%M %p")

    # Deliver packages for Truck 2
    delivered_packages2 = truckDeliverPackages(truck2, hashTable, current_time)

    # Get the delivery time of the last package delivered by each truck
    last_delivery_time1 = datetime.datetime.strptime(delivered_packages1[-1].deliveryTime, "%H:%M:%S")
    last_delivery_time2 = datetime.datetime.strptime(delivered_packages2[-1].deliveryTime, "%H:%M:%S")

    # Determine the time when Truck 3 can start delivering packages
    truck3_start_time = max(last_delivery_time1, last_delivery_time2)
    if truck3_start_time < datetime.datetime.strptime("09:05", "%H:%M"):
        truck3_start_time = datetime.datetime.strptime("09:05", "%H:%M")

    # Set the departure time for Truck 3
    truck3.departureTime = truck3_start_time.strftime("%H:%M %p")


    delivered_packages3 = truckDeliverPackages(truck3, hashTable, truck3_start_time)




def truckDeliverPackages(truck, hashTable, current_time):
    """
    This function manages the delivery of packages by a single truck.
    It determines the order in which the truck should deliver its packages based on the delivery deadlines of the packages.
    """
    # Convert the truck's departure time to a datetime object
    departure_time = current_time

    # Packages that need to be delivered early
    earlyDeliveryPackages = [1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40]
    veryEarlyDeliveryPackages = [15]

    # Create a list of early delivery packages in the truck
    early_packages = [p for p in truck.packages if str(p.id) in map(str, veryEarlyDeliveryPackages + earlyDeliveryPackages)]
    early_package_ids = [p.id for p in early_packages]

    # While there are early delivery packages in the truck
    while early_packages:
        # Find the package that is closest to the current location of the truck
        closest_package = minDistanceFrom(truck, early_packages)
        # deliverPackage(closest_package, truck, hashTable, delivered_packages, departure_time)
        departure_time = deliverPackage(closest_package, truck, hashTable, delivered_packages, departure_time)
        early_packages.remove(closest_package)

    # While there are packages in the truck
    while truck.packages:
        # Find the package that is closest to the current location of the truck
        closest_package = minDistanceFrom(truck, truck.packages)
        # deliverPackage(closest_package, truck, hashTable, delivered_packages, departure_time)
        departure_time = deliverPackage(closest_package, truck, hashTable, delivered_packages, departure_time)

    # Return the list of delivered packages
    return delivered_packages


def deliverPackage(package, truck, hashTable, delivered_packages, departure_time):
    """
      This function delivers a single package.
      It updates the status of the package, the current location of the truck, and the total mileage of the truck.
      """
    # Check if the current time is after 10:20 AM and if the package is package #9
    if departure_time > datetime.datetime.strptime("10:20 AM", "%H:%M %p") and package.id == str(9):
        # Update the address of package #9
        package.address = "410 S State St"
        package.zip = "84111"

    # Calculate the distance to the delivery address
    distance = distanceBetween(truck.currentLocation, package.address)

    # Calculate the time it will take to deliver the package
    delivery_time = departure_time + datetime.timedelta(hours=distance / truck.speed)

    # Deliver the package

    # Update the truck's current location
    truck.currentLocation = package.address

    # Update the package's status
    package.status = "Delivered"
    # Record the time the package was delivered
    package.deliveryTime = delivery_time.strftime("%H:%M:%S")
    # Update the package in the hash table
    hashTable.insert(package.id, package)

    # Add the package to the list of delivered packages
    if package not in delivered_packages:
        delivered_packages.append(package)

    # Remove the package from the truck's list of packages
    truck.packages.remove(package)

    # Update the truck's departure time to the delivery time
    departure_time = delivery_time

    # Update the total mileage for the truck
    truck.totalMileage += distance

    return departure_time