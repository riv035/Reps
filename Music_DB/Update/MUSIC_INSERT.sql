insert into band(band_name) values
	('Tame Impala'),
	('CreamSoda'),
	('RSAC & ELLA'),
	('San Cisco'),
	('Conjure one'),
	('Ariana Grande'),
	('Fleetwood Mac'),
	('The XX');


insert into genre(genre_name) values
	('Rock'),
	('Indie'),
	('Ambient'),
	('Hip Hop'),
	('Pop'),
	('Techno');


insert into album(album_name, year) values
	('Extraordinary Ways', '2005'),
	('Lonerism', '2012'),
	('Currents', '2015'),
	('ФЕЛЛА', '2019'),
	('Красиво', '2018'),
	('Gracetown', '2015'),
	('Between You and Me', '2020'),
	('Sweetener', '2018'),
	('Rumours', '1977'),
	('XX', '2009');


insert into song(song_name, album_id, duration) values
	('Extraordinary Way', '1', '00:04:42'),
	('Face the muic', '1', '00:04:35'),
	('Mind mischief', '2', '00:04:31'),
	('Keep on Lying', '2', '00:05:53'),
	('Let it happen', '3', '00:07:46'),
	('The less i know the better', '3', '00:03:38'),
	('NBA', '4', '00:02:10'),
	('Поезда', '4', '00:03:42'),
	('Пустота внутри', '4', '00:03:23'),
	('Хэдшот', '5', '00:04:27'),
	('Уйди но останься', '5', '00:04:15'),
	('Run', '6', '00:03:14'),
	('Snow', '6', '00:03:34'),
	('Skin', '7', '00:04:27'),
	('On the line', '7', '00:05:00'),
	('Succesfull', '8', '00:03:47'),
	('Breathin', '8', '00:03:18'),
	('The chain', '9', '00:04:29'),
	('VCR', '10', '00:02:57'),
	('My fantasy', '10', '00:02:38');


insert into collection(collection_name, year) values
	('Rhys Fulber Call of Nature', '2010'),
	('Greatest Indie Hits', '2016'),
	('Попсовая соточка 2019', '2019'),
	('Плачем над техно!', '2019'),
	('The Best of San Cisco', '2020'),
	('Dirtiest Black Bitches 2018', '2018'),
	('Awesome Mix vol.2', '2016'),
	('The eXXtra collection', '2010');



insert into genreband(genre_id, band_id) values
	('2', '1'),
	('6', '2'),
	('4', '3'),
	('5', '3'),
	('2', '4'),
	('3', '5'),
	('4', '6'),
	('1', '7'),
	('2', '8');



insert into bandalbum(album_id, band_id) values
	('1', '5'),
	('2', '1'),
	('3', '1'),
	('4', '3'),
	('5', '2'),
	('6', '4'),
	('7', '4'),
	('8', '6'),
	('9', '7'),
	('10', '8');



insert into collectionsong(collection_id, song_id) values
	('1', '1'),
	('1', '2'),
	('2', '3'),
	('2', '4'),
	('2', '11'),
	('2', '19'),
	('3', '7'),
	('3', '8'),
	('4', '9'),
	('4', '10'),
	('5', '11'),
	('5', '12'),
	('5', '13'),
	('5', '14'),
	('6', '15'),
	('6', '16'),
	('7', '17'),
	('8', '19');