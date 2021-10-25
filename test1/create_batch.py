from sales.models import Customer

for i in range(1, 11):
    Customer.objects.create(
        customer_id=f'{i:05d}',
        customer_name=f'customer_{i:05d}',
        contact=f'contact_{i:05d}',
        address=f'address_{i:05d}',
    )
        




        
        
        
        
        