Title: Beautify your JavaScript in Emacs
Tags: javascript, emacs, beautify

I know you'll find this hard to believe dear reader but I'm a big fan of
using Emacs to write  JavaScript. One thing that irked me in the past is
that none of the libraries got the indentation and other formatting how I
wanted. Luckily, I recently stumbled onto
[js-beautify](http://jsbeautifier.org/) (via the most excellent
[jsFiddle](http://jsfiddle.net).

Lo and behold, there is a command line interface to beautifying
JavaScript! Good thing Emacs can call shell commands on text so easily.  Thus,
we have:

    :::scheme
    ;;; js-beautify.el -- beautify some js code

    (defgroup js-beautify nil
      "Use jsbeautify to beautify some js"
      :group 'editing)

    (defcustom js-beautify-args "--jslint-happy --brace-style=end-expand
    --keep-array-indentation"
      "Arguments to pass to jsbeautify script"
      :type '(string)
      :group 'js-beautify)

    (defcustom js-beautify-path "~/projects/js-beautify/python/jsbeautifier.py"
      "Path to jsbeautifier python file"
      :type '(string)
      :group 'js-beautify)

    (defun js-beautify ()
      "Beautify a region of javascript using the code from jsbeautify.org"
      (interactive)
      (let ((orig-point (point)))
        (unless (mark)
          (mark-defun))
        (shell-command-on-region (point)
                                 (mark)
                                 (concat "python "
                                         js-beautify-path
                                         " --stdin "
                                         js-beautify-args)
                                 nil t)
        (goto-char orig-point)))

    (provide 'js-beautify)
    ;;; js-beautify.el ends here


I like it so much I have bound to M-t (for tidy) in a mode hook:

    :::scheme
    (local-set-key "\M-t" 'js-beautify)

If you want to follow any updates, I've put this snippet up as a [Gist on
GitHub](https://gist.github.com/712405) so feel free to clone and send me any
pull requests.
