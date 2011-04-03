---
title: Toggler in Ext JS
layout: post
tags:
- javascript
- extjs
---
Since it has been awhile since I last posted and we started using
[Ext JS](http://www.sencha.com/products/extjs/) at
[work](http://www.cheetahmail.com), I thought I'd post a little snippet
JavaScript for setting up a link that toggles something. 


{% highlight javascript %}
// create a toggler link...is there a better way?
var toggler = new Ext.BoxComponent({
    autoEl: {
        tag: 'a',
        href: '#',
        html: 'All'
    },
    listeners: {
        'render': function(comp) {
            var el = comp.getEl();
            el.on({
                'click': {
                    scope: comp,
                    fn: function(event, element) {
                        event.stopEvent();
                        var text = this.getEl().dom.innerHTML;
                        text = text.toggle('All', 'None');
                        this.update(text);
                        // do your toggling here
                    }
                }
            });
        }
    }
});
{% endhighlight %}

Because it's an instance of
[Ext.Component](http://dev.sencha.com/deploy/dev/docs/?class=Ext.Component) it
can easily be added to a
[Ext.Container](http://dev.sencha.com/deploy/dev/docs/?class=Ext.Component) so
it's a tad more reusable than a straight up select.  At least I think so.

Questions and comments welcome.
