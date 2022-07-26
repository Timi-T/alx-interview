#!/usr/bin/node
/* Module to print all characters of a movie from a starwars movie */

const request = require('request');

function printCharacters (index, arr) {
  /* Print all the characters from the api */
  if (index === arr.length) {
    return;
  }
  request((arr[index]), (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const character = JSON.parse(body);
    console.log(character.name);
    printCharacters(index + 1, arr);
  });
}

const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  printCharacters(0, body.characters);
});
