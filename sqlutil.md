# sql

## daily

## advanced

```sql
--table stucture
desc tablename;

--sysdate
select * from sys_dict where upper(type)='SYSDATE';

--top 100
select * from tablename where ROWNUMBER<=100;

--dual
select to_date('2019', 'yyyy') from dual;
```
