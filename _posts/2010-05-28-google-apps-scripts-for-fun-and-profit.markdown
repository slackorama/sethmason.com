---
title: Google Apps Script For Fun and Profit
layout: post
tags:
- google
- scripts
- javascript
---

OK, so I have to admit that I have a mancrush on [Google Apps
Script][script].  It's a nice little tool that allows you to do a whole
variety of things on a bunch of Google Products.  For instance:

<blockquote>
With scripts, you can:<br />
* Create your own custom spreadsheet functions<br />
* Automate repetitive tasks (e.g. process responses to Google Docs forms)</br />
* Link multiple Google products together (e.g. send emails or schedule<br />
* Calendar events from a list of addresses in a Spreadsheet)<br />
* Customize existing Google products (e.g. add custom buttons or menus to run
* your own scripts)<br />
</blockquote>

Not only is the tool itself very nice (a slick in-browser editor with syntax
highlighting and context sensitive prompts), the [tutorials][tut] are as well.
In a little under 15 minutes while reading the tutorial I was able to write a
script that emails you the next 10 days events from any calendar.  It uses
JavaScript so if you are familiar with that, then you could probably even do
it quicker than me and my old brain.

A pet peeve that I have is that the daily email I get from Google Calendar
doesn't include my contact's birthdays.  Even if it did, it'd only be for that
day which would be too late for me to drop a card in the mail. And even if did
that, it wouldn't send the email to my wife.  Thus, the following script was
born.

{% highlight javascript %}
// how many days in advance
var INTERVAL = 10;

// the calendar to grab
var CALENDAR = "Contacts' birthdays and events";

// who to send it to
var EMAIL_TO = "email1@somewhere.com,email2@somewhere.com";

//  the subject to use
var SUBJECT = "Birthdays for Seth next " + INTERVAL + " days "

function onOpen() {
  var submenu = [{ name:"Send Birthday List",
                   functionName:"sendBirthdayList"
                 }];
  SpreadsheetApp.getActiveSpreadsheet().addMenu('Birthdays', submenu);  
}

function sendBirthdayList() {
  // Get the event template string from the spreadsheet
  var emailTemplate = SpreadsheetApp
        .getActiveSheet().getRange("b2").getValue();
  var eventTemplate = SpreadsheetApp
        .getActiveSheet().getRange("b3").getValue();
  // Get the next INTERVAL days
  var start = new Date();
  var end = new Date(start.getTime() + 1000*60*60*24*10);
 
  var cal = CalendarApp.openByName(CALENDAR);
  var events = cal.getEvents(start, end);
    
  // Add each event to the email
  var eventLines = "";
  
  for (var e in events) {
    var event = events[e];
    eventLines += eventTemplate
      .replace("<TITLE>", event.getTitle())
      .replace("<DAY>", event.getEndTime().toLocaleDateString())
      .replace("'s birthday","");
            
  }
  var email = emailTemplate.replace("<EVENTS>", eventLines);
  MailApp.sendEmail(EMAIL_TO,
                    SUBJECT + now.toLocaleDateString(), email);
}


{% endhighlight %}

Lo!  Better living through technology.

Right now, I have the template for the email stored in two cells in a
spreadsheet and other configuration info at the top of the script.  Those
could probably go in cell data too, just so it'd be easier to share this
script.  But it should give you an idea of lovely it is touse [Google Apps Script][script].

Using the triggers that are built-in (Triggers &lt; Current script
triggers...), I have it scheduled to email us every 3 days at midnight.  So,
hopefully, I won't be missing any birthdays.

 [script]: http://www.google.com/google-d-s/scripts/scripts.html
 [tut]: http://www.google.com/google-d-s/scripts/articles.html
