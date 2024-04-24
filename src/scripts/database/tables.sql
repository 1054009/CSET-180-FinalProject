create table `users`
(
	`id` int unsigned auto_increment,
	`first_name` varchar(64) not null,
	`last_name` varchar(64) not null,
	`email_address` varchar(64) unique not null,
	`password` blob not null,

	primary key (`id`)
);
