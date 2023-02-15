-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT t.title AS title
    FROM tv_shows AS t
    WHERE t.id = (
        SELECT *
            FROM tv_genres AS g
            WHERE g.name = 'Comedy'
    )
 ORDER BY t.title;
