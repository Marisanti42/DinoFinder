import Express from "express";
import cors from 'cors'
import fs from "fs";
import dinobase from "./dinosaurs.js";

// var corsOptions = {
//   origin: 'http://example.com',
//   optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
// }

let about_txt;
fs.readFile("./static_content/about.txt", "utf8", (err, data) => {
  if (err) {
    return;
  }
  about_txt = data;
});

let endpoints;
fs.readFile("./static_content/endpoints.json", (err, data) => {
  if (err) {
    return;
  }
  endpoints = data;
});

const app = Express();
app.use(cors());
const port = 1212;

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.get("/about", (req, res) => {
  res.end(about_txt);
});

app.get("/endpoints", (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(endpoints);
});

app.get("/dinosaur/:dinoName", (req, res) => {
  dinobase.forEach((dino) => {
    if (dino.name == req.params.dinoName) {
      res.json(dino);
    }
  });
  res.send("not found");
});

app.get("/random", (req, res) => {
  res.send(dinobase[Math.floor(Math.random() * dinobase.length)]);
});

app.listen(port, () => {});
