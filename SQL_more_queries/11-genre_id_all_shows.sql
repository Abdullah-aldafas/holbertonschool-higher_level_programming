-- hat lists all shows contained in the database hbtn_0d_tvshows --
SELECT t.title, g.name
FROM tv_shows t
LEFT JOIN tv_show_genres tg ON t.id = tg.show_id
LEFT JOIN tv_genres g ON tg.genre_id = g.id
ORDER BY t.title ASC, g.name ASC;
