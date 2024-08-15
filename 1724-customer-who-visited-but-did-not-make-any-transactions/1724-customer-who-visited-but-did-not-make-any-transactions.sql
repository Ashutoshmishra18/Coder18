# Write your MySQL query statement below
select customer_id,count(visits.visit_id) as count_no_trans
from visits
left join transactions
using(visit_id)
where transactions.transaction_id is null
group by 1;