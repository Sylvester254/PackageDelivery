from .load_data import addressData, distanceData


def distanceBetween(address1, address2):
    # Use the addressData and distanceData lists to find the distance between two addresses
    return distanceData[addressData.index(address1)][addressData.index(address2)]

def minDistanceFrom(truck):
    # Use the distanceBetween function to find the package destination address that is closest to the truck's current location
    min_distance = float('inf')
    closest_package = None
    for package in truck.packages:
        distance = distanceBetween(truck.currentLocation, package.address)
        if distance < min_distance:
            min_distance = distance
            closest_package = package
    return closest_package.address if closest_package else None
