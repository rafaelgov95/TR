'use strict'
require('./db/config')
var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var mongodb = require('mongoose');
var router = express.Router();
var app = express();
// view engine setup
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Request-Width, Content-Type, Accept, x-access-token ');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    next();
});
const login = require('./routes/crud-login/api')('schema-login', 'login')
const posts = require('./routes/crud-post/api')('schema-posts', 'posts')
const valida_login = require('./routes/new-login')

app.use('/api/login', login)
app.use('/api/autentica', valida_login) // autentica
app.use('/api/posts', posts) // postagens do blog

app.use('/*',function (req, res) {
    res.sendFile(__dirname + '/public/index.html');
});
app.use(function (err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error');
});

module.exports = app;