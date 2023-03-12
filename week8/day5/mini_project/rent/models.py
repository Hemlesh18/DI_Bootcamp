from django.db import models

# Create your models here.
# customer model
class  Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
    
#vechcle type
class Vehicle_type(models.Model):
    Vehicle_type_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Vehicle_type_name
    
#vehicle size
class Vehicle_size(models.Model):
    Vehicle_size_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Vehicle_size_name
    
#vehicle 
class Vehicle(models.Model):
    Vehicle_type = models.ForeignKey(Vehicle_type,on_delete=models.CASCADE)
    Vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.Vehicle_type} {self.Vehicle_size}"
    

#rental
class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date= models.DateTimeField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

#rental rate 
class Rental_rate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)





    

        