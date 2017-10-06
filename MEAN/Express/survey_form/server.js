var express = require("express");
var path = require("path");
var session = require('express-session');
var app = express();
app.use(session({secret: 'no one cares'}));
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
app.get('/', function(req, res) {
  res.render("index");
});

app.post('/register', function(req, res) {
 console.log("POST DATA", req.body);
 req.session.name = req.body.name;
 req.session.location = req.body.location;
 req.session.stack = req.body.stack;
 req.session.comment = req.body.comment;
 res.redirect('/result');
});

app.get('/result', function(req, res){
  context = {
    name : req.session.name,
    location : req.session.location,
    stack : req.session.stack,
    comment : req.session.comment,
  }
  res.render("result", context);
});

app.post('/redirect', function(req, res) {
  console.log("redirect to prev page")
  res.redirect('/');
});
var server = app.listen(8000, function() {
  console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);

io.sockets.on('connection', function(socket) {
  console.log("Client/socket is connected!");
  console.log("Client/socket id is", socket.id);
  socket.on( "submit_name", function (data){
    var random_number = Math.floor(Math.random() * 1000) + 1;
    console.log( data );
    console.log( random_number )
    socket.emit('server_response', {response: data, number: random_number});
      // socket.emit('random_number', {response: });
  });
});
