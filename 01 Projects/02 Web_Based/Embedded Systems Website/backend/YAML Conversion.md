---
tags:
  - es_website
  - backend
  - idea_1
---
# YAML Conversion
So the initial idea is to conver a standard readme into a YAML frontmatter format that can be used in a static site component in our [[Embedded Systems Website]] 

Core Idea:

Read the README.md file content.

Parse the Markdown to extract headings, paragraphs, lists, and images.

Map these extracted components to the specific keys in your desired YAML frontmatter structure (e.g., title, description, main.content, longDescription.subTitle, specificationsLeft, tableData, etc.).

Generate the YAML frontmatter string.

Combine the YAML frontmatter with any remaining Markdown content (if any, though your example suggests all content is in frontmatter).