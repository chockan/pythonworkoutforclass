CREATE DATABASE my8;
use my8;
use my1;

create table user8(
id int auto_increment primary key,
name varchar(40),
age int,
phonenumber int
);

select * from user7;

insert into user7(name,age,phonenumber)
 values ("shewag",45,123456789),
 ("dhoni",42,456789123);
 
update user7 set name="john" where name="sachin" and id=1;

delete from user7 where name="john" and id=1;

create table user4(
id int auto_increment primary key,
name varchar(40),
age int,
phonenumber int
);

select * from user4;

CREATE TABLE  users3 (
id int auto_increment primary key,
name varchar(40),
age int,
phonenumber int
);
CREATE TABLE  users3 (
id int auto_increment primary key,
white int,
red int,
blue int,
black int,
green int
);


select * from test;
insert into user4(name,age,phonenumber) values("shewag",42,123456789),
("sachin",45,123456789),
("dravid",42,123456789);


INSERT INTO users (name,age,phonenumber) values
("sachin",48,90),("dhoni",2,123456789),
("sachin",48,90),("dhoni",2,123456789);

UPDATE users3
SET name = 'John Doe', age = 30
WHERE id = 1;
ALTER TABLE users3 MODIFY phonenumber varchar(15);
#######################################
ALTER TABLE users3 MODIFY phonenumber varchar(15);

##################################
UPDATE users3
SET phonenumber = '1234567890'
WHERE id = 1;

UPDATE users3
SET phonenumber = '0987654321'
WHERE id = 2;

UPDATE users3
SET 
    name = CASE 
        WHEN id = 1 THEN 'John Doe'
        WHEN id = 2 THEN 'Jane Smith'
    END,
    age = CASE
        WHEN id = 1 THEN 30
        WHEN id = 2 THEN 25
    END
WHERE id IN (1, 2);


UPDATE users3
SET name = 'Jane Smith', age = 25
WHERE id = 2;

UPDATE user4
SET name="john"
WHERE name = 'sachin' and id=3;

DELETE FROM user4
WHERE name = 'john' and id=3;