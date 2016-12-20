'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/*', function cica(request, response) {
  response.send('The request come form: ' + request.url + '\nHey! Tomi ' + new Date());
});


exampleApp.listen(3000);
