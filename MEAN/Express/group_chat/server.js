// require express
var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

var users = [];
var messages = [];
var is_user = function(user){
  for (let i = 0; i < users.length; i++){
    if (user == users[i]){
      return true;
    }
  }
  return false;
}

app.get('/', function(req, res) {
  res.render("index");
})

var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});

var io = require('socket.io').listen(server);

io.sockets.on('connection', function(socket){
  console.log("Client/socket is connected!");
  console.log("Client/socket id is: ", socket.id);
  socket.on('page_load', function(data){
    if(is_user(data.user) === true){
      socket.emit("existing_user", {error: "User already Exists"})
    }
    else {
      users.push(data.user);
      socket.broadcast.emit('load_messages', {current_user: data.user, messages: messages});
      io.emit('user_enter', {current_user: data.user});
    }
  })
  socket.on("new_message", function (data){
    messages.push({name: data.user, message: data.message});
    io.emit("post_new_message", {new_message: data.message, user: data.user})

  });
})
