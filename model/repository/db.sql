-- Save User
insert into users
    (code, name, family, username, password, role, locked)
values
    (3, 'ahmad', 'messbah', 'ahmad', 'ahmad123', 'teacher',0);


-- Search - Find
select *
from users
where code = 1;

select *
from users
where username='ali' and password='ali123';


-- Edit
update users set name='aaaa', family='bbbb', username='aaaaa', password='aaa1233', role='alaki', locked=0
where code=1;

-- Delete
delete from users where code =1;