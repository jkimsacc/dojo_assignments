//express
let express = require('express');
let app = express();

//session
let session = require('express-session');
let sessionStore = new session.MemoryStore;
app.use(session({
   cookie: { maxAge: 60000 },
   store: sessionStore,
   saveUninitialized: true,
   resave: true,
   secret: 'its a secret to everyone'
}))

//body-parser
let bodyParser = require('body-parser');
app.use(bodyParser.json())

//path
let path = require('path')
app.use(express.static(path.join(__dirname, '/public/dist')));

//mongoose
var mongoose = require("mongoose");
mongoose.connect('mongodb://localhost/trivia');
mongoose.Promise = global.Promise;

//Schema
let UserSchema = new mongoose.Schema({
   username: { type: String, required: true},
   score: { type: Number},
})

mongoose.model('User', UserSchema);
let User = mongoose.model('User');

let QuestionSchema = new mongoose.Schema({
   question: { type: String, minlength: 10, required: true },
   answer: { type: String, required: true },
   fake_answer1: { type: String, required: true },
   fake_answer2: { type: String, required: true },
})

mongoose.model('Question', QuestionSchema);
let Question = mongoose.model('Question');

//Routes
app.post('/users', (req, res, next) => {
   console.log('server post')
   new User(req.body).save()
   .then((user) =>{
      console.log("db user stored")
      req.session.username = user.username;
      req.session.user_id = user._id;
      console.log("session: " + req.session)
      res.json(true);
   }).catch((err) => {
      console.log(err)
      res.json(err)
   })
})

app.get('/users', (req, res, next) => {
   User.find({}, (err, users) => {
      if(err){
         res.json(err);
      }
      else{
         res.json(users);
      }
   }).sort({score: -1})
})

app.post('/questions', (req, res, next) => {
   console.log('server post')
   new Question(req.body).save()
   .then((question) => {
      console.log("Question stored");
   }).catch((err) => {
      console.log(err)
      res.json(err);
   })
})

app.get('/questions', (req, res, next) => {
   Question.find({}, (err, questions) => {
      if(err){
         res.json(err);
      }
      else{
         res.json(questions);
      }
   })
})

app.post('/score', (req, res, next) => {
    let score = req.headers.score;
    User.update({_id: req.session.user_id}, {score: score}, function(err) {
        if(err) {
            console.log(err)
        }else {
            res.json();
        }
    });
});

app.delete('/logout', (req, res, next) => {
   req.session.destroy();
   res.json(true);
})


app.all("*", (req, res, next) => {
   res.sendFile(path.resolve("./public/dist/index.html"))
});

app.listen(8000, function() {
   console.log("port 8000")
})
