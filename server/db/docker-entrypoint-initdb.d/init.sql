create table processes
(
	id int PRIMARY KEY auto_increment,
	type varchar(100) not null,
	action varchar(100) not null,
	target_instance_id int not null,
	finished boolean not null
);

create table target_instances
(
    id int PRIMARY KEY auto_increment,
    type varchar(100) not null,
    authenticate json not null,
    etc json null
);
