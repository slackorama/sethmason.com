Title: Cost of try/catch in JavaScript
Tags: javascript, benchmark

I know that in Java, using a try/catch is fairly expensive vs. a if
check. Since JavaScript has the same syntax for the most part, I wrote
up a simple benchmarking script to test it out. On my box, it outputs:

    if avg: 0.029
    try avg: 1.372

Note, that you'll need [the Firebug plugin](http://ww.getfirebug.com)
for [Firefox](http://www.getfirefox.com) in order to run this.

    :::javascript
    var tryFunc = function () {
      try {
        document.getElementById("fake").innerHTML = "hi there";
      } catch (e) {
        // eat it!
      }
    }

    var ifFunc = function() {
      var el = document.getElementById("fake");
      if (el) {
        el.innerHTML = "hi there";
      }
    };

    function benchmark(name, func) {
      var repeats = 1000;
      var elapsed = 0;
      var startTime =0;
      var endTime = 0;
      for (var i=0; i< repeats; i++) {
        startTime = new Date().getTime();
        func.call();
        endTime = new Date().getTime();
        elapsed += (endTime - startTime);
      }
      console.log(name + " avg: " + (elapsed / repeats ) );
    }

    benchmark( "if", ifFunc );
    benchmark( "try", tryFunc );
