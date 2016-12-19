'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/', function cica(request, response) {
  response.send('Hey! TomCat');
});

exampleApp.post('/', function kutya(request, response) {
  response.send('Hello te lo');
});

exampleApp.listen(3000);
