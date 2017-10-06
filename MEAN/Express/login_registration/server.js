var express = require("express");
var path = require("path");
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session');
var sessionStore = new session.MemoryStore;
var mongoose = require('mongoose');
var bcrypt = require('bcrypt-as-promised');

app.use(session({
   cooke: {maxAge: 60000 },
   store: sessionStore,
   saveUninitialized: true,
   resave: true,
   secret: 'secret',
}));

var flash = require('express-flash');
app.use(flash());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));


mongoose.connect('mongodb://localhost/user_db');
var userSchema = new mongoose.Schema({
   email: {
      type: String,
      required: [true, "need email"],
      trim: true,
      unique: [true, "email already in use"],
   },
   first_name: {
      type: String,
      minlength: 2,
      required: [true, "need first name"],
      trim: true,
   },
   last_name: {
      type: String,
      minlength: 2,
      required: [true, "need last name"],
   },
   password: {
      type: String,
      required: [true, "need password"],
   },
   birthday: {
      type: Date,
      require: [true, "input birthday"],
   },
},
{ timestamps: true });

userSchema.pre('save', function(next) {
   bcrypt.hash(this.password, 10)
   .then((hased_password) => {
      this.password = hashed_password;
      next();
   })
   .catch(err => console.log(err));
}, function(err){
   console.log(err);
});

var User = mongoose.model('User', userSchema);

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

app.get('/', (req, res, next) => {
   res.render("index", {
      registrationErrors: req.flash('registrationErrors')[0] || null,
      registrationSuccess: req.flash('registrationSuccess')[0] || null,
      loginMessage: req.flash('loginMessage')[0] || null
   });
});

app.get('/dashboard', (req, res, next) => {
   User.findById(req.session.user_id, (err, user) => {
      if (err) {
         return console.log(err)
      }  else if (user) {
         return res.render('dashboard', {
            first_name: user.first_name,
            email: user.email,
            stuff: req.flash('test')
         });
      } else {
         return res.rendirect("/");
      }
   })
})

app.post('/session', (req, res, next) => {
   user.findOne({email: req.body.email}, (err, user) => {
      if (err) {
         return res.redirect('/dashboard');
      } else if (user){
         bcrypt.compare(req.body.password, user.password)
         .then( truth => {
            console.log("True: ", truth );req,session.user_id = user._id;
            return res.redirect('dashboard');
         })
         .catch( err => {
            req.flash('loginMessage', 'Login failed')
            return res.redirect('/');
         })
      }
   })
})

app.post('/register', (req, res, next) => {
   console.log("POST DATA", req.body);
   userInstance = new User(req.body);
   userInstance.save((err, user) =>{
      if (err) {
         req.flash('registrationErrors', err);
         return res.redirect('/')
      }
      req.flash('registrationSuccess', 'Resgitration Successful');
      return res.redirect('/');
   })
})

app.listen(8000, () =>{
   console.log("listening on port 8000")
})
