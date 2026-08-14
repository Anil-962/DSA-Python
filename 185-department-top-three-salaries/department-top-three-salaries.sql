# Write your MySQL query statement below
# Write your MySQL query statement below
select d.name as Department , e.name as Employee, e.salary as Salary
From Employee e
inner join Department d On e.departmentId = d.id
where 3>( select count(distinct(e1.salary))
from Employee e1
where e1.salary>e.salary
and e.departmentId =e1.departmentId)
