Title: "HOWTO: Invoke a shell script on a file on save with emacs"
Tags: emacs

At my [current job](http://www.cheetahmail.com), we use a lot of
[Template Toolkit](http://www.template-toolkit.org). Due to some design
decisions (that I consider a tad strange), we have to run a shell script
on the template files (e.g. files that end with “.tt”) after they are
saved in order for them to be displayed on the dev site.

Since I started using emacs about two months ago, I’ve learned quite a
bit. A new thing on the learning heap is the
[after-save-hook.](http://www.gnu.org/software/emacs/elisp/html_node/Saving-Buffers.html)
Emacs to the rescue yet again.

Here’s a emacs lisp function I wrote to automate the execution of the
script when a template file is saved:

    :::scheme
    (defun ssm-cheetah-after-save-hook ()
      "After saving a tt file, run the language_update file"
      (if buffer-file-name
          (progn
            (setq is-tt-file (numberp (string-match "\.tt$" buffer-file-name)))
            (if is-tt-file
                (progn
                  (setq cmd (concat (getenv "B") "/bin/YOURSCRIPTHERE --template="))
                  (shell-command (concat cmd buffer-file-name))
                  (message "Updated template with %s" buffer-file-name))))))
    (add-hook 'after-save-hook 'ssm-cheetah-after-save-hook)

What it does, is first defines a function that checks to see if we have
a file name, (which should probably always be true since we are saving
now that I look at it). If we do, check to see if the name ends with
“.tt.” If it does, pass the name of the file to the shell script and
output a message to the user saying the template was updated. Finally,
the function is added to the after save hook.
