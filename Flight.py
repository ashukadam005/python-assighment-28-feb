class Flights:
    def __init__(self, flight_no, source, destination,base_fare):
        self.flight_no = flight_no
        self.source = source
        self.destination  = destination
        self.base_fare = base_fare

    def get_flight_info(self):
        print("Flight No:", self.flight_no)
        print("Source:" , self.source)
        print("Destination:",self.destination)
        return f"Flight_info:source: {self.source} , destination: {self.destination}"

    def calculate_fare(self,passanger_count,discount_percentage=0):
        total_fare = self.base_fare * passanger_count
        print("total fare:",total_fare)

        if discount_percentage > 0:
            discount_amount = total_fare * (discount_percentage/100) 
            total_fare = total_fare - discount_amount
        return total_fare        

    def update_route(self, source=None, destination=None):
        if source and destination:
            self.source = source
            self.destination=destination
        elif destination:
            self.destination = destination


print("---------------------------------------------------")

flight = Flights("AIRIndia1","Pune","banglore",1000)
flight.get_flight_info()

print("---------------------------------------------------")

passangercount_fare = flight.calculate_fare(3)
print("total fare when passanger count is given 3",passangercount_fare)

print("---------------------------------------------------")


passangerdiscount_fare = flight.calculate_fare(3, 10)
print("when passanger 3 and discount 10 is given",passangerdiscount_fare)

print("---------------------------------------------------")

flight.update_route(destination="maldives")
print("after updating dstination:")
print(flight.get_flight_info())
print("---------------------------------------------------")

flight.update_route("mumbai","chennai")
print("After updating source and destination:",flight.get_flight_info())



          
