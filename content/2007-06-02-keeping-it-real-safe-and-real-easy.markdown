Title: Keeping It Real Safe And Real Easy
Tags: subversion, configuration, vim

![Subversion logo]({filename}/images/7.png)

OK, I've fallen in love with putting my home directory in
[Subversion](http://subversion.tigris.org/ "A version control system to rival CVS").
The benefits are enormous. They include (but are not limited to):

-   ease of setting up environment on new system
-   backup
-   ability to go “back in time” using Subversion
    [tags](http://svnbook.red-bean.com/nightly/en/svn.branchmerge.tags.html "Tags rule")

Mind you I don't put everything in there, just the important stuff like
my shell configuration files and my
[vim](http://www.vim.org "The one true editor") configuration files.
Other important files (like pictures and music I spent ages ripping) are
backed up in other ways.

Here's what I currently have saved in svn:

    :::console
    $ svn ls http://my.svn.server/svn/home-dir/trunk/
    .Xdefaults
    .antrc
    .bash_profile
    .bashrc
    .dircolors
    .inputrc
    .irbrc
    bin/
    vim_local/

So now when I'm on a system, I'll have the same look and feel and same
functionality as the utilities I use will be available in my `~/bin`
directory.

For those astute readers, you'll notice that I don't have a .vimrc file
in there. That's because I'm using an excellent tip from Amir
Salihefendic\
about [taming your vim config](http://amix.dk/blog/viewEntry/162).
Basically on each system I have a specialized but simple .vimrc that
sources the vim\_local for what it needs.

I've found this setup works great on the many different systems I use
throughout a given week (e.g. Windows, Mac and Linux). And I'm safe in
the knowledge that my configuration files won't disappear should my
machines suddenly implode.
