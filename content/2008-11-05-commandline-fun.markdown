Title: Commandline Fun
Tags: curl, twitter, tip
Category: shell


Insprired by [an article on
ibm.com](http://www.ibm.com/developerworks/linux/library/l-friendfeed/?S_TACT=105AGX01&S_CMP=HP)
about using [twitter](http://www.twitter.com) from the command line, I
wrote up a simple little script to get your friends updates.

Here it is:

    :::console
    $ curl -s -u username:password \
    http://twitter.com/statuses/friends_timeline.xml |
    awk '/<text/ {
      gsub(/<\/*text>/,"");
      text = $0;
    }
    /screen_name/ {
      gsub(/ *<\/*screen_name>/,"");
      print $0;
      print text;
    }'

All it does it is use [cURL](http://curl.haxx.se/) to grab the timeline
from twitter. Then it passes it through
[awk](http://en.wikipedia.org/wiki/Awk) to extract the name and text
from your buddies. Simple and silly, yes?
