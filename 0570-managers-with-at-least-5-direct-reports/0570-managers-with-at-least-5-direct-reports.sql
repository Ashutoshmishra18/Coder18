SELECT name 
FROM Employee
WHERE id in (
    SELECT managerId
    From Employee
    GROUP BY managerID
    Having count(*)>=5
);