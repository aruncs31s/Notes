---
title: "<% tp.file.title %>"
description: "<% tp.file.title %>"
tags:
  - ""
cssclasses:
  - wide-page
dg-publish: true
aliases: []
created: 2025-11-04T00:33:55.770908
updated: 2025-11-04T00:33:55.771079
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
> > [!todo]+Tasks
> >
> > ```dataview
> > TASK
> > FROM ""
> > WHERE file.path = this.file.path
> > ```

<% tp.web.daily_quote() %>


## Tasks

- [[06 OS/Tools/Tools/Git/Git]]
