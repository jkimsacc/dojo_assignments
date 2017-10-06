//express
let express = require('express');
let app = express();

//body-parser
let bodyParser = require('body-parser');
app.use(bodyParser.json())

//path
let path = require('path')
app.use(express.static(path.join(__dirname, '/public/dist')));

//mongoose
let mongoose = require("mongoose");
mongoose.connect('mongodb://localhost/survey');
mongoose.Promise = global.Promise;

//Schema
let UserSchema = new mongoose.Schema({
   email: { type: String, required: [true, 'Please input your Email.'] },
   password: { type: String, required: [true, 'Please input your password.']},
})

//Routes
app.post("/users", (req, res, next) => {
   console.log("Server > post '/users' | req.body:", req.body);
   User.create(req.body, function(err, user){
      if(err){
         console.log(err)
      } else {
         console.log("Success!")
      }
   })
})

app.all("*", (req, res, next) => {
   res.sendFile(path.resolve("./public/dist/index.html"))
});

app.listen(8000, function() {
   console.log("port 8000")
})
