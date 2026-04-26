# UI COMPONENT LIBRARY DOCUMENTATION

## Overview

This project follows a **hybrid component architecture**:

* **Feature-based components** → grouped by domain (auth, dashboard, billing, etc.)
* **Reusable UI components** → stored in `/ui` (atomic design)

This separation ensures scalability, maintainability, and clean code organization.

---

## Folder Structure

```bash
components/
│
├── auth/           # Authentication-related UI
├── billing/        # Billing & payments UI
├── dashboard/      # Dashboard-specific components
├── profile/        # User profile components
├── tables/         # Table components (data display)
├── ui/             # Reusable atomic components

```

---

## Architecture Approach

### 1. Feature-Based Components

These are **not reusable globally**, but scoped to a feature.

Examples:

* `dashboard/` → charts, widgets
* `auth/` → login/signup UI
* `billing/` → invoices, plans

They may internally use components from `/ui`.

---

### 2. Reusable UI Components (Atomic Design)

Located in:

```bash
/components/ui/
```

These are:

* Generic
* Reusable across all features
* Controlled via props

---

## UI Components

---

## 1. Button Component

### File

```bash
/components/ui/Button.jsx
```

### Description

Reusable button with variants and sizes.

### Props

| Prop     | Type   | Description                   |
| -------- | ------ | ----------------------------- |
| children | node   | Button content                |
| variant  | string | primary / secondary / outline |
| size     | string | sm / md / lg                  |
| onClick  | func   | Click handler                 |

### Usage

```jsx
import Button from "@/components/ui/Button";

<Button variant="primary">Save</Button>
```

---

## 2. Input Component

### File

```bash
/components/ui/Input.jsx
```

### Description

Reusable input field with consistent styling.

### Props

| Prop        | Type   | Description      |
| ----------- | ------ | ---------------- |
| type        | string | input type       |
| placeholder | string | placeholder text |
| value       | string | input value      |
| onChange    | func   | handler          |

### Usage

```jsx
import Input from "@/components/ui/Input";

<Input placeholder="Enter email" />
```

---

## 3. Card Component

### File

```bash
/components/ui/Card.jsx
```

### Description

Wrapper component for grouping content.

### Usage

```jsx
import Card from "@/components/ui/Card";

<Card>
  <h2>Dashboard</h2>
</Card>
```

---

## 4. Badge Component

### File

```bash
/components/ui/Badge.jsx
```

### Description

Small status indicator.

### Usage

```jsx
import Badge from "@/components/ui/Badge";

<Badge text="Active" />
```

---

## 5. Modal Component

### File

```bash
/components/ui/Modal.jsx
```

### Description

Overlay popup component.

### Props

| Prop    | Type | Description   |
| ------- | ---- | ------------- |
| isOpen  | bool | visibility    |
| onClose | func | close handler |

### Usage

```jsx
import Modal from "@/components/ui/Modal";

<Modal isOpen={true}>
  Content
</Modal>
```

---

## Layout Components

---

## Sidebar

### File

```bash
/components/Sidebar.jsx
```

### Description

Main navigation sidebar used across dashboard pages.

### Features

* Uses `usePathname()` for active route detection
* Displays navigation items using `SidebarItem`
* Includes helper section via `SidebarHelp`

---

## SidebarItem

### File

```bash
/components/SidebarItem.jsx
```

### Description

Single navigation item inside sidebar.

### Responsibilities

* Icon + label rendering
* Active state styling
* Route linking

---

## SidebarHelp

### File

```bash
/components/SidebarHelp.jsx
```

### Description

Support/help section inside sidebar.


---

## Key Learnings

* Feature-based structure improves scalability
* UI components should remain generic and reusable
* Tailwind enables fast and consistent styling
* Breaking UI into small components improves maintainability
* Separation of layout and logic leads to cleaner code

---

## Final Note

This architecture mirrors real-world frontend systems. As the project grows, new features can be added without affecting existing components, making the codebase easier to maintain and extend.
