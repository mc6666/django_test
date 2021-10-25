from sales.models import *
from repository import *

# 指定類別名稱
repo = Repository(Customer)

# 單筆查詢，query by pk
cust = repo.get_one(2)
print(cust.customer_name)

# 多筆查詢，customer_name含0000，且id>=5
obj_list = repo.get_many(customer_name__contains='0000', id__gte=5)
for obj in obj_list:
    print(obj.customer_name)



# 單筆新增
i=11        
obj = Customer()
obj.customer_id=f'{i:05d}'
obj.customer_name=f'customer_{i:05d}'
obj.contact=f'contact_{i:05d}'
obj.address=f'address_{i:05d}'
repo.save(obj)
print(obj.id)

# 單筆刪除
repo.delete(11)

# 另一種單筆新增
i=12        
obj=repo.create(customer_id=f'{i:05d}',
    customer_name=f'customer_{i:05d}',
    contact=f'contact_{i:05d}',
    address=f'address_{i:05d}',
    )
print(obj.id)

# 單筆刪除
repo.delete_object(obj)


# 更新
obj = repo.get_one(1)
obj.customer_id=f'XXX'
repo.save(obj)

# 多筆新增
obj_list = []
for i in range(11, 21):
    obj = Customer()
    obj.customer_id=f'{i:05d}'
    obj.customer_name=f'customer_{i:05d}'
    obj.contact=f'contact_{i:05d}'
    obj.address=f'address_{i:05d}'
    obj_list.append(obj)
repo.bulk_create(obj_list)




repo_product = Repository(Product)
obj_list = []
for i in range(1, 11):
    obj = Product()
    obj.product_id=f'{i:05d}'
    obj.product_name=f'product_{i:05d}'
    obj_list.append(obj)
repo.bulk_create(obj_list)

from sales.models import *
from repository import *
from repository_do import *

# 取得客戶物件
repo = Repository(Customer)
cust = repo.get_one(2)

# 新增一筆訂單，含表頭(Order)、表身(Order_detail)
create_order(cust)
  


