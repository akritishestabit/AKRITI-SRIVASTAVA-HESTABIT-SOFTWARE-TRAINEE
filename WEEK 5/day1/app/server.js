const http = require("http");

const PORT = 3000;

const server = http.createServer((req, res) => {
  console.log(`Request received at ${new Date().toISOString()}`);
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ message: "Docker Day 1 Running " }));
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});