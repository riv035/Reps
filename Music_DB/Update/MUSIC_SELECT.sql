select genre_name, count(genre_id) from genre 
join genreband on genre.id = genreband.genre_id
group by genre_name;

select count(album_id) from song
join album on song.album_id = album.id
where year >= '2019' and year <= '2020';

select album_name, avg(song.duration) from album
join song on song.album_id = album.id
group by album_name;

select distinct band_name from band
where band_name not in (
    select distinct band_name from band
    join bandalbum on band.id = bandalbum.band_id 
    join album on album.id = bandalbum.album_id 
    where year = 2020
)
order by band_name;

select collection_name from collection
join collectionsong on collectionsong.collection_id = collection.id
join song on collectionsong.song_id = song.id
join album on song.album_id = album.id
join bandalbum on bandalbum.album_id = album.id
join band on bandalbum.band_id = band.id
where band_name = 'CreamSoda'
group by collection_name;

select album_name, count(genre_name) from album 
join bandalbum on album.id = bandalbum.album_id 
join band on bandalbum.band_id = band.id 
join genreband on band.id = genreband.band_id 
join genre on genre.id = genreband.genre_id 
group by album_name 
having count(genre_name) > 1;

select song_name from song
left join collectionsong on song.id = collectionsong.song_id
where collection_id is null;

select band.band_name, song_name, duration from song
join album on song.album_id = album.id
join bandalbum on bandalbum.album_id = album.id
join band on bandalbum.band_id = band.id 
where duration = (select min(duration) from song);

select distinct album_name from album
join song on song.album_id = album.id
where song.album_id in (
    select album_id from song
    group by album_id
    having count(album_id) = (
         select count(id) from song
         group by album_id
         order by count
         limit 1
)
);

