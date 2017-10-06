var mongoose = require('mongoose');
var person = require('./../controllers/people')

module.exports = function (app) {
   app.get('/', function(req, res) {
      person.show_all(req, res);
   });
   app.get('/new/:name/', function(req, res) {
      person.create(req, res);
   });
   app.get('/remove/:name/', function(req,res) {
      person.destroy(req, res);
   });
   app.get('/:name', function(req, res) {
      person.show_one(req, res);
   });
}
