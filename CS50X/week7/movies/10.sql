select name
from people
inner join directors on directors.person_id = people.id
inner join ratings on directors.movie_id = ratings.movie_id
where ratings.rating >= '9.0';