select name, year from album
where year = 2018;

select name, duration from song
order by duration desc limit 1;

select name from song
where duration >= '00:03:30';

select name from collection
where year between 2018 AND 2020;

select name from band
where name not like '% %';

select name from song
where lower(name) like lower('%my%');





