from .load_data import addressData, distanceData


def distanceBetween(address1, address2):
    try:
        index1 = next(i for i, v in enumerate(addressData) if v[1] == address1)
        index2 = next(i for i, v in enumerate(addressData) if v[1] == address2)
    except StopIteration:
        print(f"Error: Address not found in addressData. Address1: {address1}, Address2: {address2}")
        return None
    return distanceData[index1][index2]


def minDistanceFrom(truck):
    min_distance = float('inf')
    closest_package = None
    for package in truck.packages:
        distance = distanceBetween(truck.currentLocation, package.address)
        if distance < min_distance:
            min_distance = distance
            closest_package = package
    return closest_package.address if closest_package else None

