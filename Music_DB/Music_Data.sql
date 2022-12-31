insert into band(name) 
values('Tame Impala');

insert into band(name) 
values('CreamSoda');

insert into band(name) 
values('RSAC & ELLA');

insert into band(name) 
values('San Cisco');

insert into band(name) 
values('Conjure one');

insert into band(name) 
values('Ariana Grande');

insert into band(name) 
values('Fleetwood Mac');

insert into band(name) 
values('The XX');


insert into genre(name) 
values('Rock');

insert into genre(name) 
values('Indie');

insert into genre(name) 
values('Ambient');

insert into genre(name) 
values('Hip Hop');

insert into genre(name) 
values('Pop');

insert into genre(name) 
values('Techno');


insert into album(name, year) 
values('Extraordinary Ways', '2005');

insert into album(name, year) 
values('Lonerism', '2012');

insert into album(name, year) 
values('Currents', '2015');

insert into album(name, year) 
values('ФЕЛЛА', '2019');

insert into album(name, year) 
values('Красиво', '2018');

insert into album(name, year) 
values('Gracetown', '2015');

insert into album(name, year) 
values('Between You and Me', '2020');

insert into album(name, year) 
values('Sweetener', '2018');

insert into album(name, year) 
values('Rumours', '1977');

insert into album(name, year) 
values('XX', '2009');


insert into song(name, album_id, duration) 
values('Extraordinary Way', '1', '00:04:42');

insert into song(name, album_id, duration) 
values('Face the muic', '1', '00:04:35');

insert into song(name, album_id, duration) 
values('Mind mischief', '2', '00:04:31');

insert into song(name, album_id, duration) 
values('Keep on Lying', '2', '00:05:53');

insert into song(name, album_id, duration) 
values('Let it happen', '3', '00:07:46');

insert into song(name, album_id, duration) 
values('The less i know the better', '3', '00:03:38');

insert into song(name, album_id, duration) 
values('NBA', '4', '00:02:10');

insert into song(name, album_id, duration) 
values('Поезда', '4', '00:03:42');

insert into song(name, album_id, duration) 
values('Хэдшот', '5', '00:04:27');

insert into song(name, album_id, duration) 
values('Уйди но останься', '5', '00:04:15');

insert into song(name, album_id, duration) 
values('Run', '6', '00:03:14');

insert into song(name, album_id, duration) 
values('Snow', '6', '00:03:34');

insert into song(name, album_id, duration) 
values('Skin', '7', '00:04:27');

insert into song(name, album_id, duration) 
values('On the line', '7', '00:05:00');

insert into song(name, album_id, duration) 
values('Succesfull', '8', '00:03:47');

insert into song(name, album_id, duration) 
values('Breathin', '8', '00:03:18');

insert into song(name, album_id, duration) 
values('The chain', '9', '00:04:29');

insert into song(name, album_id, duration) 
values('Dreams', '9', '00:04:17');

insert into song(name, album_id, duration) 
values('VCR', '10', '00:02:57');

insert into song(name, album_id, duration) 
values('My fantasy', '10', '00:02:38');




insert into collection(name, year) 
values('Rhys Fulber Call of Nature', '2010');

insert into collection(name, year) 
values('Greatest Indie Hits', '2016');

insert into collection(name, year) 
values('Попсовая соточка 2019', '2019');

insert into collection(name, year) 
values('Плачем над техно!', '2019');

insert into collection(name, year) 
values('The Best of San Cisco', '2020');

insert into collection(name, year) 
values('Dirtiest Black Bitches 2018', '2018');

insert into collection(name, year) 
values('Awesome Mix vol.2', '2016');

insert into collection(name, year) 
values('The eXXtra collection', '2010');



insert into genreband(genre_id, band_id) 
values('2', '1');

insert into genreband(genre_id, band_id) 
values('6', '2');

insert into genreband(genre_id, band_id) 
values('5', '3');

insert into genreband(genre_id, band_id) 
values('2', '4');

insert into genreband(genre_id, band_id) 
values('3', '5');

insert into genreband(genre_id, band_id) 
values('4', '6');

insert into genreband(genre_id, band_id) 
values('1', '7');

insert into genreband(genre_id, band_id) 
values('2', '8');



insert into bandalbum(album_id, band_id) 
values('1', '5');

insert into bandalbum(album_id, band_id) 
values('2', '1');

insert into bandalbum(album_id, band_id) 
values('3', '1');

insert into bandalbum(album_id, band_id) 
values('4', '3');

insert into bandalbum(album_id, band_id) 
values('5', '2');

insert into bandalbum(album_id, band_id) 
values('6', '4');

insert into bandalbum(album_id, band_id) 
values('7', '4');

insert into bandalbum(album_id, band_id) 
values('8', '6');

insert into bandalbum(album_id, band_id) 
values('9', '7');

insert into bandalbum(album_id, band_id) 
values('10', '8');



insert into collectionsong(collection_id, song_id) 
values('1', '1');

insert into collectionsong(collection_id, song_id) 
values('1', '2');

insert into collectionsong(collection_id, song_id) 
values('2', '3');

insert into collectionsong(collection_id, song_id) 
values('2', '4');

insert into collectionsong(collection_id, song_id) 
values('2', '11');

insert into collectionsong(collection_id, song_id) 
values('2', '19');

insert into collectionsong(collection_id, song_id) 
values('3', '7');

insert into collectionsong(collection_id, song_id) 
values('3', '8');

insert into collectionsong(collection_id, song_id) 
values('4', '9');

insert into collectionsong(collection_id, song_id) 
values('4', '10');

insert into collectionsong(collection_id, song_id) 
values('5', '11');

insert into collectionsong(collection_id, song_id) 
values('5', '12');

insert into collectionsong(collection_id, song_id) 
values('5', '13');

insert into collectionsong(collection_id, song_id) 
values('5', '14');

insert into collectionsong(collection_id, song_id) 
values('6', '15');

insert into collectionsong(collection_id, song_id) 
values('6', '16');

insert into collectionsong(collection_id, song_id) 
values('7', '17');

insert into collectionsong(collection_id, song_id) 
values('8', '19');