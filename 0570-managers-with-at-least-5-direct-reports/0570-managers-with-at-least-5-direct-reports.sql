# Write your MySQL query statement below
SELECT h.name FROM Employee h
JOIN Employee i ON h.id=i.managerID
GROUP BY i.managerID
HAVING COUNT(*)>=5;
