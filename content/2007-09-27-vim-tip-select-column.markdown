Title: "Vim Tip: Select Column"
Tags: vim

<img src="http://sethmason.com/images/11.png" align="left"/> How many times have you wanted
to replace a column of text with something. With [vim](http://vim.org)
it’s easy. Just use `CTRL-V` to select a column using a visual block.

Once it’s selected, you can do a search and replace, yank, cut and other
actions. For example, here’s the keystrokes to change a column.

-   Put cursor and beginning of text to select
-   Press `CTRL-V` to begin select of the column
-   When you reach the end of your select, type '`c`'
-   Type the new text. Note that this will only replace the first
    instance.
-   Now hit `<ESC><ESC>`. All the text has been changed!

The same thing works with plain old '`v`' (select character by
character) and `SHIFT-V` (select by line).

Happy vimming!
