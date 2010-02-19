---
title: A Better Bugzilla2 
layout: post
tags:
- bugzilla
- greasemonkey
---

For a variety of reasons, I'm still using version 2 of
[Bugzilla](http://www.bugzilla.org) at work even though it's considered "dead"
by Bugzilla.  And the interface looks like it's been dead awhile.

But, thanks to
[Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/748) I'm not
stuck with the interface.  Inspired by
[Jesse Ruderman's TidyBug](http://www.squarefree.com/2009/02/26/tidybug/) I
made my own Greasemonkey script which I'm calling [TidyBz2](/userscripts/tidybz2.user.js).

Here's the before shot:

<figure>
<img src="/images/20100218_tidybz2-pre.png" width="540" height="330"
border="0"/>
</figure>

Here's the after shot:

<figure>
<img src="/images/20100218_tidybz2-post.png" width="540" height="310"
border="0"/>
</figure>

It hides the huge header, makes the title of the issue much more prominent and
fixes some other formatting nits I disliked.  Information that I think is more
important is moved up to the top as well.  But there are also perks you can't
see.  You can use the keyboard to do pretty much anything you need to: comment,
resolve, browse the URL, search, navigate between comments a la gmail, etc.
Once you have it installed, just press <kbd>?</kbd> to see all the keyboard shortcuts.

It's up on [GitHub](http://github.com/slackorama/tidybz2) so feel free to fork
it and make any modifications you'd like to see.


