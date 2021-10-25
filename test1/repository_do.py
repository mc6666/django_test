from sales.models import *
from repository import *
from django.db import transaction

# order save
@transaction.atomic
def create_order(cust):
    repo = Repository(Order)
    ord=repo.create(order_id='so_0001',
    customer_id=cust,
    order_date='20210801',
    required_date='20210901',
    )
    
    # 多筆新增
    repo_detail = Repository(Order_Detail)
    repo_product = Repository(Product)
    obj_list = []
    for i in range(1, 4):
        obj = Order_Detail()
        obj.order_id=ord
        obj.product_id=repo_product.get_one(i)
        obj.unit_price=100
        obj.quantity=5
        obj.discount=0
        obj_list.append(obj)
    repo_detail.bulk_create(obj_list)

