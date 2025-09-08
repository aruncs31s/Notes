---
id: Embedded Systems Website
aliases: 
tags:
  - project
  - website
  - es_website
  - "#main_page"
cssclasses:
  - wide-page
Status: Active
dg-publish: true
---

# ES Website


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
date: 2025-10-9 00:00:00
to: プロジェクトを完了する 🎉
completedLabel: プロジェクトを完了する 🎉
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


## Introduction 
This project aims to develop a website where , GCEK Embedded Systems students can show case their projects and hopefully products that they develop in the future. 
So what do you need , if you are planning to contribute read the [[#Contribute Section]] 
## Contribution
Contribution might be the hardest that me can ask. But also the beautiful thing , because you will never learn things if you don't try , and always remember to grow , you don't have to remember it you will do that eventually. This all might sound like some gimic , i don't know how to convince otherwise. 
As i have said contribution might be the hardest because , 
1. You have to learn , Astro , [[React]] , Javascript , and HTML + CSS and Tailwind. 
**what i have to say about it.**
I don't know any of it , except JS ,HTML , CSS , so how can i do this?. The obvious answer would be to use chatgpt.

>[!Note] **Note on ChatGPT**
>Using AI tools like , ChatGPT , Gemini , Claude etc..  is ok but there are some problems which comes with it if you don't know how to use it. 
>1. You will get codebanged , which means the codebase will become , so large that you might use complex design patterns to implement simple functions and use of outdated libraries. 
>2. You will lose the ability to read , and understand the code. **Why?**
>It has to do with how to learn code, by using what i've learned over the years , that you learn code mostly by doing, so you have to get your hands dirty, think of it like 
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



## Login Feature 

