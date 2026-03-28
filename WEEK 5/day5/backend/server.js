

const express = require("express");
const mongoose = require("mongoose");

const app = express();
const PORT = process.env.PORT;

mongoose.connect(process.env.MONGO_URL)
  .then(() => console.log("Mongo connected"))
  .catch(err => console.log(err));

app.get("/api", (req, res) => {
  res.send("Hello from Backend");
});

app.get("/health", (req, res) => {
  res.send("OK");
});

app.listen(PORT, () => {
  console.log("Server running on " + PORT);
});