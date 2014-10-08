Title: .bashrc Fun With Subversion
Tags: subversion, bash
Category: shell

Do you use Subversion a lot from the command line in bash? Then this tip
is for you.

Add the following to your .bashrc

    :::bash
    # svn completion
    _svn ()
    {
        local cur prev
        COMPREPLY=()
        cur=${COMP_WORDS[COMP_CWORD]}
        prev=${COMP_WORDS[COMP_CWORD-1]}
        if [ $COMP_CWORD -eq 1 ] || [ "${prev:0:1}" = "-" ]; then
            COMPREPLY=( $( compgen -W 'add blame cat checkout cleanup \
            commit copy delete diff export help import info list lock \
            log merge mkdir move propdel propedit propget proplist \
            propset resolved revert status switch unlock update' $cur ))
        else
            COMPREPLY=( $( compgen -f $cur ))
        fi
        return 0
    }
    ccomplete -F _svn -o default -X '@(*/.svn|.svn)' svn

Save your .bashrc, source it (using `source .bashrc`) and now Subversion
commands will complete. For example, enter `svn upd` press the Tab key
and you'll get `svn update`.

Think of all the keystrokes you'll be saving.

**Update:** I just found Subversion's own [bash completion
script](http://svn.collab.net/repos/svn/trunk/tools/client-side/bash_completion)
which has a ton more options. Mine is easier to maintain. :)
