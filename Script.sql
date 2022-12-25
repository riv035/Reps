create table if not exists Genre (
	id serial primary key,
	name varchar not null
);

create table if not exists Band (
	id serial primary key,
	name varchar not null,
	genre varchar not null
);

create table if not exists Album (
	id serial primary key,
	name varchar not null,
	band varchar not null,
	year integer not null
);

create table if not exists Song (
	id serial primary key,
	name varchar not null,
	album_id integer not null references Album(id),
	duration time not null,
	collection varchar not null
);

create table if not exists Collection (
	id serial primary key,
	name varchar not null,
	year integer not null
);

create table if not exists GenreBand (
	genre_id integer references Genre(id),
	band_id integer references Band(id),
	constraint pk primary key (genre_id, band_id)
);

create table if not exists BandAlbum (
	album_id integer references Album(id),
	band_id integer references Band(id),
	constraint prk primary key (album_id, band_id)
);

create table if not exists CollectionSong (
	collection_id integer references Collection(id),
	song_id integer references Song(id),
	constraint pkey primary key (collection_id, song_id)
);