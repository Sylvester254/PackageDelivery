from .load_data import addressData, distanceData


def distanceBetween(address1, address2):
    i = addressData.index(address1)
    j = addressData.index(address2)
    return distanceData[max(i, j)][min(i, j)]




def minDistanceFrom(truck, packagesToLoad):
    # Find the package whose destination address is closest to the truck's current location
    closest_package = min(packagesToLoad, key=lambda package: distanceBetween(truck.currentLocation, package.address))
    return closest_package

