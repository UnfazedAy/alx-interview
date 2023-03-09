#!/usr/bin/node

const argv = process.argv
const request = require('request');

function getPromise (url) {
  const promise = new Promise(function (resolve, reject) {
    request(url, function (err, res, body){
        if (err) reject(err); else resolve(body);
    });
  });
  return promise
}

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, async function (err, res, body) {
  if (err) throw err;
  const data = JSON.parse(body).characters;

  for (let i of data) {
    const res = await getPromise(i)
    console.log(res)
  }
});