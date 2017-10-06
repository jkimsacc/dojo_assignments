var mongoose = require('mongoose');
var Task = mongoose.model('Task')

module.exports = {
   show_all: (req, res) => {
      Task.find({}, (err, results) => {
         err ? console.log(err.message) :res.json(tasks);
      });
   },
   create: function(req, res) {
      var task = new Task(req.body);
      newTask.save((err) => {
         err ? console.log(err.message) : res.json(task);
      })
   },
   retrieve: (req,res) => {
      Task.findOne(req.params, (err, task) => {
         err ? console.log(err.message) : res.json(task);
      })
   }
   update: function(req, res) {
      Task.findOneAndUpdate(req.params, req.body, (err, task) => {
         err ? console.log(err.message) : res.json(task);
      })
   },
   delete: function(req, res) {
      Task.findOneAndRemove(req.params, (err, task) => {
         err ? console.log(err.message) : res.json(task);
      })
   }
}
