var restify = require('restify');

function getStatus(req, res, next) {
    res.send({"device": req.params.id, "data": "Something useful would go here"});
    next();
}

var server = restify.createServer();
server.get('/status/:id', getStatus);

server.listen(8000, function() {
    console.log('%s listening at %s', server.name, server.url);
});