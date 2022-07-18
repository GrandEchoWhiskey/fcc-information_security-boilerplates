const express = require('express');
const app = express();
const helmet = require('helmet');

let ninetyDaysInMilliseconds = 90 * 24 * 60 * 60;

module.exports = app;
const api = require('./server.js');
app.use(helmet.noCache());
app.use(helmet.dnsPrefetchControl());
app.use(helmet.hsts({ maxAge: ninetyDaysInMilliseconds }));
app.use(helmet.ieNoOpen());
app.use(helmet.noSniff());
app.use(helmet.frameguard({action: 'deny'}));
app.use(helmet.hidePoweredBy({setTo: 'PHP'}));
app.use(helmet.xssFilter());
app.use(helmet.contentSecurityPolicy({directives: {
      "defaultSrc": ["'self'"],
      "scriptSrc": ["'self'", "trusted-cdn.com"]
    }}));
app.use(express.static('public'));
app.disable('strict-transport-security');
app.use('/_api', api);
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});
let port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Your app is listening on port ${port}`);
});
