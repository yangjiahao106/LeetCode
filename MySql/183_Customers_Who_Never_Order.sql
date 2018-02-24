
#方法一：
select Name Customers
from Customers
where id  not in (select CustomerId from Orders)

#方法二：
select Name Customers
from Customers c
left join Orders o on o.CustomerId = c.id
where o.CustomerId is NULL

