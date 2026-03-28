const express = require("express");
const os = require("os");

const app = express();
const PORT = 3000;

let count = 0;

app.get("/", (req, res) => {
  count++;
  res.send(`Request #${count} handled by ${os.hostname()}`);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});