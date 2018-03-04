# 子查询不能使用limit
# count 可以计算有相同数据时的名次。

select d.name Department, e.name Employee, e.salary Salary
from Employee e
inner join Department d on e.DepartmentId = d.id
where 3 > (select count(distinct(e2.salary))
            from employee e2
            where e2.DepartmentId = e.DepartmentId and
                salary > e.salary)
order by d.id , e.salary desc