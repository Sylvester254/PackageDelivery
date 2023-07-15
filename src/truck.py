class Truck:
    """
    This class represents a delivery truck. It contains information about the truck's ID, current location, packages,
    speed, departure time, total mileage, total delivery time, and the last loaded package.
    The initial current location is set to "4001 South 700 East" (the hub), the speed is set to 18 miles per hour,
    the departure time is set to "09:05 AM", and the total mileage and total delivery time are set to 0.
    """

    def __init__(self, id):
        """
        Initializes a new instance of the Truck class.

        :param id: The truck's ID.
        """
        self.id = id
        self.currentLocation = "4001 South 700 East"
        self.packages = []
        self.speed = 18
        self.departureTime = "08:00 AM"
        self.totalMileage = 0
        self.totalDeliveryTime = 0
        self.lastLoadedPackage = None
