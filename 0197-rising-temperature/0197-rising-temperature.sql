# Write your MySQL query statement below
select id from Weather A where temperature >(
select temperature from weather B 
where B.recordDate=Date_sub(A.recordDate,interval 1 day)
);