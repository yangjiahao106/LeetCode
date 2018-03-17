
# 注意：
# 错误'You can not specify target table p1 for update in FROM clause'
# 需要再套一层select
# delect from 只有一个表时不能使用别名

--方法一
delete
from Person
where id not in
(select m.mi from
    (select min(id) mi from Person group by email) m
)

-- 方法二
delete p1
from Person p1, Person p2
where p1.Email = p2.Email and
p1.Id > p2.Id