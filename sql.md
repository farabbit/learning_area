# sql

## utilities

select columns

```sql
SELECT t.COLUMN_NAME FROM USER_TAB_COLUMNS t where t.TABLE_NAME='SENTRY_SETTLEMENTINSTRUCTION';
```

## concepts

### Pseudo-column

1. sysdate, systimestamp
2. RowNum, RowID
   * RowNum = sequence when select rows
   * RowID = physical identifier in table space
3. CURRVAL, NEXTVAL
4. UID, USER
5. Level
6. ORA_ROWSCN

### Datatype

Datetimes:

1. DATE
2. TIMESTAMP
3. TIMESTAMP WITH TIME ZONE
4. TIMESTAMP WITH LOCAL TIME ZONE

Intervals:

1. INTERVAL YEAR TO MONTH
2. INTERVAL DAY TO SECIBD

#### DATE & TIMESTAMP & INTERVAL

SYSDATE + 1 = tomorrow
SYSDATE + (10/1440) = ten minutes from now

| elements                  | TO_* datetime | Description                                             |
| :------------------------ | :------------ | :------------------------------------------------------ |
| -/,.;:"text"              | YES           | Punctuation and quoted text will bereproduced in result |
| AD A.D.                   | YES           | AD indicator                                            |
| BC B.C.                   | YES           | BC indicator                                            |
| CC SCC                    |               | Centery                                                 |
| Y YY YYY YYYY SYYYY Y,YYY | YES           | Year                                                    |
| YEAR SYEAR                |               | Year spelled out                                        |
| Q                         |               | Quater                                                  |
| MM                        | YES           | Month (1-12)                                            |
| MON                       | YES           | Abbreviated name of month                               |
| Month                     | YES           | Month                                                   |
| RM                        | YES           | Roman numeral month                                     |
| WW                        |               | Week of year                                            |
| W                         |               | Week of month                                           |
| D                         | YES           | Day of Week, depends on NLS terriory                    |
| DAY                       | YES           | Name of the day                                         |
| DD                        | YES           | Day of month (1-31)                                     |
| DDD                       | YES           | Day of year (1-366)                                     |
| DL                        | YES           | Long date format                                        |
| DS                        | YES           | Short date format                                       |
| DY                        | YES           | Abbreviated name of day                                 |
| AM A.M. PM P.M.           | YES           | Meridian indicator                                      |
| HH HH12                   | YES           | hour of day                                             |
| HH24                      | YES           | hoyr of day                                             |
| MI                        | YES           | minutes                                                 |
| SS                        | YES           | Second (0-59)                                           |
| SSSSS                     | YES           | Seconds pass midnight (0-86399)                         |




### 1. Sequence

实现多表ID的一致性

create

```sql
CREATE SEQUENCE [schema_name . ] sequence_name  
  [ AS [ built_in_integer_type | user-defined_integer_type ] ]  
  [ START WITH <constant> ]  
  [ INCREMENT BY <constant> ]  
  [ { MINVALUE [ <constant> ] } | { NO MINVALUE } ]  
  [ { MAXVALUE [ <constant> ] } | { NO MAXVALUE } ]  
  [ CYCLE | { NO CYCLE } ]  
  [ { CACHE [ <constant> ] } | { NO CACHE } ]  
  ;
```

use

```sql
IF EXISTS(SELECT * FROM sys.sequences WHERE name = N'TestSeq')
    DROP SEQUENCE TestSeq;
GO
--创建序列对象 
CREATE SEQUENCE TestSeq AS TINYINT
    START WITH 1
    INCREMENT BY 1;
GO
--创建表
CREATE TABLE TEST(ID tinyint,  Name varchar(150))
--产生序列号码并插入表中
INSERT INTO TEST(ID,Name) VALUES(NEXT VALUE FOR TestSeq, 'allen')
INSERT INTO TEST(ID,Name) VALUES(NEXT VALUE FOR TestSeq, 'kevin')

SELECT * FROM TEST
```

### 2. Procedure

structure

``` sql
CREATE PROCEDURE proc_name [(@parameter varchar(10)] [, @outPara varchar(10) output]
  AS [settings]
  BEGIN
    select * from sales.salesReason;
  END
GO
```

run & delete

```sql
execute proc_name ['value'|@parameter='value']

drop procedure proc_name
```

### 3. Join

```sql
SELECT Table1.column1, Table2.column2
  From Table1
  [] JOIN Table2
  ON Table1.id == Table2.id
```

> Inner Join
> Left Join  
> Right Join  
> full join

### 4. Transactions

#### 四大原则 ACID

> 原子性 Atomic  
> 一致性 Consistent  
> 隔离性 Isolation  
> 持久性 Duration

#### 事务

##### 隔离级别

* Read uncommitted
  * Dirty read
  > 可能读到其他人未commit的数据
* Read committed
  * 不可重复读 Non repeatable read
  > 重复读同一数据，另一个事务恰好在此时修改了此数据，第一个事务中两此读取可能不一致
* Reapeatable read
  * 幻读 Phamtom read
  > 查询记录时发现不存在，另一个事务插入此数据后，第一个事务仍无法查询到，但可以更新
* Serializable
  > 最严格的级别，事务只可串行执行，效率大大下降

##### Controls

> commit  
> rollback  
> savepoint -> create savepoint  
> set transaction	??? 

### 5. Begin, End, Go

#### Begin ... Exception ... End

> make several codes into a logical block

**Go** for T-SQL
> tell SQLServer a set of code ends, execute those code and continue

### 6. Cursor

> a memory workspace that save temprory data blocks from database

#### type

> 隐式Cursor  
> 显式Cursor  
> Ref Cursor (Dynamic Cursor)  

#### 隐式Cursor

Select Into / Update / Insert / Delete -> these only get one data from db at one time
| command                   | return |
| :------------------------ | -----: |
| SQL%ROWCOUNT              |    Int |
| SQL%FOUND or SQL%NOTFOUNT |   Bool |
| SQL%ISOPEN                |   Bool |

sample here

``` sql
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

#### 显式Cursor

Properties
| command             | return |
| :------------------ | -----: |
| %ROWCOUNT           |    Int |
| %FOUND or %NOTFOUND |   Bool |
| %ISOPEN             |   Bool |

how to
| four steps |                 to use |
| :--------- | ---------------------: |
| define     | Cursor [CursorName] IS |
| open       |      Open [CursorName] |
| manipulate |     Fetch [CursorName] |
| close      |     Close [CursorName] |

#### Ref Cursor

> pass

##### How to use

[Also see this link](https://blog.csdn.net/mydreamneverstop/article/details/78604033)

### 6. 授权命令 Grant, Revoke

#### Grant: 承认，准许，同意，授予，拨款

structure

```sql
GRANT <permission> ON TABLE tableName[(columnName)] TO <username> [WITH GRANT OPTION]
or
GRANT <permission> ON <dataObject> FROM <username>
```

> dataObject -> column name or row name  
> permission means operations to db -> select, update

#### Revoke: 撤销，废除，取消

structure

```sql
REVOKE <permission> ON TABLE <tableName[(columnName)]> FROM <username> [CASCADE | RESTROCT]
```

### spool

将sql输出写入到文件中

### 聚合查询 = COUNT, AVG, MAX, MIN + groupby

### 多表查询

