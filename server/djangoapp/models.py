from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
#    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
#    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='car model')
    dealer_id = models.IntegerField(default=50)
    car_type = models.CharField(max_length=5, choices=CAR_TYPES, default=SEDAN)
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Dealer ID: " + str(self.dealer_id) + "," + \
               "Type: " + self.car_type + "," + \
               "Year: " + str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
