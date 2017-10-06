var mongoose = require('mongoose');
var dogs = require('../controllers/dogs')

module.exports = function(app) {
   app.get('/', function(req, res) {
      dogs.show_all(req, res)
   });
   app.post('/create', function(req, res) {
      dogs.create(req, res)
   });
   app.get('/dogs/:id', function(req, res) {
      dogs.show_one(req, res)
   });

   app.get('/dogs/edit/:id', function(req, res) {
      dogs.edit(req, res)
   });

   app.post('/dogs/edit/:id', function(req, res) {
     dogs.update(req, res)
   });

   app.get('/dogs/destroy/:id', function(req,res){
      dogs.destroy(req, res)
   });
}
