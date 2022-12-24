select title
from movies
inner join stars on stars.movie_id = movies.id
inner join ratings on ratings.movie_id = movies.id
inner join people on people.id = stars.person_id
where people.name like 'Chadwick Boseman'
order by ratings.rating desc
limit 5;