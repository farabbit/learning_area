### problems

fetch
cursor
as
is
procedure
<br/>


### Procedure

**structure**
```
CREATE PROCEDURE proc_name [(@parameter varchar(10)] [, @outPara varchar(10) output]
	AS [???]
	BEGIN
		select * from sales.salesReason;
	END
GO
```

**run & delete**
```
execute proc_name ['value'|@parameter='value']

drop procedure proc_name
```

### Join
```
SELECT Table1.column1, Table2.column2
	From Table1
	[] JOIN Table2
	ON Table1.id == Table2.id
```
> Inner Join
> Left Join
> Right Join
> full join
<br/>


### Transactions
**四大原则 ACID**
> 原子性
> 一致性
> 隔离性
> 持久性

**Controls**
> commit
> rollback
> savepoint		create savepoint
> set transaction	???
<br/>


### Begin, End, Go

**Begin ... Exception ... End**
> make several codes into a logical block
**Go** for T-SQL
> tell SQLServer a set of code ends, execute those code and continue

<br/>

### Cursor
##### a memory workspace that save temprory data blocks from database
**type**
> 隐式Cursor
> 显式Cursor
> Ref Cursor (Dynamic Cursor)

**隐式Cursor**
Select Into / Update / Insert / Delete -> these only get one data from db at one time
> SQL%ROWCOUNT			Int
> SQL%FOUND | SQL%NOTFOUNT	Bool
> SQL%ISOPEN			Bool
sample here
```
Set Serveroutput on;

begin
    update t_contract_master set liability_state = 1 where policy_code = '123456789';  
      
    if SQL%Found then  
       dbms_output.put_line('the Policy is updated successfully.');  
       commit;  
    else  
      dbms_output.put_line('the policy is updated failed.');  
    end if;  
  
end;   
/
```
<br/>

**显式Cursor**
Properties
> %ROWCOUNT		Int
> %FOUND | %NOTFOUND	Bool
> %ISOPEN		Bool

How to use -> four steps
> define	Cursor [CursorName] IS;
> open		Open [CursorName];
> manipulate	Fetch [CursorName];
> close		Close [CursorName]; -- DO NOT FOGOT THIS STEP
<br/>

**Ref Cursor**
> pass
<br/ >

##### How to use
[See this](https://blog.csdn.net/mydreamneverstop/article/details/78604033)
<br/>


### 授权命令 Grant, Revoke
##### Grant: 承认，准许，同意，授予，拨款
**structure**
```
GRANT <permission> ON TABLE tableName[(columnName)] TO <username> [WITH GRANT OPTION]
or
GRANT <permission> ON <dataObject> FROM <username>
```
> dataObject -> column name or row name
> permission means operations to db -> select, update ```
##### Revoke: 撤销，废除，取消
**structure**
```
REVOKE <permission> ON TABLE <tableName[(columnName)]> FROM <username> [CASCADE | RESTROCT]
```






