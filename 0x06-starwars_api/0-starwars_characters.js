#!/usr/bin/node
// list characters of a given film

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            console.error('error:', error);
          } else {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});