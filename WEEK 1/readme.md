# WEEK 1 — ENGINEERING MINDSET BOOTCAMP

## Overview

This week focused on building a strong engineering mindset by working with system-level tools, Node.js, Git, networking, and automation. The goal was not just writing code, but understanding how systems behave, debugging efficiently, and building reliable workflows.

---

## DAY 1 — System Reverse Engineering + Node & Terminal

### Objective

Understand the system environment using Node.js and terminal tools.

### Tasks Performed

* Built a Node.js script `sysinfo.js` to extract:

  * Hostname
  * Available disk space (in GB)
  * Top 5 open ports
  * Default gateway
  * Logged-in users count

* Created shell aliases for productivity:

```bash
alias gs="git status"
alias files="ls -lha"
alias ports="lsof -i -P -n | grep LISTEN"
```

* Captured runtime metrics using:

  * `process.cpuUsage()`
  * `process.resourceUsage()`

* Stored metrics in:

```
/logs/day1-sysmetrics.json
```

### Deliverables

* `sysinfo.js`
* Shell config snippet (`.bashrc` / `.zshrc`)
* `logs/day1-sysmetrics.json`

---

## DAY 2 — Node CLI & Concurrency

### Objective

Build a performant CLI tool and understand parallel processing.

### Implementation

Created CLI tool:

```
stats.js --lines <file> --chars <file> --words <file>
```

### Features

* Counts:

  * Total lines
  * Total words
  * Total characters

* Processes multiple files in parallel using async operations

* Outputs performance report:

```json
{
  "file": "data1.txt",
  "executionTimeMs": 51,
  "memoryMB": 14.3
}
```

### Bonus Feature

* Removes duplicate lines
* Writes output to:

```
/output/unique-<filename>
```

### Deliverables

* `stats.js`
* `/logs/performance*.json`
* Processed output files

---

## DAY 3 — Git Mastery

### Objective

Develop strong version control and debugging skills.

### Tasks Performed

* Created a repository with 10 commits

* Introduced a bug intentionally in commit 5

* Used `git bisect` to identify the faulty commit

* Created a release branch:

```
release/v0.1
```

* Used `git cherry-pick` to selectively bring changes

* Used `git stash` to:

  * Save uncommitted work
  * Switch branches safely
  * Restore changes

### Documentation

* Recorded bisect logs
* Documented cherry-pick decisions
* Demonstrated stash workflow

### Deliverables

* `bisect-log.txt`
* `cherry-pick-report.md`
* `stash-proof.txt`
* Commit graph screenshot

---

## DAY 4 — HTTP / API Forensics

### Objective

Understand APIs, headers, and request/response analysis.

### Tasks Performed

#### cURL Analysis

* Fetched GitHub API:

```
curl -v https://api.github.com/users/octocat
```

* Extracted:

  * Rate limit remaining
  * ETag
  * Server header

#### Pagination Study

* Explored paginated API:

```
/users/octocat/repos?page=1&per_page=5
```

* Analyzed:

  * Link headers
  * Navigation across pages

#### Postman Collection

Created API test collection:

* GET user data
* GET repositories (multiple pages)

#### Node HTTP Server

Built a simple server with:

* `/ping` → returns timestamp
* `/headers` → returns request headers
* `/count` → maintains in-memory counter

### Deliverables

* `curl-headers.txt`
* `pagination-analysis.md`
* Postman collection (`.json`)
* `server.js`

---

## DAY 5 — Automation & Mini CI Pipeline

### Objective

Automate workflows and simulate a CI pipeline.

### Tasks Performed

#### Health Monitoring Script

Created:

```
healthcheck.sh
```

* Pings server every 10 seconds
* Logs failures:

```
/logs/health.log
```

#### Pre-commit Validation (Husky)

Implemented checks:

* Prevent `.env` file commits
* Enforce JS formatting
* Ignore log files

#### Packaging

Generated bundle:

```
bundle-<timestamp>.zip
```

Includes:

* `src/`
* `logs/`
* `docs/`
* `checksums.sha1`

#### Scheduling

* Configured cron job:

  * Runs health check every 5 minutes

### Deliverables

* `healthcheck.sh`
* Husky pre-commit screenshots
* `bundle*.zip`
* `checksums.sha1`
* Cron job screenshot

---

## Key Learnings

* Systems are observable if you know where to look (logs, ports, headers)
* Performance measurement is as important as functionality
* Git is not just version control — it's a debugging tool
* APIs reveal a lot through headers, not just data
* Automation reduces human error and improves reliability

---

## Folder Structure

```
week1/
│
├── day1/
├── day2/
├── day3/
├── day4/
├── day5/
└── README.md
```

---

## Final Note

This week emphasized thinking like an engineer — breaking systems, observing behavior, and building tools that are reliable, measurable, and maintainable.
