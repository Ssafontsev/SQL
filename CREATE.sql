create table Genre (
	id serial primary key,
	name varchar(50) not null
);
create table Artist (
	id serial primary key,
	name varchar(50) not null
);
create table GenreArtist (
    primary key(artist_id, genre_id)
    artist_id integer references Artist(id) not null,
    genre_id integer references Genre(id) not null
);
create table Album (
	id serial primary key,
	album_name varchar not null,
	year integer check(year > 0) not null
);
create table AlbumArtist (
    primary key(album_id, artist_id)
    album_id integer references Album(id) not null,
    artist_id integer references Artist(id) not null
);
create table Collection (
	id serial primary key,
	title varchar(50) not null,
	year integer check(year > 0) not null
);
create table Track (
	id serial primary key,
	title varchar(50) not null,
	time integer check(time > 0) not null,
	album_id integer references Album(id) not null
);
create table TrackCollection (
    primary key(track_id, collection_id)
    track_id integer references Track(id) not null,
    collection_id integer references Collection(id) not null
);