let express = require("express");
let app = express();

let mongoose = require("mongoose");
mongoose.connect('mongodb://localhost/playerSchema');
let PlayerSchema = new mongoose.Schema({
   name: {type: String, require: true },
   position: {type:String, require: true },
   game1: {type: String},
   game2: {type: String},
   game3: {type: String},
});
mongoose.model("Player", PlayerSchema);
let Player = mongoose.model("Player");

const path = require("path");

let bodyParser = require("body-parser")
// app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

app.use(express.static(__dirname + '/public/dist'));


app.get("/players", (req, res, next) => {
   Player.find({}, function(err, players){
      console.log("server > get")
      res.json(players)
   })
})

app.post("/players", (req, res, next) => {
   console.log("server > create");
   let playerInstance = new Player(req.body);
   playerInstance.save(function(err){
      if (err){
         return res.json(err)
      }
      Player.find({}, function(err, players){
         res.json(players);
      })
   })
})

app.delete("/players/:id", (req, res, next) => {
   console.log("Server > delete", req.params.id);
   Player.deleteOne({_id:req.params.id}, (err, data)=>{
      if (err) return res.json(err)
      else return res.json(true)
   })
})

app.put('/players/:id', (req, res, next) => {
   console.log("Server > Put", req.params.id);
   console.log("Server > Put", req.body)
   // Player.find({})
})


app.all("*", (req, res, next) => {
   res.sendfile(path.resolve("./public/dist/index.html"))
})

app.listen(1337, ()=> console.log("listening to 1337"))
