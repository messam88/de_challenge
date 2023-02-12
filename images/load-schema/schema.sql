drop table if exists person;
drop table if exists place;


create table `place` (
  `id` int not null auto_increment,
  `city` varchar(80) default null,
  `county` varchar(80) default null,
  `country` varchar(80) default null,
  primary key (`id`)
);

create table `person` (
  `id` int not null auto_increment,
  `place_id` int default null,
  `given_name` varchar(80) default null,
  `family_name` varchar(80) default null,
  `date_of_birth` varchar(80) default null,
  primary key (`id`),
  FOREIGN KEY (place_id) REFERENCES place(id)
);