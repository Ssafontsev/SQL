1
SELECT genre_id, COUNT(artist_id)
FROM genreartist
GROUP BY genre_id
ORDER BY genre_id;
2
SELECT year, COUNT(track.id)
FROM track LEFT JOIN album ON track.album_id = album.id
WHERE year IN ('2019', '2020')
GROUP BY year;
3
SELECT album_name, AVG(time)
FROM track LEFT JOIN album ON track.album_id = album.id
GROUP BY album_name;
4
SELECT artist.name
FROM album
JOIN albumartist ON album.id = albumartist.album_id
JOIN artist ON artist.id = albumartist.album_id
WHERE year != 2020;
5
SELECT co.title
FROM collection co
JOIN trackcollection tc ON co.id = tc.collection_id
JOIN track tr ON tr.id = tc.track_id
JOIN album a ON a.id = tr.album_id
JOIN albumartist aa ON a.id = aa.album_id
JOIN artist ar ON aa.artist_id = ar.id
WHERE ar.name = 'Леонтьев';
6
FROM album a
LEFT JOIN albumartist aa ON a.id = aa.album_id
LEFT JOIN artist ar ON ar.id = aa.artist_id
LEFT JOIN genreartist ga ON ar.id = ga.artist_id
LEFT JOIN genre g ON g.id = ga.genre_id
GROUP BY a.album_name
HAVING COUNT(DISTINCT g.name) > 1
ORDER BY a.album_name
7
SELECT t.title
FROM track t
LEFT JOIN trackcollection tc on t.id = tc.track_id
WHERE tc.track_id IS null
8
SELECT a.album_name, t.time
FROM track t
LEFT JOIN album a ON a.id = t.album_id
LEFT JOIN albumartist aa ON aa.album_id = a.id
LEFT JOIN artist ar ON ar.id = aa.artist_id
GROUP by a.album_name, t.time
HAVING t.time = (SELECT MIN(time) FROM track)
ORDER BY a.album_name
9
SELECT DISTINCT a.album_name
FROM album a
LEFT JOIN track t ON t.album_id = a.id
WHERE t.album_id IN (
    SELECT album_id
    FROM track
    GROUP BY album_id
    HAVING COUNT(id) = (
        SELECT COUNT(id)
        FROM track
        GROUP BY album_id
        ORDER BY COUNT
        LIMIT 1
    )
)
ORDER BY a.album_name