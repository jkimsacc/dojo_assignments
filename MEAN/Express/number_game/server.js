var express = require("express");
var path = require("path");
var session = require('express-session');
var app = express();
app.use(session({secret: 'no one cares'}));var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

var number = Math.floor(Math.random() * 100) + 1;
var attempt = Math.ceil(Math.log2(100));
console.log(attempt);
console.log(number);
app.get('/', function(req, res) {
  context = {
    number,
    attempt,
    last_guess : req.session.last_guess,
    message : req.session.message
  }
  res.render("index", context);
})

app.post('/process', function(req, res) {
  attempt -= 1;
  if (attempt > 0){
    if (number == req.body.guess){
      console.log("correct!");
      req.session.message = "Correct!";
      req.session.last_guess = "";
    }
    else if (number > req.body.guess){
      req.session.message = "Higher!";
      req.session.last_guess = req.body.guess;
    }
    else {
      req.session.message = "Lower!";
      req.session.last_guess = req.body.guess;
    }
  }
  else {
    req.session.message = "Wrong! out of attempts";
    req.session.last_guess = req.body.guess;
  }
  res.redirect('/');
})

app.post('/reset', function(req, res){
  console.log('reset');
  number = Math.floor(Math.random() * 100) + 1;
  attempt = Math.ceil(Math.log2(100));
  req.session.message = "";
  req.session.last_guess = "";
  res.redirect('/');
})
app.listen(8000, function() {
 console.log("listening on port 8000");
});
