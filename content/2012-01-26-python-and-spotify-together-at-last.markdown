Title: Python and Spotify Together At Last
Tags: python, spotify
Category: music

Here's a simple script to show the currently playing song in Spotify. All you
have to do is put it on your `$PATH` and run:

    :::console
    > nowplaying
    The Unsinkable Fats Domino by Guided By Voices

While this is handy in and of itself (to some people), if you are running
[GNU Screen](http://www.gnu.org/software/screen/), you can have it output the
currently playing song in your statusline. Just add the following to your `.screenrc`:

    :::console
    backtick 101 5 5 /home/YOURNAME/bin/nowplaying
    hardstatus string  '%101`'

If you already have a `hardstatus` (or `caption`) line, you'll just need to
add `%101` in there somewhere. Then, you'll have the currently playing song
easily available.

For info about what the above does, see the [GNU Screen manual about backtick](http://www.gnu.org/software/screen/manual/html_node/Backtick.html).

Here's the entire script:

    :::python
    #!/usr/bin/env python
    """Spit out the currently playing song."""
    import dbus
    import sys

    try:
        bus = dbus.Bus(dbus.Bus.TYPE_SESSION)
        spotify = bus.get_object('com.spotify.qt','/')
        info = spotify.GetMetadata()
    except dbus.exceptions.DBusException:
        print('Spotify is not running')
        sys.exit(1)

    track = {}
    trackMap = { 'artist'    : 'xesam:artist',
                 'album'     : 'xesam:album',
                 'title'     : 'xesam:title'
                 }

    for key, value in trackMap.items():
        if not value in info:
            continue
        piece = info[value]
        if isinstance(piece, list):
            piece = ', '.join(piece)

        track[key] = piece.encode('utf-8')

    if track.has_key('title') and track.has_key('artist'):
        print('%s by %s' % (track['title'], track['artist']))
    else:
        print('No song playing')


If you want Spotify to use the built-in notifier in Ubuntu, then by all means
check out [Spotify-notify](http://code.google.com/p/spotify-notify/). It also
adds support for media keys.
