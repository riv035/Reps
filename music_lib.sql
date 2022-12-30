create table if not exists genre (
	id serial primary key,
	name varchar not null
);

create table if not exists band (
	id serial primary key,
	name varchar not null
);

create table if not exists album (
	id serial primary key,
	name varchar not null,
	year integer not null
);

create table if not exists song (
	id serial primary key,
	name varchar not null,
	album_id integer not null references album(id),
	duration time not null
);

create table if not exists collection (
	id serial primary key,
	name varchar not null,
	year integer not null
);

create table if not exists genreband (
	genre_id integer references genre(id),
	band_id integer references band(id),
	constraint pk primary key (genre_id, band_id)
);

create table if not exists bandalbum (
	album_id integer references album(id),
	band_id integer references band(id),
	constraint prk primary key (album_id, band_id)
);

create table if not exists collectionsong (
	collection_id integer references collection(id),
	song_id integer references song(id),
	constraint pkey primary key (collection_id, song_id)
);