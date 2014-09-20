Title: Debugging Is Sexy Good Times
Tags: Javascript, Firebug, Firefox

I love me some [JSON](http://json.org "JavaScript Object Notation").
The problem with it is that it’s not too human readable when you need to
see what it’s returning. Sure you could litter your code with alerts or
console.debug (if you are using
[Firebug](http://www.getfirebug.com "Awesome JavaScript debugger") and
[Firefox](http://www.getfirefox.com "Awesome web browser") to figure
out what values are you getting back.

But if you’ve got the Firefox/Firebug setup (and why don’t you if you
don’t?) then you can just use the Firebug console to display the JSON
data. Say for instance you have the following data returned from your
service (but imagine it’s a bazillion lines long):

    :::json
    {"SomeObject":{"Attrib1":"foo",
                   "Attrib2":"bar",
                   "SubObject": {"SubAttrib1":"bar"}
                  }
    }

Just wrap that in an `eval` function, plug it into the console and you
get back a nice little tree of your data in the DOM view.

![](http://sethmason.com/images/5.png)

Now isn’t that sexy?
