-- hat lists all shows contained in the database hbtn_0d_tvshows --
SELECT t.title, g.name
FROM tv_shows t
LEFT JOIN tv_show_genres tg ON t.id = tg.show_id
ORDER BY t.title ASC, g.name ASC;
