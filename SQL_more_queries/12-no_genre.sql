-- lists all shows contained in hbtn_0d_tvshows without a genre linked --
SELECT t.title, tg.genre_id
FROM tv_show AS t
LEFT JOIN tv_show_genres AS ts
ON t.id = ts.show_id
WHERE ts.genre_id IS NULL
ORDER BY t.title ASC, ts.genre_id ASC;