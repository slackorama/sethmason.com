Title: Org Exporting and Emailing
Tags: emacs, org
Category: editor

I use org-mode. I use Emacs. I send email using Emacs.

Thus, I *really* liked John Kitchin's post about
[sending email with org](http://kitchingroup.cheme.cmu.edu/blog/2014/06/08/Better-integration-of-org-mode-and-email/).
It was almost perfect (to me). The only thing it didn't do was format the
content before exporting. It just sent it out as plain org.

Thanks to his hard work, I just had to add a few bits to come up with this.
Now I can get the cool line blocks around my code and execute the org-babel blocks
in my headings before they get sent out. This is very helpful when sending out
snippets of code and random command line effluvia.

    :::emacs-lisp
    (defun email-heading-after-export (backend &optional plist)
      "Send the current org-mode heading as the body of an email, after converting
    it to the given backend.
    "
      (interactive)
      (setq *email-heading-point* (set-marker (make-marker) (point)))
      (save-excursion
        (org-mark-subtree)
        (let ((TO (org-entry-get (point) "TO" t))
              (SUBJECT (nth 4 (org-heading-components)))
              (continue nil)
    	  (switch-function nil)
    	  (yank-action nil)
    	  (send-actions '((email-send-action . nil)))
    	  (return-action '(email-heading-return))
              (plist `(:with-toc nil ,@plist)))
          ;; we do not  want the mark to interfere with export
          (deactivate-mark)
          (message (format "%s" plist))
          (org-export-to-buffer backend "*org-to-email*" nil t nil t plist
                                nil)
          (switch-to-buffer "*org-to-email*")
          (let ((content (buffer-substring (point-min) (point-max))))
            (compose-mail TO SUBJECT nil continue switch-function yank-action
                          send-actions return-action)
            (message-goto-body)
            (insert content)
            (if TO
                (message-goto-body)
              (message-goto-to))))))


Now, I can email a heading as ASCII

    :::emacs-lisp
    (defun email-heading-as-ascii ()
      (interactive)
      (email-heading-after-export 'ascii))

Or UTF-8:

    :::emacs-lisp
    (defun email-heading-as-utf8 ()
      (interactive)
      (message "wtf")
      (email-heading-after-export 'ascii '(:ascii-charset utf-8)))

Even Markdown:

    :::emacs-lisp
    (defun email-heading-as-markdown ()
      (interactive)
      (email-heading-after-export 'md))

You could even send email as HTML but there's no way I'm giving out the tips
on how to do that.

Let me know if you have any questions or comments about the above. And thanks
to John Kitchin! This code uses the same
[License](https://creativecommons.org/licenses/by-sa/4.0/deed.en_US).
