from django.shortcuts import render
from .models import Customer
from faker import Faker

# Create your views here.
def fake_data(request):
    fake = Faker()
    for _ in range (5):
    
        last_name=fake.last_name()
        first_name=fake.first_name()
        email=fake.email()
        city=fake.city()
        country=fake.country()
        phone_number=fake.msisdn()
        address= fake.address()


        #create new customer
        Customer.objects.create(
            last_name=last_name,
            first_name=first_name,
            email=email,
            city=city,
            country=country,
            phone_number=phone_number,
            address=address
        )
        #print (f"{last_name}, {first_name},{email},{city}, {country},{phone_number},{address}")


    #access the customer entries
    customers = Customer.objects.all()

    #print the customers 
    for customer in customers:
        print (customer)





    return render(request, "fake_data.html")