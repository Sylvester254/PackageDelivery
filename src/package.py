class Package:
    def __init__(self, id, address, city, state, zip, deliveryTime, weight, specialNotes):
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
        return f"Package {self.id}: {self.address}, {self.city}, {self.state}, {self.zip}, Delivery Time: {self.deliveryTime}, Weight: {self.weight}, Special Notes: {self.specialNotes}, Status: {self.status}"
