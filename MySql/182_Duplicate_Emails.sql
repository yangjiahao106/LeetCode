
#方法一：子查询
select Email
from (select Email ,count(Email) c from Person group by Email) e
where e.c > 1

#方法二：having筛选
select Email
from Person
group by Email
having count(*) > 1