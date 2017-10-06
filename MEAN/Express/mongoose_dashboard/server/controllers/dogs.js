var mongoose = require('mongoose');
var Dog = mongoose.model('Dog')
module.exports = {
   create: function(req, res) {
      var newDog = new Dog(req.body);
      newDog.save(function(err) {
         if (err) {
            res.redirect('/', {title: 'error!!', errors: newDog.errors})
         } else {
            console.log('created!');
            res.redirect('/');
         }
      })
   },
   show_all: function(req, res) {
      Dog.find({}, function(err, results){
         res.render('./../client/views/index', {dogs: results});
      })
   },
   show_one: function(req, res) {
      Dog.findOne({_id: req.params.id}, function(err, result){
         res.render('./../client/views/dog', { dog : result});
      })
   },
   update: function(req, res) {
      Dog.update({_id: req.params.id}, req.body, function(err, result){
         res.redirect('/dogs/:id');
      })
   },
   destroy: function(req, res) {
      Dog.remove({_id: req.params.id}, function(err, results){
         if (err) {console.log(err);}
         res.redirect('/');
      });
   }
}
