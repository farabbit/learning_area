# linux

## advanced

### grep

```shell
grep [-options] <pattern> <file>
egrep = grep with regular expression
```

| Options      | Description                           |
| :----------- | :------------------------------------ |
| -c           | Calculation times of matches          |
| -i           | Ignore case                           |
| -n           | Output with line index                |
| -v           | Reverse search(lines without matches) |
| -e pattern   | Use regex in pattern                  |
| -f file      | put file path                         |
| --color=auto | Highlight matches                     |

### ps

```shell
ps -ef | grep <pattern>
```

### crontab

#### -l -> display current jobs

| display            | MIN    | HOUR   | DAY    | MON    | WEEK  | COMMAND |
| :----------------- | :----- | :----- | :----- | :----- | :---- | :------ |
| possible value     | 0-59,* | 0-23,* | 1-31,* | 1-12,* | 0-6,* | command |
| example 1          | 30     | 7      | 8      | *      | *     | ls      |
| 每月8号7：30执行ls |
| example 2          | 0      | */2    | *      | *      | *     | ls      |
| 每两小时执行ls     |

> \* -> every
> \*/15 -> every 15

#### -e -> edit or add new cron
