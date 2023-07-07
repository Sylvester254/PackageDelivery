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