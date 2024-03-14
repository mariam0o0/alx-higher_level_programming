-- List all Comedy shows in hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres a ON tv_shows.id = a.show_id
INNER JOIN tv_genres b ON a.genre_id = b.id
WHERE b.name = 'Comedy'
ORDER BY tv_shows.title ASC;
