from customer.models import Customer, Order 

def perform_db_operations():
    
    Customer.objects.all().delete()
    Order.objects.all().delete()

    
    my_new_customer = Customer()
    my_new_customer.name = "ABC Corp."
    my_new_customer.email = "testuser8@example.com"
    my_new_customer.save()

    xyz_corp = Customer()
    xyz_corp.name = "XYZ Corporation"
    my_new_customer.name = "testuser2@example.com"
    xyz_corp.save()

    customer_one = Customer.objects.get(name = "XYZ Corporation")
    print(customer_one.name)
    customer_one.name = "Some new name"
    customer_one.save()


    Customer.objects.create(name = "Plumbing Specialists", email = "testuser3@example.com")
    Customer.objects.create(name = "Electronic Experts", email = "testuser4@example.com")
    Customer.objects.create(name = "Structural Consultants", email = "testuser5@example.com")

    
    customer = Customer.objects.get(name = "Electronic Experts")
    print(customer.name)

    results = Customer.objects.filter(name__startswith=("Plumb"))
    print(results.count())
    print(results[0].name)

    customer = Customer.objects.all()
    print(customer.count())

    results = Customer.objects.exclude(name__startswith=("Plumb"))
    print(results.count())
    print(results[0].name)
    print(results[1].name)
    print(results[2].name)

    customers = Customer.objects.all()
    print(customers)
    print(customers[0])
    print(customers[0].name)
    print(customers[1].name)

    the_customer = Customer.objects.get(name = "Electronic Experts")
    order1 = Order(customer=the_customer, total_price=25.99, total_items=3)
    order1.save()
    order2 = Order(customer=the_customer, total_price=12.99, total_items=1)
    order2.save()