from .distance import distanceBetween, minDistanceFrom


def loadPackages(truck, packagesToLoad, hashTable):
    # Packages that must go out for delivery on the same truck
    sameTruckPackages = [13, 14, 15, 16, 19, 20, 25, 30]  # Include package 25 and 30
    # Packages that may only be delivered by truck 2
    truck2OnlyPackages = [3, 18, 36, 38, 6]  # Include package 6
    # Packages that cannot leave the hub before 9:05 a.m
    lateDeparturePackages = [28, 32]  # Remove package 6 and 25

    # Remove the late departure packages from the packagesToLoad list
    if truck.id != 3:
        for id in lateDeparturePackages:
            package = hashTable.retrieve(str(id))
            if package and package in packagesToLoad:
                packagesToLoad.remove(package)

    # Load packages that have specific truck requirements
    if truck.id == 2:
        for id in truck2OnlyPackages:
            package = hashTable.retrieve(str(id))
            if package and package in packagesToLoad:
                truck.packages.append(package)
                packagesToLoad.remove(package)
                truck.lastLoadedPackage = package
    elif truck.id == 1:
        for id in sameTruckPackages:
            package = hashTable.retrieve(str(id))
            if package and package in packagesToLoad:
                truck.packages.append(package)
                packagesToLoad.remove(package)
                truck.lastLoadedPackage = package
    elif truck.id == 3:
        # Add the late departure packages back to the packagesToLoad list
        for id in lateDeparturePackages:
            package = hashTable.retrieve(str(id))
            if package and package not in packagesToLoad:
                packagesToLoad.append(package)
        for id in lateDeparturePackages:
            package = hashTable.retrieve(str(id))
            if package and package in packagesToLoad:
                truck.packages.append(package)
                packagesToLoad.remove(package)
                truck.lastLoadedPackage = package

    # Find the package closest to the current location
    while len(truck.packages) < 16 and packagesToLoad:
        closest_package = minDistanceFrom(truck, packagesToLoad)
        # Check constraints for specific packages
        if (closest_package.id in truck2OnlyPackages) or \
                (closest_package.id in sameTruckPackages and truck.id != 1) or \
                (closest_package.id in lateDeparturePackages and truck.id != 3):
            continue

        truck.packages.append(closest_package)
        packagesToLoad.remove(closest_package)
        truck.lastLoadedPackage = closest_package

    # Return the updated list of packages to load
    return packagesToLoad
