# Repository Structure — itsnishant089

This document explains the purpose of every file in this GitHub profile repository.

## Why This Repository Exists

GitHub has a special feature: if you create a repository with the **exact same name as your username**, the `README.md` in that repository is rendered on your GitHub profile page. This repository (`itsnishant089/itsnishant089`) is that special profile repository.

---

## File Map

### `README.md`
**Purpose:** The centerpiece of the entire profile. This file renders directly on `github.com/itsnishant089`. It contains the full visual profile including hero banner, about section, projects, skills, stats, and more. Written in GitHub-flavored Markdown with embedded HTML and SVG references.

### `svg/profile.svg`
**Purpose:** The animated hero banner displayed at the top of the profile. Built as a self-contained SVG with CSS animations, SVG filters (blur, glow, drop shadows), terminal-style UI chrome, ASCII art, and a matrix rain background. This is the visual centerpiece that creates the first impression.

### `svg/avatar.svg`
**Purpose:** An ASCII-art terminal portrait that replaces a traditional profile photo. Rendered entirely in SVG with monospace text, terminal window chrome, and a blinking cursor animation. No raster images are used.

### `svg/terminal.svg`
**Purpose:** A simulated Linux terminal session that tells the viewer about Nishant through familiar CLI commands like `whoami`, `cat about.txt`, `ls projects/`, and `git status`. Includes line-by-line reveal animations and a blinking cursor.

### `svg/techstack.svg`
**Purpose:** An animated grid of technology cards showing the full tech stack. Each card uses glassmorphism-style SVG filters and subtle glow animations. Technologies are grouped by category: Languages, Frontend, Backend, and Tools.

### `svg/achievements.svg`
**Purpose:** A vertical timeline of hackathon wins and key achievements. Each entry is a glass-styled card with neon connectors, animated entry effects, and award indicators. Covers Orbix, Evolothon, HACKRUST, and Technophilia wins.

### `assets/background.svg`
**Purpose:** An animated matrix-style falling character background. Uses CSS keyframes to animate vertical text columns. Intended as a visual element that can be referenced or embedded.

### `assets/grid-pattern.svg`
**Purpose:** A cyberpunk-style perspective grid overlay. Adds depth and visual texture when layered behind content. Uses subtle opacity to avoid overwhelming foreground elements.

### `assets/noise-texture.svg`
**Purpose:** An SVG noise texture generated with `feTurbulence`. Provides the subtle grain effect used in glassmorphism designs. Referenced as a filter in other SVGs.

### `assets/glow-effect.svg`
**Purpose:** A reusable neon glow effect built with SVG filters (`feGaussianBlur` + `feComposite`). Can be referenced by other SVGs to apply consistent glow styling.

### `assets/icons/terminal-icon.svg`
**Purpose:** A custom terminal prompt icon matching the cyberpunk theme. Used in README sections and SVG compositions.

### `assets/icons/code-icon.svg`
**Purpose:** A code brackets icon (`< >`) for the skills and projects sections.

### `assets/icons/link-icon.svg`
**Purpose:** An external link arrow icon for project links and social connections.

### `.github/workflows/update.yml`
**Purpose:** GitHub Actions workflow that runs on a daily schedule. It generates the contribution graph snake animation using `Platane/snk` and commits the output to a `dist/` branch. This keeps dynamic visual elements up to date without manual intervention.

### `docs/STRUCTURE.md`
**Purpose:** This file. Documents the repository structure and explains why each file exists, making the project maintainable and understandable for contributors or future reference.
