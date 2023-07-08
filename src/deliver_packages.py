def truckDeliverPackages(truck):
    # Loop through all the packages in the truck
    for package in truck.packages:
        # Deliver the package
        print(f"Delivering package {package.id} to {package.address}")
        # Update the truck's current location
        truck.currentLocation = package.address
        # Update the package's status
        package.status = "Delivered"
        print(f"Package {package.id} has been delivered.")
