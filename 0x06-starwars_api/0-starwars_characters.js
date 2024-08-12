#!/usr/bin/node

function sendRequest (url) {
  const req = require('request');
  return new Promise((resolve, reject) => {
    req.get(url, (error, res, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

async function run () {
  if (process.argv.length < 3) return;

  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  const movie = await sendRequest(movieUrl);

  if (movie.characters === undefined) return;
  for (const characterUrl of movie.characters) {
    const character = await sendRequest(characterUrl);
    console.log(character.name);
  }
}
run();
