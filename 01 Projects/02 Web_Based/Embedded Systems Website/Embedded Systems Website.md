---
id: Embedded Systems Website
aliases: 
tags:
  - project
  - website
  - es_website
cssclasses:
  - wide-page
Status: Active
dg-publish: true
---

# ES Website


> [!tldr]- Test
> what



>[!SUMMARY]- Table of Contents
>- [[Embedded Systems Website#ES Website|ES Website]]
>    - [[Embedded Systems Website#Features Need|Features Need]]
>    - [[Embedded Systems Website#Structure|Structure]]
> [!blank|right-small]
>
> - [[01 UI]]
>   - [[01 Projects/02 Web_Based/Embedded Systems Website/Home Page]]
>   - [[Projects Page]]
> - [[02 Login Feature]]

```widgets
type: countdown
date: 2025-08-9 00:00:00
to: Complete the Project 🎉
completedLabel: Project is done 🎉
```

> [!summary]+ Lauch Workspace
>
> ```bash
> cd ~/Projects/es_website_gcek/ && alacritty -e tmux new-session -A -s  Website
> ```

> [!multi-column]+ Git
>
> > [!Todo]- **Check for Update**
> >
> > ```bash
> > export PROJECT_DIR=~/Projects/es_website_gcek/
> > cd $PROJECT_DIR && git status
> > ```
>
> > [!important]- **Update**
> >
> > - update
> >
> > ```bash
> > export PROJECT_DIR=~/Projects/es_website_gcek/
> > cd $PROJECT_DIR
> > git add -A
> > git commit -m "update"
> > git push origin main
> > ```

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
