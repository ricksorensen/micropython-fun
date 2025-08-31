# Pull Request Help: #

## 20240609: based on updating `samd` to allow new functions ##

1.  From my micropython fork on github, create new branch `samd_func`
    `$ git clone https:\\micropython\ricksorensen rjsfork`
2.  From my clone (rjsfork)
    `$ cd rjsfork;git checkout samd_func`
3.  Modify file(s) ..eg `mcu/samd21/mpconfigmcu.h`
4.  Test
5.  commit and sign changes
    `$ cd rjsfork; git commit -s ports/samd/mcu/samd21/mpconfigmcu.h`
    this brings up editor to add commit message:
    * Line1.  Title <72 char, filename: Title (don't forget space after :)
    * Line2.  Blank
    * Line3 and following.  Description, multiple lines, markdown, <= 74 char/line
    save and exit editor
6.  Check:
    `$ git log --show-signature -l`
    will show commit message
7.  `$ git push` 
8.  From github, my fork - create pull request

## 20250514:

!!! Once pull request is started do not resync that branch !!!

My `pydev` environment has micropython versions of `pre-commit1` and `uncrustify` installed.  Note that `pre-commit` tends to change in place.

Can use `>pre-commit run --file xxx` to check 

9. If changes to commit are needed: (Thanks RHH, yet again)
    1. `$ git commit --amend`
    this brings up editor to modify commit message
    save and exit editor
    2. `$ git push -f`
    probably more sophisticated steps here!
    The pull request will be automatically updated
    
 ##20250846: how to split repository
https://github.com/orgs/community/discussions/167314

``` text
Hi,
I think you can use git filter-repo for your case.
I guess your current structure is similar to this:

/repository
  /project_A
  /project_B
  /project_C
1. Download from the official repo or install with pip install git-filter-repo
2. Add it in your PATH (Accessible in System>About>Advanced system settings>Environment Variables>System variables).
3. Within your monorepo run below for project_A:
   >git clone --no-local --no-hardlinks <path-to-monorepo> project_A-repo
4. Go to the folder
 >  >cd project_A-repo
5. Run this,
   > git filter-repo --subdirectory-filter project_A
6. Repeat the same for all your projects.
7. Go to your GitHub and create new repository for your project.
8. Add it as remote (in this case default is 'main')
   >git remote add origin <new-repository-url>
   >git push -u origin main  oops I did:
      > git pull --rebase <repo url> main   to get new files
      > git push -u origin main 
```
Link: Git Filter  https://github.com/newren/git-filter-repo
