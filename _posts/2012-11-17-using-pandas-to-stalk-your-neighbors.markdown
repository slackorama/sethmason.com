---
title: Using Pandas to stalk your neighbors
layout: post
tags:
 - python
 - pandas
---
I picked up the book [Python for Data Analysis][pfda] as I've been seeing it
mentioned in quite a few places. And so far, it's great. A very good high
level overview of using [Pandas][pandas]. No, not the cute kind of pandas. I'm
talking about the Python library for data analysis. Derp.

Anyhow, I decided to dive in and see what I could find out about my neighbors.
Chapter 9 of [the book][pfda] goes into analyzing the
[2012 Federal Election Commission Database][fec] so I loaded it up:

{%highlight pycon %}
>>> import pandas as pd
>>> fec = pd.read_csv('P00000001-ALL.csv')
{% endhighlight %}

Looking into the data, there is some garbage rows. I grabbed all the Culver
City zip codes (well, the zip codes I care about) at least:

{% highlight pycon %}
>>> zips = fec.contbr_zip.unique()
>>> mask = np.array([str(x).startswith('90232') for x in zips])
>>> fec[fec.contbr_zip.isin(zips[mask])].contbr_city.value_counts()
CULVER CITY     241
CUILVER CITY      2
SANTA MONICA      1
{% endhighlight %}

I don't know if these come from bad data from the contributor or from the FEC so I'm just
going to include everything based on zip code.

{% highlight pycon %}
>>> culver = fec[fec.contbr_zip.isin(zips[mask])]
>>> culver.contb_receipt_amt.sum()
58341.0
{% endhighlight %}

Fifty-eight grand! Nice going Culver City!

Now let's see who got the money:

{% highlight pycon %}
>>> culver.pivot_table('contb_receipt_amt', rows='cand_nm', aggfunc=sum)
cand_nm
Huntsman, Jon                      4500
Obama, Barack                     50381
Paul, Ron                           500
Roemer, Charles E. 'Buddy' III      110
Romney, Mitt                       2850
{% endhighlight %}

That's kind of interesting...Huntsman got more money from the 90232 than
Romney.

Now, let's check out the occupations that contributed the most:

{% highlight pycon %}
>>> culver.pivot_table('contb_receipt_amt', rows='contbr_occupation',
... aggfunc=sum).order(ascending=False).head(10)
contbr_occupation
RETIRED                               7272.0
ACCOUNT MANAGER                       5000.0
VICE PRESIDENT, INTERNET MARKETING    4000.0
PROFESSOR                             2800.5
PRESIDENT & C.E.O.                    2500.0
GALLERY OWNER                         2500.0
BOOKKEEPER                            2500.0
HOMEMAKER                             1971.0
INTERIOR DESIGNER                     1500.0
WRITER                                1410.0
{% endhighlight %}


Retirees going large.  That's kind of interesting. Let's look at that.

{% highlight pycon %}
>>> culver[culver.contbr_occupation == 'RETIRED'].pivot_table(
... 'contb_receipt_amt', rows='cand_nm', aggfunc=sum)
cand_nm
Obama, Barack                     7162
Roemer, Charles E. 'Buddy' III      10
Romney, Mitt                       100
{% endhighlight %}

Maybe I misunderstand our local retirees (at least the ones I've met) but this was
surprising to me. I really expected Romney to come out on top.

I think that's enough peeking into my neighbors contributions habits for one
night. I have to say [Pandas][pandas] makes this sort of thing really easy.
I've only scratched the surface here. There's lots more that one can do
(mathematically speaking) with Panads. [Python for Data Analysis][pfda] gives
you a really good introduction to Pandas and then [the webiste][pandas] fills
in the gaps.

[Python for Data Analysis][pfda] and Panads get two thumbs up from me. Thanks
to [O'Reilly][ora] and [Wes McKinney][wesm].

   [pfda]:  http://www.amazon.com/gp/product/1449319793/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1449319793&linkCode=as2&tag=slackorama-20
   [pandas]:  http://pandas.pydata.org
   [fec]:  http://www.fec.gov/disclosurep/PDownload.do
   [ora]: http://oreilly.com/
   [wesm]: http://blog.wesmckinney.com/
