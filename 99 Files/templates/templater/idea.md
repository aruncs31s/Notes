---
title: "<% tp.file.title %>"
tags:
  - idea
  - etlab
  - brainstorm
cssclasses:
  - wide-page
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
updated: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %> Idea

> [!idea]
> Lightweight brainstorm, investigation, or feature idea for **<% tp.file.title %>**.

## Summary

<% await tp.system.prompt("One-liner summary", "What is this idea about?") %>

## Context / Motivation

<% await tp.system.prompt("Why is this idea useful or needed?", "Background and motivation here") %>

## Key Points
- Point 1: <% await tp.system.prompt("First key point", "") %>
- Point 2: <% await tp.system.prompt("Second key point", "") %>
- Point 3: <% await tp.system.prompt("Third key point", "") %>

## Risks / Constraints
- Risk 1: <% await tp.system.prompt("Potential risk or constraint", "") %>
- Risk 2: <% await tp.system.prompt("Another consideration", "") %>

## Dependencies
- <% await tp.system.prompt("Related issues or ideas", "") %>

## Action Items
- [ ] <% await tp.system.prompt("Next step 1", "Investigate or design") %>
- [ ] <% await tp.system.prompt("Next step 2", "Implement or prototype") %>
- [ ] <% await tp.system.prompt("Next step 3", "Test or review") %>

## Notes / Discussion
<% await tp.system.prompt("Additional notes or discussion points", "") %>

---

_Created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>_