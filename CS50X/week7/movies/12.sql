select title
from movies
inner join stars on stars.movie_id = movies.id
inner join people on people.id = stars.person_id
where people.name like 'Johnny Depp'
INTERSECT
select title
from movies
inner join stars on stars.movie_id = movies.id
inner join people on people.id = stars.person_id
where people.name like 'Helena Bonham Carter';