-- sqlite3 maragi.db < maragi_schema.sql

drop table if exists user;
create table user (
  id integer primary key autoincrement,
  name text not null
);

drop table if exists goal;
create table goal (
  id integer primary key autoincrement,
  user_id integer,
  title text not null
);

drop table if exists action;
create table action (
  id integer primary key autoincrement,
  goal_id integer,
  description text
);
