-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table players(id serial primary key, name text);

create table matches(id serial primary key, player1 int references players (id), player2 int references players (id), winner int references players (id));

create table rounds(level int, match int references matches (id));
