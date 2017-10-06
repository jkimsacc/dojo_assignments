var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
  Message.find({}, false, true).populate('_comments').exec(function(err, messages){
    res.render('index', {messages: messages});
  });
});
app.post('/message', function(req,res){
    var newMessage = new Message({name: req.body.name, message: req.body.message});
    newMessage.save(function(err){
        if(err){
            console.log(err);
            res.render('index', {errors: newMessage.errors});
        } else {
            console.log("success");
            res.redirect('/');
        }
    })
})

app.post('/comment/:id', function (req, res) {
  var message_id = req.params.id;
  Message.findOne({_id: message_id}, function(err, message){
    var newComment = new Comment({name: req.body.name, message: req.body.message});
    newComment._message = message_id;
    Message.update({_id: message._id}, {$push: {"_comments": newComment}}, function(err){

    });
    newComment.save(function(err){
      if(err) {
        console.log(err);
        res.render('index', {errors: newComment.errors});
      } else {
        console.log("comment added");
        res.redirect('/');
      }
    });
  });
});

app.listen(8000, function() {
  console.log("listening on port 8000");
});

mongoose.connect('mongodb://localhost/message_board', {
    useMongoClient: true
});

var Schema = mongoose.Schema;
var MessageSchema = new mongoose.Schema({
  name: String,
  message: String,
  _comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
});

MessageSchema.path('name').required(true, 'Name cannot be blank');
MessageSchema.path('message').required(true, 'Message cannot be blank');
mongoose.model("Message", MessageSchema);

var Message = mongoose.model('Message');
var CommentSchema = new mongoose.Schema({
  name: String,
  message: String,
  _message: { type: Schema.Types.ObjectId, ref:'Message'},
});

CommentSchema.path('name').required(true, 'Name cannot be black');
CommentSchema.path('message').required(true, 'Message cannot be black');
mongoose.model("Comment", CommentSchema);
var Comment = mongoose.model('Comment');
