var mongoose = require('mongoose');
var tasks = require('../controllers/tasks')

module.exports = function(app) {
   app.get('/', function(req,res){
      res.redirect('/tasks')
   });
   app.get('/tasks', function(req, res){
      tasks.show_all(req, res)
   });
   app.post('/tasks', function(req, res) {
      tasks.create(req,res)
   });
   app.put('/tasks/:id', function(req, res) {
      task.update(req,res)
   });
   app.delete('/tasks/:id', function(req, res) {
      task.delete(req, res)
   });
}
