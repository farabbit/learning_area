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

### How to use

* Create SSH key

> ssh-keygen -t rsa -c "email@example.com" -> write this in shell or Git bash to create a SSH key
>> .ssh dir: id_rsa, id_rsa.pub

* Add pub key to Github 

> login GitHub -> Account setting -> SSH Keys -> Add -> paste id_rsa.pub

### Add remote repository

> GitHub -> Create new repo
> as GitHub prumpt, entry command in cmd
>> git remote add origin git@github.com:<GithubAccountName>/<repoName>.git
>>> origin is default remote repo name of git  

> push local repo to remote repo
>> git push -u origin master
>>> -u means git will relate both local and remote master branch together  

> any other modifications later
>> git push origin master

### Clone from remote repository

> git clone git@github.com:<username>/<repoName>.git
<>

## Branch management 分支管理

### Basic

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

禁用Fast forward时，git会在merge时生成新的commit
--no-ff

```shell
git checkout -b dev
git add readme.txt
git commit -m "add merge"
git checkout master

git merge --no-ff -m "merge with no-ff" dev
```

stragegy
> Master branch should be stable, only use this branch to release new version.  
> work in dev branch, and when 1.0 release, merge dev to master

##### Bug branch
with git stash
> git stash -> save workspace  
> git stash list  
> git stash apply [<stashName>]
>> stash will not be deleted automatically  
>> git stash drop -> drop stash  
> git stash pop 
>> drop stash when recover your workspace

##### Feature branch
add a Feature branch when test your codes
> git branch -d <featureBanchName>
> git branch -D <featureBanchName> -> mandatory drop



# git cheat sheet

## 一、常见命令

### 创建

克隆现有的存储库

 $ git clone ssh://user@domain.com/repo.git
创建新的本地存储库

 $ git init    
### 本地变化
更改工作目录中的文件

 $ git status  
对跟踪文件的更改

 $ git diff    
将所有当前更改添加到下一次提交

 $ git add .   
将< file >中的一些更改添加到下一次提交

  $ git add -p <file>  
提交跟踪文件中的所有本地更改

 $ git commit -a   
提交先前阶段的更改

 $ git commit  
更改最后提交 
不要修改发布的提交！

 $ git commit --amend  
### 提交历史
显示所有提交，从最新开始

 $ git log 
显示特定文件随时间的变化

 $ git log -p <file>   
谁在< file >中更改了内容和时间？

  $ git blame <file>   

### 分支和标签

列出所有现有分支
 $ git branch -av

切换分支
 $ git checkout <branch>  

根据当前的头部创建一个新分支
 $ git branch <new-branch> 

基于远程分支创建新的跟踪分支
$ git checkout --track <remote/bran- ch>

删除本地分支
  $ git branch -d <branch> 

提交标签
  $ git tag <tag-name>

### 更新和发布

列出所有当前配置的远程主机

 $ git remote -v   
显示有关远程

 $ git remote show <remote>    
添加名为< Remote >的新远程存储库

$ git remote add <shortname> <url> 
从< Remote >下载所有更改，但不要集成到Head中

$ git fetch <remote>   
下载更改并直接合并/集成到头中

$ git pull <remote> <branch>   
在远程上发布本地更改

$ git push <remote> <branch>   
删除远程上的分支

$ git branch -dr <remote/branch>   
发布标签

$ git push --tags
1. 合并和重基
将<分支>合并到当前的头部
  $ git merge <branch> 

将当前的头重新定位到<分支> 
不要重新发布已发布的提交！
  $ git rebase <branch>    

中止重基
  $ git rebase --abort 

解决冲突后继续重基
 $ git rebase --continue   

使用配置的合并工具解决冲突
 $ git mergetool   

使用编辑器手动解决冲突，并(在解决后)将文件标
记为“已解决”。
  $ git add <resolved-file>    
  $ git rm <resolved-file> 
7. 撤销
放弃工作目录中的所有本地更改。

$ git reset --hard HEAD    
放弃特定文件中的本地更改。

$ git checkout HEAD <file> 
还原一个提交(通过产生一个新的具有相反更改的提交)

$ git revert <commit>  
将头指针重置为上一次提交 
…并放弃自那以后的所有变化

$ git reset --hard <commit>    
…并将所有更改保留为未分阶段的更改。

$ git reset <commit>   
…并保存未提交的本地更改。

$ git reset --keep <commit>    
## 二、最佳做法
1. 提交相关修改
  提交应该是相关更改的包装。例如，修复两个不同的bug应该产生两个单独的提交。消息使其他开发者更容易理解禅宗。 如果出了什么问题就把它们退回去。

有了诸如分阶段区域和ABI特性这样的工具，只对文件的部分进行分级，Git使创建非常细粒度的提交变得非常容易。

2. 经常提交
  提交经常使您的承诺保持较小，并且再次帮助您仅提交相关的更改。 
  此外，它允许您更频繁地与其他人共享代码。 
这样对每个人来说都比较容易 定期集成更改，避免合并冲突。

  相反，很少有大量的提交，并且很少分享它们，这使得解决冲突变得困难。

3. 不要半途而废
  您应该只在代码完成时提交代码。这并不意味着您必须在提交之前完成一个完整的大型功能。完全相反：分裂

特性的实现分为逻辑块，并记住要尽早提交。

  但是，不要只承诺在一天结束前离开办公室之前就在存储库中有一些东西。如果仅仅因为需要一个干净的工作副本(检查分支)而想提交 在变化，拉等）考虑使用Git的«stash»特征相反。

4. 在提交之前测试代码
  抵制诱惑，去做一些你认为已经完成的事情。彻底测试它，以确保它真的完成了。

  而且没有副作用(据我们所知)。虽然在本地存储库中提交半生不熟的东西只需要您原谅自己，但是在以下情况下进行代码测试就更重要了。 这涉及到推送/与他人共享代码。

5. 编写良好的提交消息
  开始您的消息，以一个简短的总结，您的变化(多达50个字符作为一个Gui-deline)。将它与下面的正文分隔开，方法是包含一个空行。您的消息正文应该提供如以下问题的邮件式解答：

改变的动机是什么？

它与以前的实施方式有何不同？
  使用祈使句、现在时态（省去变化、不改变或改变）与来自Git合并的命令生成的消息一致。

6. 版本控制不是备份系统。
  在远程服务器上备份文件是拥有版本控制系统的一个很好的副作用。但是你不应该像使用备份系统一样使用你的VCS。在执行版本控制时，您将应该注意语义上的（见相关的Chan-Ges）-你不应该只是在文件中填塞。

7. 使用分支
  分支是Git最强大的特性之一，这不是偶然的：快速和容易的分支是第一天的中心要求。分支是帮助你避免混淆不同发展方向的完美工具. 您应该在开发工作流程中广泛使用分支：用于新特性、bug修复、想法……

8. 就工作流达成一致
  git允许您从许多不同的工作流中选择：长时间运行的分支、主题branch、合并或重基、git-flow…。您选择哪一个取决于以下几个因素：你的项目，你的整体开发和部署工作流程，（也许最重要的）是你和你的队友的个人喜好。无论你选择工作，只要确保达成一个共同的工作流程，每个人都遵循这个工作流程。

9. 使用帮助和文档
获取命令行的帮助

  $ git help <command> 

## internal sharing

------------------------

Local repository

remote repository

git config --global(local, system

git cat-file -t
  文件类型
git cat-file -p
  文件内容