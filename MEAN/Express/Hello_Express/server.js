var express = require("express");

var session = require('express-session');
// original code:
var app = express();
// more new code:
app.use(session({secret: 'codingdojorocks'}));
app.use(express.static(__dirname + "/static"));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));

var count = 0;

app.get('/', function(request, response){
  count += 1;
  var context = { count };
  response.render('index', {title: "my Express project"});
})

app.post("/users", function (request, response){
    // var users_array = [
    //     {name: "Michael", email: "michael@codingdojo.com"},
    //     {name: "Jay", email: "jay@codingdojo.com"},
    //     {name: "Brendan", email: "brendan@codingdojo.com"},
    //     {name: "Andrew", email: "andrew@codingdojo.com"}
    // ];
    console.log("POST DATA \n\n", request.body)
    //code to add user to db goes here!
    // redirect the user back to the root route.
    response.redirect('/')
    // response.render('users', {users: users_array});
})
app.get("/users/:id", function (req, res){
    console.log("The user id requested is:", req.params.id);
    // just to illustrate that req.params is usable here:
    res.send("You requested the user with id: " + req.params.id);
    // code to get user from db goes here, etc...
});


app.listen(8000, function(){
  console.log("listening on port 8000");
})
