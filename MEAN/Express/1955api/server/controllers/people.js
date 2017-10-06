var mongoose = require('mongoose');
var Person = mongoose.model('Person');

module.exports = {
   show_all: function(req, res) {
      Person.find({}, function(err, results) {
         res.json(results)
      })
   },
   show_one: function(req, res) {
      Person.findOne({_name: req.params.name}, function(err, result) {
         res.json(result)
      })
   },
   create: function(req, res) {
      var person = new Person({name: req.params.name});
      person.save(function(err) {
         if(err){
            console.log("meh");
         } else {
            res.redirect('/');
         }
      })
   },
   destroy: function(req, res) {
      Person.remove({_name: req.params.name}, function(err, results){
         if (err) {console.log(err);}
         res.redirect('/');
      })
   }
}
