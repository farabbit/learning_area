# bash

## variables

--------------------------

### difine  

> DO NOT put space arround "="  

```bash
var="xxx"
```

### use

```bash
echo $var OR echo ${var}  
```

### delete

```bash
unset var  
```

### variable type

> local variable  
> envrionment variable  
> shell variable  

## string

--------------------------

### single quote

> CAN NOT put variables or "\\" inside

### double quo

> CAN put variables or "\\" inside

### montage string

```bash
greetings='hello, '$your_name' !'
```

### string length

```bash
str="abcd"
echo ${#str}
```

### sub string

```bash
str="abcdefg"
echo ${str:1:4} # out: bcde
```

## array

--------------------------

### define

```bash
arr=(value0 value1 value2)
arr[0]=value0
```

### read

```bash
echo ${arr[0]}
```

### length

```bash
length=${#arr[@]}
# OR
length=${#arr[*]}
# var length inside array
length0=${#arr[0]}
```

## shell notes

```bash
# single line
:<<!
mutiple line # as a function
!

```

## parameters

--------------------------

### sample

- $n: nth parameter

```bash
echo "parameter0: $0"
```

### special character

| special char | explanations                                      |
| :----------- | :------------------------------------------------ |
| $#           | parameter count                                   |
| $\*          | return every parameter when with " arround        |
| $@           | return every parameter with ' arround when with " |
| $\$          | process ID                                        |
| $!           | last process ID at background                     |
| $-           | display shell options                             |
| $?           | display                                           |
