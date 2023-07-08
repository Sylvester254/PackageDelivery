class Truck:
    def __init__(self, id):
        self.id = id
        self.currentLocation = "4001 South 700 East"  # the hub is at WGU
        self.packages = []
        self.speed = 18  # Speed in miles per hour
        self.departureTime = "08:00 AM"  # Trucks can leave the hub no sooner than 8:00 a.m.
        self.totalMileage = 0
        self.totalDeliveryTime = 0
        self.lastLoadedPackage = None