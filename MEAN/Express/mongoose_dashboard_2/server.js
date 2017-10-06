var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/mongoose_dashboard');
mongoose.Promise = global.Promise;

var DogSchema = new mongoose.Schema({
  name: String,
}, {timestamps: true});
mongoose.model('Dog', DogSchema);
var Dog = mongoose.model('Dog')

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
  Dog.find({}, function(err, results){
    if(err) {console.log(err); }
    res.render('index', { dogs: results});
  })
});

app.post('/create', function(req, res) {
  console.log("POST DATA", req.body);
  var dog = new Dog(req.body);
  console.log(dog);
  dog.save(function(err){
    if (err) {
      console.log("sounds good, doesn't work");
      res.render('/', {title: 'you have errors!', errors: dog.errors})
    } else {
      console.log('Welcome to the pack!')
      res.redirect('/');
    }
  })
});

app.get('/dogs/:id', function(req, res) {
  Dog.findOne({_id : req.params.id}, function(err, results){
    if(err) {
      console.log(err);
    }
    console.log(results);
    res.render('dog', { dog : results });
  });
});

app.get('/dogs/edit/:id', function(req, res) {
  Dog.findOne({_id : req.params.id}, function(err, results){
    if(err) {
      console.log(err);
    }
    res.render('edit', { dog : results});
  });
});

app.post('/dogs/edit/:id', function(req, res) {
  Dog.update({_id: req.params.id}, req.body, function(err, results){
    if (err) { console.log(err); }
    res.redirect('/');
  });
});

app.get('/dogs/destroy/:id', function(req,res){
  Dog.remove({_id: req.params.id}, function(err, results){
    if (err) {console.log(err);}
    res.redirect('/');
  });
});

app.listen(8000, function() {
  console.log("listening on port 8000");
});
