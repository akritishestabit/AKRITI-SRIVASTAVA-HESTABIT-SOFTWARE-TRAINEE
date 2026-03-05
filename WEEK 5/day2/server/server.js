const express = require("express");
const mongoose = require("mongoose");

const app = express();
const PORT = 5000;

const MONGO_URL = "mongodb://mongo:27017/testdbdockerfile";

mongoose
  .connect(MONGO_URL)
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

app.get("/", (req, res) => {
  res.send("Backend running with Docker Compose");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});