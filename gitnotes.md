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
    
 ## 20250846: how to split repository
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

## 20251204: show information
```bash
$ git status -uno
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   config.esp32s3.py
	modified:   config.py
	modified:   holiday.py
	modified:   simpfirefly.py
```
+ shows branch/version
+ does not show commit version, 
+ shows differences with version

git log
```bash
$ git log
commit e6357ac6cf7af70acfdaa8b9b137ea1bfeb6c6de (HEAD -> main, origin/main)
Author: Rick Sorensen <rick.sorensen@gmail.com>
Date:   Mon Dec 1 11:40:25 2025 -0600

    README: Add schematic image

commit 03676b99b2ddfad31acf0484bf8cddf42ae4fd11 (tag: neopixel_ldr_v0.87, tag: Display_v1.00)
Author: Rick Sorensen <rick.sorensen@gmail.com>
Date:   Mon Dec 1 10:01:56 2025 -0600

    holiday: 2025 Hanukkah

commit c4de475c72a02ce543fe64e7193f59a8e7a7a924
Author: Rick Sorensen <rick.sorensen@gmail.com>
Date:   Sun Nov 2 10:19:58 2025 -0600

    mqttquick: catch no network exceptions
```

git log
git tag
git show
```bash
$ git show
commit e6357ac6cf7af70acfdaa8b9b137ea1bfeb6c6de (HEAD -> main, origin/main)
Author: Rick Sorensen <rick.sorensen@gmail.com>
Date:   Mon Dec 1 11:40:25 2025 -0600

    README: Add schematic image
```
