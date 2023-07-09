class Package:
    """
    This class represents a package to be delivered. It contains information about the package's ID, address, city, state,
    zip code, delivery time, weight, special notes, and status. The status is initially set to "At hub".
    """

    def __init__(self, id, address, city, state, zip, deliveryTime, weight, specialNotes):
        """
        Initializes a new instance of the Package class.

        :param id: The package's ID.
        :param address: The package's delivery address.
        :param city: The city of the delivery address.
        :param state: The state of the delivery address.
        :param zip: The zip code of the delivery address.
        :param deliveryTime: The delivery time for the package.
        :param weight: The weight of the package.
        :param specialNotes: Any special notes related to the package.
        """
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryTime = deliveryTime
        self.weight = weight
        self.specialNotes = specialNotes
        self.status = "At hub"

    def __str__(self):
        """
        Returns a string representation of the Package instance.

        :return: A string that represents the package.
        """
        return f"Package {self.id}: {self.address}, {self.city}, {self.state}, {self.zip}, Delivery Time: {self.deliveryTime}, Weight: {self.weight}, Special Notes: {self.specialNotes}, Status: {self.status}"
