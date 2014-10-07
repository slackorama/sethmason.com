Title: Cygwin And SSH Tip
Tags: cygwin, ssh, bash

![cygwin logo]({filename}/images/8.png)

Auto completion for `ssh` under cygwin was driving me nuts. It wasn't
parsing the `~/.ssh/known_hosts` file like it should have and using
those values to auto-complete. Investigating, (by using `ssh -v`) I
found out that my `known_hosts` didn't exist in `${HOME}/.ssh` and `ssh`
was using the one in `C:/Documents and Settings/smason/.ssh`. Uh,
*excuse me*? My `$HOME` is `/home/smason`. I `cd ~` and I'm in
`/home/smason`. Bafflement ensued.

Turns out my `/etc/passwd` was all mucked up. It had my `HOME` directory
set to the one in my `Documents and Settings` directory. I manually
edited my `/etc/passwd` and now `ssh` auto completion works.

Wow, the [second post]({filename}/2007-06-12-bashrc-fun-with-subversion.markdown)
in a row dealing with auto completion. I guess I **really** like
auto-completion. Think of the keystrokes I'm saving you!
