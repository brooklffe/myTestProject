create table tb7(
    id int not null primary key auto_increment,
    name varchar(64) not null,
    password char(64) not null,
    email varchar(64) not null,
    age tinyint,
    salary decimal(10,2),-- 精确数字，10位最高，2位小数
    ctime datetime
)default charset=utf8;

insert into tb7(name,password,email,age,salary,ctime) values("zhangsan",123123,'123@123',29,1000.21,'2024-12-12 11:11:11');