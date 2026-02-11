const os = require("os");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

function getAvailableDiskSpaceGB() {
  try {
    const output = execSync("df -k /").toString().split("\n")[1].split(/\s+/);
    const availableKB = output[3];
    return (availableKB / 1024 / 1024).toFixed(2);
  } catch {
    return null;
  }
}

function getOpenPorts() {
  try {
    const output = execSync(
      "lsof -i -P -n | grep LISTEN | head -n 5",
    ).toString();
    return output.trim().split("\n");
  } catch {
    return [];
  }
}

function getDefaultGateway() {
  try {
    const output = execSync("ip route | grep default").toString();
    return output.split(" ")[2];
  } catch {
    return null;
  }
}

function getLoggedInUsersCount() {
  try {
    const output = execSync("who").toString();
    return output.trim().split("\n").length;
  } catch {
    return 0;
  }
}

const sysInfo = {
  hostname: os.hostname(),
  availableDiskGB: getAvailableDiskSpaceGB(),
  openPorts: getOpenPorts(),
  defaultGateway: getDefaultGateway(),
  loggedInUsers: getLoggedInUsersCount(),

  cpuUsage: process.cpuUsage(),
  resourceUsage: process.resourceUsage(),

  timestamp: new Date().toISOString(),
};

const logDir = path.join(__dirname, "logs");
if (!fs.existsSync(logDir)) {
  fs.mkdirSync(logDir);
}

fs.writeFileSync(
  path.join(logDir, "day1-sysmetrics.json"),
  JSON.stringify(sysInfo, null, 2),
);

console.log("Day 1 system metrics captured successfully");
