Title: Editing Huge Amounts of Files Easily
Tags: shell, sed, find
Category: programming

Where I [work](http://www.ign.com), we have tons of static html files
that are published using our custom built Content Management System.
Sometimes, we have to change a single line on every single page. For
example, the latest case involved a change involving the size of ads
that were on the pages. Rather than use publishing and database
resources just to make this relatively simple change, I use the power of
the shell. Specifically, I use
[find](http://linuxcommand.org/man_pages/find1.html),
[sed](http://www.grymoire.com/Unix/Sed.html) and a shell script
that I wrote. It's based on a shell script in the [Unix Power
Tools](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http%3A%2F%2Fwww.amazon.com%2FPower-Tools-Third-Shelley-Powers%2Fdp%2F0596003307%3Fie%3DUTF8%26s%3Dbooks%26qid%3D1191730398%26sr%3D8-1&tag=slackorama-20&linkCode=ur2&camp=1789&creative=9325)
book.

First off, we need to find all the files. I usually accomplish this with
something simple like

    :::console
    $ find /www -type f -name "*.html" -print

This simply finds that end with .html in the /www directory. You can do
more complex things with `find` like find all files modified in the last
2 days by Frank if you needed to change files like that.

The results of this will be passed off to a file named `replace.sh`
located in my `~/bin` directory. `replace.sh` is reproduced here:

    ::bash
    #!/bin/sh
    temp=/tmp/replace$$
    echo -n "editing $1: "
    if test "$1" = sedscr; then
        echo -n "Not editing sedscript!"
    elif test -s $1; then
             sed -f sedscr $1 > $temp
        if test -s "$temp"; then
            if cmp -s "$1" $temp; then
                echo -n "FILE NOT CHANGED: "
            else
                # save original, just in case
                # mv $1 $1.bak
                cp $temp "$1"
            fi
            echo -n "done"
        else
            echo -n "Sed produced an empty file \
    - check your sedscript".
        fi
    else
        echo -n "ORIGINAL FILE IS EMPTY"
    fi
    rm -f $temp
    echo

So, the command we would run would now look like this:

    :::console
    $ find /www -type f \
          -name "*.html" \
          -exec ~/bin/replace.sh {} \;

This does the same as above but passes each file found by the `find`
command above to the `~/bin/replace.sh` script.

You'll notice that the `replace.sh` file calls `sed` using a file named
`sedscr.` The next step is creating the `sedscr` file.

The `sedscr` files simple contains `sed` commands. It must exist in the
same directory that you call the `find` command above from. Here's a
sample `sedscr` that just does a simple replace.

    :::perl
    s/BigHonkingAd/NiceSmallAd/

You can enter in as many complex [sed commands](http://main.rtfiber.com.tw/~changyj/sed/) as you want. It's
`sed` so the power is there!

This simply replaces all instances of BigHonkingAd with NiceSmallAd in
each of your files found by the `find` command. The nice thing about the
`replace.sh` script is that it will not edit the file if the contents of
your `sedscr` don't produce an altered file. Also, if you want the
`replace.sh` to make a backup of your original file, just uncomment the
`mv` line.

Using this methodology, I'm able to edit about 5000 files a minute. It
could probably be faster if I used
[xargs](http://unixhelp.ed.ac.uk/CGI/man-cgi?xargs) and the output of
`replace.sh` is a little verbose but this solution has worked for me for
years and if it ain't broke, why fix it?
