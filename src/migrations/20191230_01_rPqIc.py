"""

"""

from yoyo import step

__depends__ = {}

CREATE_TABLE = '''
create table account(
   uuid char(36) char set ascii not null primary key,
   name varchar(512) not null,
   last_name varchar(512) not null,
   age tinyint not null,
   sex enum('male', 'female', 'other') not null,
   country varchar(256) not null,
   created_at datetime default now(),
   updated_at datetime default now()
);
create table hobby(
   id int not null auto_increment primary key,
   name varchar(512) not null
);
create table account_hobby(
   account_id char(36) char set ascii not null ,
   hobby_id int not null,
   foreign key (account_id) references account(uuid),
   foreign key (hobby_id) references hobby(id),
   primary key (account_id, hobby_id)
);

'''

DROP_TABLE = '''
DROP TABLE account_hobby;
DROP TABLE hobby;
DROP TABLE account;
'''

steps = [
    step(CREATE_TABLE, DROP_TABLE)
]
