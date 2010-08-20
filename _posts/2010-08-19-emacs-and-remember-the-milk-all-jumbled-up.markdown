---
title: Emacs and Remember The Milk all jumbled up
layout: post
tags:
- emacs
- rtm
- emacs-lisp
---

I'm a huge fan of [Remember The Milk][1] and [GNU Emacs][2].  So much so, that
I've given them both money over the years.   And now I've (kind of) combined
them.  I just pushed [slack-rtm][3] to GitHub.

I've kind of avoided Emacs Lisp, [the 1984 Subaru of Lisp][6].  While I've
done some minor hacking of my .emacs in the two years I've been using Emacs, I
have not really done any serious programming in it.  But with this, I'm hoping
to remedy that a bit.  It's been fine so far, even though the learning curve has
been steep.  I don't think I'll be writing a JavaScript interpreter anytime soon.

Right now, it's pretty simple.  It just creates a buffer and shoves your tasks
into it.  I've only tested it on GNU Emacs 23.1.50.1.  Ultimately, I'd like it
to sync between an [orgmode][4] file and RTM, kind of like what
[Sacha Chua did with org-toodledo.][5]

So, [have at it][3].  Feel free to fork it and send me pull requests.  I'm hoping
to release early (DONE!) and often.

[1]: http://www.rememberthemilk.com
[2]: http://www.gnu.org/software/emacs/
[3]: http://github.com/slackorama/slack-rtm
[4]: http://www.orgmode.org
[5]: http://sachachua.com/blog/2010/05/org-toodledo/
[6]: http://steve-yegge.blogspot.com/2008/11/ejacs-javascript-interpreter-for-emacs.html

