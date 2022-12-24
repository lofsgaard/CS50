select avg(rating) from ratings
inner join movies on ratings.movie_id = movies.id
where movies.year = '2012';