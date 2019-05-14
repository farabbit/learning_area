### problems

fetch
cursor
as
is
procedure



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
#### Inner Join
#### Left Join
#### Right Join
#### full join

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
