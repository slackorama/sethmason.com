Title: Machine specific startup files in BASH
Tags: bash, configuration

Here’s a helpful tip if you use a couple of different machines and need
specific things set up on a specific machine.

Just add the following to your
[.bashrc](http://en.wikipedia.org/wiki/Bash)

    :::bash
    ## Read Generic RC                                                                            
    for rcfile in "$HOME/.shell/"*.rc;
    do                        
        if [ -r "$rcfile" ]; 
    done

Thus, common things are stored in your .bashrc (like aliases, functions,
etc.) and things you want on a specific machine are in their own
directory.

Then, just put whatever machine specific files you want/need in
\~/.shell and name them with .rc. For instance, I have
\~/.shell/smurf.rc that sets up some smurf information.

    :::console
    > export FAVORITE_SMURF="Poppa Smurf"
    > export SMURF_LOVER=$HOME/bin/blue_love  

That way, if I ever need something that’s specific to a machine, I just
drop it in my .shell directory and away we go.
