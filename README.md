# Pull Request Help: #

20240609: based on updating `samd` to allow new functions
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
    * Line3.  Description, multiple lines, markdown, <= 74 char/line
    save and exit editor
6.  Check:
    `$ git log --show-signature -l`
    will show commit message
7.  `$ git push` 
8.  From github, my fork - create pull request
9.  If changes to commit are needed: (Thanks RHH, yet again)
    1.  `$ git commit --amend`
    this brings up editor to modify commit message
    save and exit editor
    2.  `$ git push -f`
    probably more sophisticated steps here!
    The pull request will be automatically updated
    
