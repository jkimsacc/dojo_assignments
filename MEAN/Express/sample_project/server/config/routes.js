var quotes = require('../controllers/quotes.js');
module.exports = function(app) {
  app.get('/', function(req, res) {
    res.render('./../../client/views/index')
  })
  app.post('/quotes', function(req,res){
    quotes.create(req, res)
  })
  app.get('/main', function (req, res) {
    quotes.show(req, res)
  })
}
