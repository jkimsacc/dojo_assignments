var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

var count = 0;

app.get('/', function(req, res) {
  count += 1;
  context = { count };
  res.render("index", {count:count});
})
// post route for adding a user
app.post('/ninja1', function(req, res) {
  console.log("POST DATA", req.body);
  count += 1;
  res.redirect('/');
})
app.post('/ninja2', function(req, res) {
  console.log("POST DATA", req.body);
  count = 0;
  res.redirect('/');
})
// tell the express app to listen on port 8000
app.listen(8000, function() {
 console.log("listening on port 8000");
});
