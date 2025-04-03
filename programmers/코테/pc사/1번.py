# SELECT 
#     c.email,
#     COUNT(s.id) AS total
# FROM 
#     customers c
# LEFT JOIN 
#     sites s ON c.id = s.customer_id AND s.is_active = TRUE
# GROUP BY 
#     c.id, c.email
# ORDER BY 
#     c.email ASC;
