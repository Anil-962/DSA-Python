# Write your MySQL query statement below
select d.name as Department , e.name as Employee, e.salary as Salary
From Employee e
inner join Department d On e.departmentId = d.id
where e.salary =( select Max(salary) from Employee where departmentId =e.departmentId)
