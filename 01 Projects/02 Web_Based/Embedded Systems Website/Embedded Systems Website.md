---
id: Embedded Systems Website
aliases: 
tags:
  - project
  - website
dg-publish: true
---

# Website
- [[01 UI]]

- [[02 Login Feature]]

## Features Need

- [x] Login Feature
- Students should be able to showcase the projects

@end Features

- [ ] make a local store website

## Structure

@begin Structure

```
src/
├── assets/
│   ├── scripts/          # JS scripts
│   └── styles/           # CSS styles
├── components/           # Reusable components
│   ├── Meta.astro        # Meta component for SEO
│   ├── sections/         # Components for various sections of the website
│   ├── ThemeIcon.astro   # Component for toggling light/dark themes
│   └── ui/               # UI components categorized by functionality
├── content/              # Markdown files for blog posts, insights, products, and site configuration
│   ├── blog/
│   ├── docs/
│   ├── insights/
│   └── products/
├── data_files/           # Strings stored as JSON files
├── images/               # Static image assets for use across the website
├── layouts/              # Components defining layout templates
│   └── MainLayout.astro  # The main wrapping layout for all pages
├── pages/                # Astro files representing individual pages and website sections
│   ├── 404.astro         # Custom 404 page
│   ├── blog/
│   ├── fr/               # Localized content
│   ├── contact.astro
│   ├── index.astro       # The landing/home page
│   ├── insights/
│   ├── products/
│   ├── robots.txt.ts     # Dynamically generates robots.txt
│   └── services.astro
├── utils/                # Shared utility functions and helpers
└── content.config.ts     # Contains content collections configuration options
```

@end Structure
