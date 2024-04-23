#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(response.body);
    const completedTasks = {};
    tasks.forEach((task) => {
      if (task.completed === true) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
