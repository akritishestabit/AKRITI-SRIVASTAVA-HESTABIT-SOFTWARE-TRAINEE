// const express = require("express");

// const app = express();
// const PORT = 3000;

// app.get("/", (req, res) => {
//   res.send("Hello from backend container");
// });

// app.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
// });

const express = require("express");
const os = require("os");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send(`Response from container: ${os.hostname()}`);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});