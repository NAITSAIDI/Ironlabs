SELECT * FROM first_Queries.apple_sample;
select Count("id"), prime_genre from first_Queries.apple_sample
group by prime_genre;

/*1. What are the different genres?*/
select prime_genre from first_Queries.apple_sample;

/*2. Which is the genre with the most apps rated?*/
select track_name, rating_count_tot, prime_genre from first_Queries.apple_sample
order by rating_count_tot desc;

/*3 Which is the genre with most apps?*/
select prime_genre, Count("id") from first_Queries.apple_sample
group by prime_genre
order by count("id") desc;

/* 4 Which is the one with the least?*/
select prime_genre, Count("id") from first_Queries.apple_sample
group by prime_genre
order by count("id") asc;
/* 5 Find the top 10 apps most rated*/
select track_name, rating_count_tot from first_Queries.apple_sample
order by rating_count_tot desc
limit 10;
/* 6 Find the top 10 apps best rated by users*/
select track_name, user_rating from first_Queries.apple_sample
order by user_rating desc
limit 10;
/*7 Take a look at the data you retrieved in question 5. Give some insights*/
select track_name, rating_count_tot, user_rating, prime_genre from first_Queries.apple_sample
order by rating_count_tot desc
limit 10;
# There is no visible corelation between the number of ratings and the rating avenage so it is difficult to express any useful insight
/* 8 Take a look at the data you retrieved in question 6. Give some insights*/
select track_name, user_rating, rating_count_tot, prime_genre from first_Queries.apple_sample
order by user_rating desc
limit 10;
/*9. Now compare the data from questions 5 and 6. What do you see?*/


/*All of the selected apps are above 4 points yet we can see that some of the best rated have been highly rated, but we can alwo see the same number (4,5) on a less rated apps */
select track_name, user_rating, rating_count_tot, price from first_Queries.apple_sample
where user_rating="5"
order by rating_count_tot desc
limit 10;
 /* 