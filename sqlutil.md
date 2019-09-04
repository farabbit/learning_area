# sql

## daily

## advanced

```sql
--
insert in to table1 ('id2'), select column2, column3 from table1 where id='id1';

--table stucture
desc tablename;

--sysdate
select * from sys_dict where upper(type)='SYSDATE';

--top 100
select * from tablename where ROWNUMBER<=100;

--dual
select to_date('2019', 'yyyy') from dual;

--查看表依赖
select * from user_dependencies t where t.referenced_name = 'tablename';

--复制表
--DB source:
grant all on tableSource to userSource;
--DB target
create table tableR as select * from userSource.tableSource;
insert into tableR select * from userSource.tableSource;
```
