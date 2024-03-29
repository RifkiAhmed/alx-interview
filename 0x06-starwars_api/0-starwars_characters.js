#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (body) {
    const film = JSON.parse(body);
    const filmCharacters = film.characters;

    const characters = filmCharacters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body));
          }
        });
      });
    });

    Promise.all(characters)
      .then((characters) => {
        characters.forEach((character) => {
          console.log(character.name);
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
