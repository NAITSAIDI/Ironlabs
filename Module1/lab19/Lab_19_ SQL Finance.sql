SELECT * FROM olist.order_items LIMIT 10;

-- Q1. From the order_items table, find the price of the highest priced order and lowest price order.
SELECT order_id, price FROM olist.order_items ORDER BY price DESC LIMIT 1;
SELECT order_id, price FROM olist.order_items ORDER BY price ASC LIMIT 1;

-- Q2. From the order_items table, what is range of the shipping_limit_date of the orders?
-- Range can be expresed from the first date to the last
-- First date:
SELECT shipping_limit_date FROM olist.order_items ORDER BY shipping_limit_date LIMIT 1;
-- Last date:
SELECT shipping_limit_date FROM olist.order_items ORDER BY shipping_limit_date DESC LIMIT 1;

-- Q3. From the customers table, find the states with the greatest number of customers.
-- First I get familiar with the Table 
SELECT * FROM olist.customers LIMIT 10;
-- Now I will group customers by counting their id and grouping them by thier state
SELECT customer_state, count(customer_id)G FROM olist.customers GROUP BY customer_state ORDER BY count(customer_id) DESC;
-- To show only the first one:
SELECT customer_state, count(customer_id)G FROM olist.customers GROUP BY customer_state ORDER BY count(customer_id) DESC LIMIT 1;
-- I want to check if I get the same results if I will use customer_unique_id
SELECT customer_state, count(customer_unique_id)G FROM olist.customers GROUP BY customer_state ORDER BY count(customer_unique_id) DESC LIMIT 1;

-- Q4. From the customers table, within the state with the greatest number of customers, find the cities with the greatest number of customers.
-- Below 20 cities with the highest number of customers
SELECT customer_city, count(customer_id) FROM olist.customers WHERE customer_state = 'SP' GROUP BY customer_city ORDER BY count(customer_id) DESC LIMIT 20;

-- Q5. From the closed_deals table, how many distinct business segments are there (not including null)?
-- See the table
SELECT * FROM olist.closed_deals LIMIT 10;
-- Answer:
SELECT DISTINCT business_segment FROM olist.closed_deals WHERE business_segment <> 'Null';

-- Q6. From the closed_deals table, sum the declared_monthly_revenue for duplicate row values in business_segment 
-- and find the 3 business segments with the highest declared monthly revenue (of those that declared revenue).
SELECT business_segment, sum(declared_monthly_revenue) FROM olist.closed_deals
GROUP BY business_segment
ORDER BY sum(declared_monthly_revenue) DESC
LIMIT 3;

-- Q7. From the order_reviews table, find the total number of distinct review score values.
-- See the Table:
SELECT * FROM olist.order_reviews
LIMIT 10;
-- Answer:
SELECT review_score, count(DISTINCT review_id) FROM olist.order_reviews
GROUP BY review_score
ORDER BY review_score DESC;

-- Q8.  In the order_reviews table, create a new column with a description 
-- that corresponds to each number category for each review score from 1 - 5, 
-- then find the review score and category occurring most frequently in the table.
SELECT review_score, count(review_score),
CASE WHEN review_score = '1' THEN 'Terrible'
WHEN review_score = '2' THEN 'Bad'
WHEN review_score = '3' THEN 'Acceptable'
WHEN review_score = '4' THEN 'Good'
ELSE 'Very Good!'
END AS Description_review
FROM olist.order_reviews
GROUP BY review_score
ORDER BY count(review_score) DESC;
-- The most frequent:
SELECT review_score, count(review_score) as Frequency,
CASE WHEN review_score = '1' THEN 'Terrible'
WHEN review_score = '2' THEN 'Bad'
WHEN review_score = '3' THEN 'Acceptable'
WHEN review_score = '4' THEN 'Good'
ELSE 'Very Good!'
END AS Description_review
FROM olist.order_reviews
GROUP BY review_score
ORDER BY count(review_score) DESC
LIMIT 1;

-- Q9. From the order_reviews table, find the review value occurring most frequently and how many times it occurs.
-- The most frequent:
SELECT review_score, count(review_score) as Frequency,
CASE WHEN review_score = '1' THEN 'Terrible'
WHEN review_score = '2' THEN 'Bad'
WHEN review_score = '3' THEN 'Acceptable'
WHEN review_score = '4' THEN 'Good'
ELSE 'Very Good!'
END AS Description_review
FROM olist.order_reviews
GROUP BY review_score
ORDER BY count(review_score) DESC
LIMIT 1;