#### tips
> git只能跟踪文本文件的改动，二进制文件不行

## Repository 版本库
**commands**
basic
> git init --> init a repository inside this dir
> git add <filename1> [<filename...>] --> tell git that add this file to repository
> git commit --> commit changes
>> git commit -m "message" --> add message while commit

status & diff
> git status --> 
> git diff --> difference

version control
> git log --> check every prev commit
> git reset --hard <HEAD<^ | ~nbr> | <commitId>>
>> HEAD^^^^ or HEAD~4 means prev 4th commit
> git reflog --> check prev commands

cancel changes
> git checkout -- <filaname> --> rollback this file  to prev commit or add
> git reset HEAD <filename> --> 撤销暂存区的修改
>> git checkout -- <filename> --> 如果文件已经存入暂存区，可以执行这两条命令取消

delete
> git rm --> delete file from repository
> rm <filename> & git checkout -- <filename> --> recover file from remove
<br/>

## Remote repository 远程库
##### How to use
* Create SSH key
> ssh-keygen -t rsa -c "email@example.com" -> write this in shell or Git bash to create a SSH key
>> .ssh dir: id_rsa, id_rsa.pub
* Add pub key to Github 
> login GitHub -> Account setting -> SSH Keys -> Add -> paste id_rsa.pub

##### Add remote repository
> GitHub -> Create new repo
> as GitHub prumpt, entry command in cmd
>> git remote add origin git@github.com:<GithubAccountName>/<repoName>.git
>>> origin is default remote repo name of git
> push local repo to remote repo
>> git push -u origin master
>>> -u means git will relate both local and remote master branch together
> any other modifications later
>> git push origin master

##### Clone from remote repository
> git clone git@github.com:<username>/<repoName>.git
<>

## Branch management 分支管理
##### Basic
**with command: git branch**
create & switch
> git branch --> display all branches, * means current branch
> git branch <branchName> --> create
> git checkout <branchName> --> switch
> git checkout -b dev --> create and switch
>> = git branch dev + git checkout dev

merge 分支合并
> git checkout master
> git merge branch1

delete
> git branch -d dev

##### Branch conflict 解决冲突
手动修改冲突内容

##### Branch management strategy 分支管理策略

*Fast-forward* may loss branch information

*TODO*