# What I Did

Here's what I did to get this site off the ground after moving machines:

``` shell
uv venv .venv
source .venv/bin/activate
uv pip install -r ./requirements.txt
```

Then to preview the site I ran:

``` shell
uv run pelican -r -l
```

Then to publish it I ran:

``` shell
uv run pelican -s pelicanconf.py
rsync -avz --delete ./output/ slackorama:/home/slackorama/sethmason.com/
```

I guess I can kill the fabfile.py here. It's probably overkill.
