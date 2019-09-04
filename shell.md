# shell

## advanced

### export

> 在一个shell脚本程序中定义变量，当该脚本运行时，这个定义的变量只是该脚本程序内 的一个局部变量，其他的shell不能引用它，要使某变量值可以在其他shell中被改变，可以用export对已定义的变量输出。export命令使系统在创建每个新shell时定义这个变量的一个拷贝。这个过程称之为变量输出。

```shell
# add new PATH to linux only for this login
export a=`ls`
```

## basic

```shell
#!/bin/bash

# commenting
# one line commenting
:<<EOF
Multiple line commenting
EOF

# variable
var0="abc"
echo var0

# string
str0="var0: "$var0"."
str1="var0:$var0."
str2="var0: ${var0}."
# length
echo "length of var0:${#var0}"

# substring
str3="abcdefg"
echo ${str3:1:4} # output bcde
# find substring
echo `expr index "$str3" ef` # output 4 (find e OR f)
```

### array

```shell
# array
array0=(str0 str1 str2)
# read
valueN=${array0[n]}
echo ${array0[@]} # with @ can get all element in array
# array length
length=${#array_name[@]} # @ or * both ok
```

### parameters

```shell
# parameters: $d
echo $0 # filename
echo $1 # first parameter
echo $2 # second parameter

# others
$# # number of parameters
$* # string of all parameters, like "$1 $2 $3"
$@ # stromg pf all parameters, like "$1""$2""$3"
$$ # process id
$! # last process id of linux backend
$- # options
$? # exit status of last command, 0->no error, others->error

# read parameters
read name
echo $name
```

### operator

with [] surronded: will return bool

```shell
# calculation
`expr "$1 + 1"`
`awk "$2 + 2"`
# calculate operators
+-*/
%
=
== !=

# relational operator
-eq -ne # equal, non equal
-gt -lt # greater than, less than
-ge -le # greter or equal, less or equal
echo [$1 -eq 1]

# bool operator
! # not
-o # or
-a # and

# logic operator
&& # logic and
|| # logic or

# string operator
= !=
-z # if is empty string
-n # if is non empty string
$ # if is empty string

# file testing operator
-b file # if is block device file
-c file # if is charactor device file
-d file # if is directory
-f file # if is normal file (non folder or device file)
-p file # if is 有名管道

-g file # if is ...
-k file # if is setted Stiky bit (黏着位)
-u file # if is seted SUID bit
-r/-w/-x file # if is readable/writeable/executable
-s file # if is non empty file
-e file # if file/directory exists
```

### echo

### redirect

```shell
# > redirect write
# >> redirect add
command >> file1
# >& redirect and save to the same file
command > file1 2>&1 # save both stdout & stderr to file1
```

| character | filename | hardware |
| :-------- | :------- | :------- |
| 0         | stdin    | keyboard |
| 1         | stdout   | monitor  |
| 2         | stderror | monitor  |

###

#### switch case

```shell
case $round in
1)  roundTime=1530 ;;
2)  roundTime=1705 ;;
3)  roundTime=1900 ;;
4)  roundTime=eod
    echo "EOD round" ;;
*)  echo "[Error] invalid round input"
    exit 1 ;;
esac
```
