from vehicle import Vehicle

class Car(Vehicle):


# By defining our secific init method on a Car class, the python nterpreter will call it when we take an instance of a Car, but it only will call one init method.  So, the Vehicle init method will not be automatically called.  We have to manually call it in the Car init method, so that we create a proper instance of a Vehicle

  def __init__(self, price, ab_count, material="cloth"):
    self.price = price
    self.seat_material = material
    self.airbag_count = ab_count
    super().__init__("car")

  def calc_payments(self, months, rate):
    return f"Your payments for a purchase price of ${self.price} over {months} at {rate} would be too high. Buy something cheaper."
