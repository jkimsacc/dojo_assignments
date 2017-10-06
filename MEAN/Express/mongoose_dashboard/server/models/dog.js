var mongoose = require('mongoose');
var DogSchema = new mongoose.Schema({
  name: String,
}, {timestamps: true});

var Dog = mongoose.model('Dog', DogSchema);
