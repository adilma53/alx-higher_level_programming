#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    const completed = {};
    const task = JSON.parse(body);
    for (const i in task) {
      if (task[i].completed === true) {
        if (completed[task[i].userId] === undefined) {
          completed[task[i].userId] = 1;
        } else {
          completed[task[i].userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + resp.statusCode);
  }
});
