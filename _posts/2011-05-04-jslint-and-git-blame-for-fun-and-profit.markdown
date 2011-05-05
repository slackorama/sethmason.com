---
title: JSLint and git blame for fun and profit
layout: post
tags:
- git
- jslint
---
For some unknown reason, we have a problem with superfluous trailing commas at
work in our JavaScript. It's probably because we have a bunch of Perl
developers writing JavaScript. Unfortunately, this doesn't play well in a
world with Internet Explorer.

[JSLint](http://www.jslint.com) makes this easy enough to track down. But I
wanted something more. I wanted to know who the culprits were. Thus, I whipped
up this little script that'll take a list of files and tell you who committed
a file with a trailing comma in it. Besides, JSLint, You'll need
[Rhino](https://www.mozilla.org/rhino/) and a script to execute commands
(named runtime.js). I'll try and post that later.

{% highlight javascript %}
// blame_comma.js -- loop through the files passed in and see who has
// commas in them

// find ../htdocs/js/ECM -type f -name "*.js" -print | \
// xargs java -classpath \
//   /usr/share/yuicompressor-2.4.2/lib/rhino-1.6R7.jar \
//   org.mozilla.javascript.tools.shell.Main blame_comma.js

load('fulljslint.js');
load('runtime.js');

(function(args) {
    var bad_files = {};
    for (var i = 0; i < args.length; i++) {
        var file = args[i],
            js = readFile(file);
        var success = JSLINT(js, {
		    browser : true,
            undef   : true,
            newcap  : false,
            indent  : 4,
            predef: ["Ext","ECM","ActiveXObject","window",
                     "TestCase","document","assertTrue","sinon","gt"]
	    });
        if (!success) {
            var errors = JSLINT.errors;
            for (var j=0;j<errors.length;j++) {
                var e = errors[j];
                if (e && e.reason && e.reason.match(/Extra comma/)) {
                    var cmd = 'git blame -L' + e.line + ', ' +
                              e.line + ' -- ' + file;
                    var output = runtime.exec( cmd );
                    if (!bad_files[file]) {
                        bad_files[file] = [];
                    }
                    bad_files[file].push(output);
                }
            }
        }
    }
    for (var key in bad_files) {
        if (bad_files.hasOwnProperty(key)) {
            print("\n" + key);
            var errors = bad_files[key];
            for (var i = 0; i<errors.length;i++) {
                print(errors[i]);
            }
        }
    }
})(arguments)
{% endhighlight %}

Like most of the stuff I seem to do lately, this is available as a
[gist on GitHub](https://gist.github.com/947059). Let me know if you see
anything you like.
