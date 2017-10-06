var mongoose = require('mongoose');
var PersonSchema = new mongoose.Schema({
   name: String,
}, {timestamps: true});

var Person = mongoose.model('Person', PersonSchema);
