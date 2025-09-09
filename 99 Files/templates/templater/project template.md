---
id: project template
aliases: []
tags:
  - files
  - templates
  - templater
creation_date: <% tp.file.creation_date() %>
github: <% tp.system.prompt("GitHub Repo") %>
modification_date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
project_type: <% tp.system.suggester(["electronics", "linux", "web", "ai/ml", "other"], ["electronics", "linux", "web", "ai/ml", "other"]) %>
dg-publish: true
---
# <% tp.file.title %>

> [!multi-column]+
>
> > [!summary|left-mediam]+ Links
> >
> > ###### Outlinks
> >
> > ```dataview
> > LIST
> > FROM outgoing([[]])
> > ```

> >
> > ###### Sub Notes
> >
> > ```dataview
> > LIST
> > WHERE contains(file.folder, this.file.folder) AND file.name != this.file.name
> > ```

>
> > [!todo]+ Tasks
> >
> > ```dataview
> > TASK
> > FROM ""
> > WHERE file.path = this.file.path
> > ```

<% tp.web.daily_quote() %>

## Tasks

- [[06 OS/Tools/Tools/Git/Git]]
