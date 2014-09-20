#!/usr/bin/env python

import os
import re

import textile

HEAD_LINE = re.compile(r'^---')
TAG_LINE = re.compile(r'^\s?- (\S+)$')
TITLE_LINE = re.compile(r'title: (.*)$')
BEGIN_HL_LINE = re.compile(r'{%\s?highlight (\S+) %}$')
END_HL_LINE = re.compile(r'{% endhighlight %}')

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OLD = os.path.join(BASE, "sethmason.com", "_posts")
TO = os.path.join(BASE, "new.sethmason.com", "temp")

for post in os.listdir(OLD):
    is_textile = 'textile' in post
    in_highlight = None
    in_head = False
    tags = []
    title = '???'
    body = []
    with open(os.path.join(OLD, post)) as f:
        content = f.readlines()
    print(post)

    for line in content:
        if in_head:
            tag_match = TAG_LINE.match(line)
            if tag_match:
                tags.append(tag_match.group(1))
            title_match = TITLE_LINE.match(line)
            if title_match:
                title = title_match.group(1)
            if HEAD_LINE.match(line):
                in_head = False
            continue

        if HEAD_LINE.match(line):
            in_head = True
            continue

        hl_match = BEGIN_HL_LINE.match(line)
        if hl_match:
            in_highlight = hl_match.group(1)
            if is_textile:
                body.append('bc. ')
            else:
                body.append('    :::{}\n'.format(in_highlight))
            continue

        if in_highlight:
            if END_HL_LINE.match(line):
                in_highlight = None
                continue
            body.append('    {0}'.format(line))
        else:
            body.append(line)

    meta = '{}.meta'.format(post)
    if is_textile:
        meta = meta.replace('.textile','')
        output = '{}.body'.format(post.replace('.textile','.html'))
    else:
        meta = meta.replace('.markdown','')
        output = '{}.body'.format(post)

    with open(os.path.join(TO, meta), 'w') as f:
        f.write('Title: {0}\n'.format(title))
        f.write('Tags: {0}\n'.format(', '.join(tags)))

    with open(os.path.join(TO, output), 'w') as f:
        if is_textile:
            f.writelines(textile.textile(''.join(body)))
        else:
            f.writelines(body)


# then I did:
#   : for i in $(ls temp/*html.body); do md=$(echo $i | sed -e 's/html/markdown/'); pandoc -f html -t markdown -o $md $i; done

# then I did:

#  for i in $(ls temp/*markdown.body); do
#   echo $i
#   out=$(echo $i| sed -e 's/temp\//content\//' -e 's/\.body//');
#   meta=$(echo $i | sed -e 's/\.markdown\.body/.meta/')
#   cat "$meta" > "$out"
#   echo "" >> "$out"
#   cat "$i" >> "$out"
# done

# Still needed to fix some nits....improper syntax highlighting. bad textile code
