Hey wasn't exactly sure what you guys wanted, and if I can use Jquery jqueryA.html provides the solution (it will keep proption you for keys it will add)
And if JQuery is not allowed, jsA.js has a pue java script solution returned simple as a string. to run
open node,
a = require("./jsA")
there will be two exported funtions
a.allContentKeys
and
a.addContentKey

a.allContentKeys() will return a string nesting of all the keys you provided

a.addContentKey(key) will return a nesting of the key your provided and build with every future call with different keys

enjoy!
-Konrad Dudziak
