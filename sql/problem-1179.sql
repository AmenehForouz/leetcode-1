/*
Problem 1179 - Reformat Department Table

Write an SQL query to reformat the table such that there is a department 
id column and a revenue column for each month.
*/

SELECT id,
MAX(CASE WHEN month LIKE "Jan" THEN revenue ELSE null END) AS Jan_Revenue,
MAX(CASE WHEN month LIKE "Feb" THEN revenue ELSE null END) AS Feb_Revenue,
MAX(CASE WHEN month LIKE "Mar" THEN revenue ELSE null END) AS Mar_Revenue,
MAX(CASE WHEN month LIKE "Apr" THEN revenue ELSE null END) AS Apr_Revenue,
MAX(CASE WHEN month LIKE "May" THEN revenue ELSE null END) AS May_Revenue,
MAX(CASE WHEN month LIKE "Jun" THEN revenue ELSE null END) AS Jun_Revenue,
MAX(CASE WHEN month LIKE "Jul" THEN revenue ELSE null END) AS Jul_Revenue,
MAX(CASE WHEN month LIKE "Aug" THEN revenue ELSE null END) AS Aug_Revenue,
MAX(CASE WHEN month LIKE "Sep" THEN revenue ELSE null END) AS Sep_Revenue,
MAX(CASE WHEN month LIKE "Oct" THEN revenue ELSE null END) AS Oct_Revenue,
MAX(CASE WHEN month LIKE "Nov" THEN revenue ELSE null END) AS Nov_Revenue,
MAX(CASE WHEN month LIKE "Dec" THEN revenue ELSE null END) AS Dec_Revenue
FROM Department
GROUP BY id