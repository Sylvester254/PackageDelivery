"""
This script calculates the distance between two addresses and finds the package closest to a given location.
"""

from .load_data import addressData, distanceData

def distanceBetween(address1, address2):
    """
    This function calculates the distance between two addresses.
    It uses the addressData and distanceData lists to find the distance between the two addresses.
    """
    i = addressData.index(address1)
    j = addressData.index(address2)
    return distanceData[max(i, j)][min(i, j)]

def minDistanceFrom(truck, packagesToLoad):
    """
    This function finds the package whose destination address is closest to the truck's current location.
    It uses the distanceBetween function to calculate the distance between the truck's current location and each package's destination address.
    """
    closest_package = min(packagesToLoad, key=lambda package: distanceBetween(truck.currentLocation, package.address))
    return closest_package
