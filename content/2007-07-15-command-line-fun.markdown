Title: Command Line Fun
Tags: bash, configuration

If you use the command line in bash, you should check out the CDPATH
environment variable. It’ll make your life tons easier.

From the [bash man
pages](http://www.linuxcommand.org/man_pages/bash1.html), CDPATH is
defined as:

> The search path for the cd command. This is a colon-separated list of
> directories in which the shell looks for destination directories
> specified by the cd command. A sample value is “.:\~:/usr”.

In my .bashrc, I’ve got the following defined:\
` CDPATH='.:..:../..:~/projects'`

This allows me to just type `cd app` when I want to go to
`~/projects/app`. Another great part of it is that if I am in `/var/log`
and want to go to `/var/www` I only need to type `cd www`. The `..` in
the CDPATH takes care of finding it.

The important part of it is the first one. The single period allows for
`cd` to work normally and find directories in your current directory.
