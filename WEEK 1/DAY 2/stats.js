const fs = require("fs");
const path = require("path");
const args = process.argv.slice(2);


const countLines = args.includes("--lines");
const countWords = args.includes("--words");
const countChars = args.includes("--chars");
const removeDuplicates = args.includes("--unique");


const files = args.filter(arg => !arg.startsWith("--"));

if (files.length === 0) {
  console.error("No input files provided");
  process.exit(1);
}


const logDir = path.join(__dirname, "logs");
const outputDir = path.join(__dirname, "output");

if (!fs.existsSync(logDir)) {
  fs.mkdirSync(logDir);
}

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}


function processFile(file) {
  return new Promise((resolve, reject) => {
    const startTime = Date.now();
    const startMemory = process.memoryUsage().heapUsed;

    fs.readFile(file, "utf-8", (err, data) => {
      if (err) {
        return reject(err);
      }

      const lines = data.split("\n");
      //const lines = data.split("\n").filter(line => line.trim() !== "");
      const words = data.split(/\s+/).filter(Boolean);
      const chars = data.length;


      if (removeDuplicates) {
        const uniqueLines = [...new Set(lines)];
        const outputFile = path.join(
          outputDir,
          `unique-${path.basename(file)}`
        );
        fs.writeFileSync(outputFile, uniqueLines.join("\n"));
      }

      const endTime = Date.now();
      const endMemory = process.memoryUsage().heapUsed;

      resolve({
        file: path.basename(file),
        lines: countLines ? lines.length -1 : undefined,
        words: countWords ? words.length : undefined,
        chars: countChars ? chars : undefined,
        executionTimeMs: endTime - startTime,
        memoryMB: ((endMemory - startMemory) / 1024 / 1024).toFixed(2)
      });
    });
  });
}


Promise.all(files.map(processFile))
  .then(results => {
    const logFile = path.join(
      logDir,
      `performance-${Date.now()}.json`
    );

    fs.writeFileSync(logFile, JSON.stringify(results, null, 2));

    console.log("File processing completed");
    console.log(results);
  })
  .catch(error => {
    console.error("Error while processing files:", error.message);
  });
