from .distance import distanceBetween
from .load_data import addressData


def loadPackages(truck, hashTable):
    # Assuming packagesToLoad is a list of packages that need to be loaded
    packagesToLoad = [item for sublist in hashTable.table for key, item in sublist if item.status == "At hub"]
    # Packages that must go out for delivery on the same truck
    sameTruckPackages = [13, 14, 15, 16, 19, 20]
    # Packages that may only be delivered by truck 2
    truck2OnlyPackages = [3, 18, 36, 38]
    # Packages that cannot leave the hub before 9:05 a.m.
    lateDeparturePackages = [6, 25, 28, 32]

    # Load packages that must go out for delivery on the same truck
    if truck.id == 1:
        for id in sameTruckPackages:
            package = hashTable.retrieve(id)
            if package and package in packagesToLoad:
                truck.packages.append(package)
                packagesToLoad.remove(package)

    # Load packages that may only be delivered by truck 2
    if truck.id == 2:
        for id in truck2OnlyPackages:
            package = hashTable.retrieve(id)
            if package and package in packagesToLoad:
                truck.packages.append(package)
                packagesToLoad.remove(package)

    # Load other packages
    while len(truck.packages) < 16 and packagesToLoad:
        # Find the package closest to the current location
        # print(f"Truck's current location: {truck.currentLocation}")
        # print(f"{addressData}")
        closest_package = min(packagesToLoad, key=lambda package: distanceBetween(truck.currentLocation, package.address))
        # Do not load packages that cannot leave the hub before 9:05 a.m. if it's not yet 9:05 a.m.
        if closest_package.id in lateDeparturePackages and truck.departureTime < "09:05 AM":
            continue
        truck.packages.append(closest_package)
        packagesToLoad.remove(closest_package)


def deliverPackage(truck, package):
    # Update the package's status and delivery time
    package.status = "Delivered"
    package.deliveryTime = currentTime  # You'll need to keep track of the current time
    # Remove the package from the truck's list of packages
    truck.packages.remove(package)
    # Update the truck's total mileage and total delivery time
    truck.totalMileage += distanceBetween(truck.currentLocation, package.address)
    truck.totalDeliveryTime += distanceBetween(truck.currentLocation, package.address) / truck.speed
    # Update the truck's current location
    truck.currentLocation = package.address
