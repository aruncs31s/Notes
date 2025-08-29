---
id: Home
aliases: 
tags: 
dg-publish: true
cssclasses:
  - wide-page
---

# HOME
- [[Projects]]

```widgets
type: quote
quote: When you stare into the abyss, the abyss stares back at you.
```


## Tasks 

![[Cal_mon_friday.excalidraw|1000x300]]

```dataview
CALENDAR due
WHERE typeof(due) = "date"
```


```tasks
path includes 98 Private/Todo.md

```

```todoist
filter: "today | overdue"
```

> [!todo] Just DO
>
> ```tasks
> not done
> due on today
> ```



> [!note] Completed
>
> ```tasks
> done
> due on today
> ```

---

> [!multi-column]
>
> > [!note|wide-3]+ Projects
> >
> > ```dataview
> > List file.mtime
> > FROM #project
> > LIMIT 7
> > ```
>
> > [!float|wide-3]+ Notes
> >
> > ```dataview
> > LIST file.mtime
> > SORT file.mtime DESC
> > LIMIT 7
> > ```

- [ ] Checkout [Adding Metadata to your Pages](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/) 📅 2025-04-17

## Work 

```tasks
not done 
path includes Work/
```

## Startups 



## Files 
```dataview
CALENDAR file.ctime
```

> [!IMPORTANT]- **Keep It up to date**
>
> > [!NOTE]- **Windows**
> >
> > ```python
> > import os as win
> > win.system("cd C:/Users/arunc/Git/Notes && dir && git pull origin main")
> > ```
>
> > [!NOTE]- **Linux**
> >
> > ```bash
> > cd /home/aruncs/Notes/ && git add -A ; git commit -m "automated backup" ; git push origin main
> > ```




