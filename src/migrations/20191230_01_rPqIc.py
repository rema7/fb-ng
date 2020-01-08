"""

"""

from yoyo import step

__depends__ = {}


steps = [
    step(
        """
        create table account(
           uuid char(36) char set ascii not null primary key,
           email varchar(128) not null,
           name varchar(512) not null,
           password varchar(128) not null,
           last_name varchar(512) not null,
           age tinyint not null,
           sex varchar(32) not null,
           country varchar(256) not null,
           created_at datetime default now(),
           updated_at datetime default now()
        );
        """, "DROP TABLE account"
    ),
    step(
        """
        create table hobby(
           id int not null auto_increment primary key unique,
           name varchar(512) not null
        );
        """, "DROP TABLE hobby"
    ),
    step(
        """
        create table account_hobby(
           account_id char(36) char set ascii not null ,
           hobby_id int not null,
           foreign key (account_id) references account(uuid),
           foreign key (hobby_id) references hobby(id),
           primary key (account_id, hobby_id)
        );
        """, "DROP TABLE account_hobby"
    )
]
