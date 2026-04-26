# WEEK 2 — FRONTEND FUNDAMENTALS (HTML, CSS, JAVASCRIPT)

## Overview

This week focused on building strong frontend foundations by combining semantic HTML, modern CSS layouts, and JavaScript (ES6+) to create responsive and interactive user interfaces.

The emphasis was on understanding how the browser renders UI, structuring clean layouts, and adding dynamic behavior using JavaScript without relying on frameworks.

---

## DAY 1 — HTML5 + Semantic Layout

### Objective

Build a strong understanding of HTML structure using semantic elements and accessibility principles.

### Work Done

* Created a fully structured blog page using only semantic HTML (no `<div>` usage)
* Used tags like:

  * `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
* Built forms with:

  * Input fields, dropdowns, and validation
* Embedded media:

  * Images, video/audio elements
* Applied accessibility basics:

  * `alt` attributes
  * ARIA labels
  * Proper tab navigation

### Key Learning

Semantic HTML improves readability, accessibility, and SEO while making the structure self-explanatory.

### Deliverable

* `blog.html`

---

## DAY 2 — CSS Layout Mastery (Flexbox + Grid)

### Objective

Design responsive layouts using modern CSS techniques.

### Work Done

* Practiced advanced CSS selectors:

  * Attribute selectors, sibling selectors, `nth-child`
* Built layouts using:

  * Flexbox (for 1D layouts like navbar and hero section)
  * CSS Grid (for 2D layouts like product grids)
* Implemented responsive design:

  * Mobile-first approach
  * Media queries for different screen sizes

### Features Implemented

* Responsive navbar
* Hero section layout
* Dynamic product grid (adjusts columns based on screen width)

### Key Learning

Flexbox is ideal for alignment and spacing, while Grid is better for full-page layouts. Combining both leads to clean and scalable UI design.

### Deliverables

* `index.html`
* `style.css`
* UI comparison screenshots

---

## DAY 3 — JavaScript ES6 + DOM Manipulation

### Objective

Understand modern JavaScript and how to manipulate the DOM dynamically.

### Work Done

* Practiced ES6 concepts:

  * `let` vs `const`
  * Arrow functions
  * Destructuring and spread operator
* Used array methods:

  * `map`, `filter`, `reduce`
* Built interactive components:

  * Navbar toggle
  * Dropdown menu
  * Modal popup

### Mini Project

* Created an interactive FAQ accordion:

  * Click to expand/collapse answers
  * Smooth DOM updates using event listeners

### Key Learning

JavaScript brings interactivity to static pages, and understanding DOM manipulation is the foundation before moving to frameworks.

### Deliverable

* `/js-dom-practice/`

---

## DAY 4 — JS Utilities + LocalStorage Project

### Objective

Write modular JavaScript and persist data using browser storage.

### Work Done

#### Debugging

* Used browser DevTools:

  * Breakpoints
  * Watch variables

#### Utility Functions

* Implemented reusable utilities:

  * Debounce
  * Throttle
  * GroupBy

#### Todo App (Mini Project)

* Built a fully functional Todo application:

  * Add tasks
  * Edit tasks
  * Delete tasks
  * Persist data using LocalStorage

#### Error Handling

* Used `try-catch` for safe execution
* Maintained error logs:

```id="errlog"
/logs/errors.md
```

### Key Learning

LocalStorage enables persistence without a backend, and modular code improves maintainability and scalability.

### Deliverable

* `todo-app/`

---

## DAY 5 — Capstone Project (E-commerce UI)

### Objective

Combine HTML, CSS, and JavaScript to build a complete, responsive application.

### Project Description

Developed a mini e-commerce product listing page using real API data.

### Features Implemented

#### Data Fetching

* Used Fetch API:

```id="fetchapi"
https://dummyjson.com/products
```

#### UI Rendering

* Displayed product cards with:

  * Title
  * Image
  * Price

#### Functionalities

* Search bar:

  * Filters products dynamically
* Sorting:

  * Price (High → Low)
* Responsive design:

  * Works across mobile, tablet, desktop

### Final Touches

* Clean UI layout
* Optimized responsiveness
* Improved user interaction

### Deliverables

* Repository: `week2-frontend`
* Pages:

  * `/index.html`
  * `/products.html`

---

## Key Learnings

* Semantic HTML creates meaningful and accessible structures
* Flexbox and Grid are essential for modern responsive layouts
* JavaScript (ES6+) simplifies complex logic with cleaner syntax
* DOM manipulation is the core of frontend interactivity
* LocalStorage enables persistence without backend support
* Building a full project improves understanding of real-world workflows

---

## Folder Structure

```id="folder2"
week2-frontend/
│
├── index.html
├── products.html
├── style.css
├── js/
│   ├── main.js
│   ├── utils.js
│
├── js-dom-practice/
├── todo-app/
├── logs/
└── README.md
```

---

## Final Note

This week transitioned from static structure to dynamic applications. It built the foundation required to move into frontend frameworks by strengthening core concepts of layout, interactivity, and state handling in the browser.
