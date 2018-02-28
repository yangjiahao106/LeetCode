
#方法一

SELECT d.name AS Department, e.name AS Employee, e.Salary AS Salary
FROM Employee e
INNER JOIN department d ON e.DepartmentId = d.Id
WHERE e.salary = ( SELECT MAX(salary) FROM Employee WHERE departmentId = d.id)

方法二
SELECT D.Name AS Department ,E.Name AS Employee ,E.Salary
FROM
	Employee E,
	(SELECT DepartmentId,max(Salary) as max FROM Employee GROUP BY DepartmentId) T,
	Department D
WHERE E.DepartmentId = T.DepartmentId
  AND E.Salary = T.max
  AND E.DepartmentId = D.id

