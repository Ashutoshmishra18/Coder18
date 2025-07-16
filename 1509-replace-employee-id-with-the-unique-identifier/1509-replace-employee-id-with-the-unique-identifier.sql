# Write your MySQL query statement below
Select a.unique_id as unique_id, b.name as name
from Employees b left join EmployeeUNI a on b.id=a.id