let express = require("express");
let app = express();


app.use(express.static(__dirname + '/public/dist'));

// BodyParser

let bodyParser = require("body-parser");
// app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());


//DB

let mongoose = require("mongoose");
mongoose.connect('mongodb://localhost/dojo_trivia')
mongoose.Promise = global.Primise;

const path = require("path");

var Schema = mongoose.Schema;
var UserSchema = new mongoose.Schema({
   username: String,
   score: Number,
})
// UserSchema.path('username').required(true, 'Username Required to play');
mongoose.model("User", UserSchema);
var User = mongoose.model("User");

var QuestionSchema = new mongoose.Schema({
   question: String,
   answer: String,
   fake_answer1: String,
   fake_answer2: String,
});
// QuestionSchema.path('question').required(true, 'question Required');
// QuestionSchema.path('answer').required(true, 'answer Required');
// QuestionSchema.path('fake_answer1').required(true, 'fake answer 1 Required');
// QuestionSchema.path('fake_answer2').required(true, 'fake answer 2 Required');
mongoose.model("Question", QuestionSchema);
var Question = mongoose.model("Question");

//Routes

app.get("/users", (req, res, next) => {
   User.find({}, function (err, users){
      console.log("server > get users")
      res.json(users)
   })
});

app.post("/users", (req, res, next) => {
   console.log("server > create", req.body);
   let userInstance = new User(req.body);
   userInstance.save(function(err){
      if (err){
         return res.json(err)
      }
   })
})

app.post("/questions", (req, res, next) => {
   console.log("server > createQuestion()", req.body)
   let questionInstance = new Question(req.body);
   questionInstance.save(function(err){
      if (err){
         return res.json(err)
      }
   })
})

app.all("*", (req,res,next) => {
   res.sendFile(path.resolve("./public/dist/index.html"))
})

app.listen(8000, () => console.log("local port 8000"))
