
#方法一：子查询 不等于：<> 不等于NULL：is not NULL
select Name Employee
from Employee m1
where m1.ManagerId is not NULL
    and m1.Salary >= (select Salary from Employee m2 where m1.ManagerId = m2.Id );

#方法二：联结
select E.Name Employee
from Employee E
    left outer join Employee M
    on E.ManagerId = M.Id
where E.ManagerId is not NULL
    and E.Salary > M.Salary;

#方法三： 使用where 联结
select m1.Name Employee
from Employee m1, Employee m2
where m1.ManagerId = m2.Id
and m1.Salary > m2.Salary
