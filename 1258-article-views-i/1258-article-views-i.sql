# Write your MySQL query statement below
SELECT author_id as id from  Views
WHERE author_id=viewer_id
GROUP BY author_id
order by author_id asc;