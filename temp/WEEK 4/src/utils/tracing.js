const { v4: uuidv4 } = require("uuid");

function tracingMiddleware(req, res, next) {
  const incomingId = req.headers["x-request-id"];

  const requestId = incomingId || uuidv4();

 
  req.requestId = requestId;


  res.setHeader("X-Request-ID", requestId);

  next();
}

module.exports = tracingMiddleware;