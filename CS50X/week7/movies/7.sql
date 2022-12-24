select title, ratings.rating
from movies
INNER JOIN ratings on ratings.movie_id = movies.id
where year like '2010'
order by rating desc, title asc;