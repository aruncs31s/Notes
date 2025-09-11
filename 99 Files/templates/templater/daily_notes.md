---
id: daily_notes
aliases: []
tags:
  - files
  - templates
  - templater
created: <% tp.file.creation_date() %>
dg-publish: true
---
tags:: [[+Daily Notes]]

# <% moment(tp.file.title,'YYYY-MM-DD').format("dddd, MMMM DD, YYYY") %>

← [[<% tp.date.now("YYYY-MM-DD", -1) %>|Yesterday]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>|Tomorrow]] →

---

## 📋 Tasks

### Today's Tasks
```tasks
not done
due on <% tp.date.now("YYYY-MM-DD") %>
```

### Completed Today
```tasks
done on <% tp.date.now("YYYY-MM-DD") %>
```

## 📅 Daily Reflection

##### 🙌 What am I excited about today?

- 

##### 🎯 What do I want to accomplish today?

- [ ] 
- [ ] 
- [ ] 

##### 🤔 What challenges am I facing?

- 

##### 🌟 What am I grateful for?

- 

## 📝 Notes

<% tp.file.cursor() %>

---

## 📊 Today's Activity

### Notes Created Today
```dataview
LIST
FROM ""
WHERE file.cday = date("<% tp.date.now("YYYY-MM-DD") %>")
SORT file.ctime ASC
```

### Notes Modified Today
```dataview
LIST
FROM ""
WHERE file.mday = date("<% tp.date.now("YYYY-MM-DD") %>") AND file.cday != date("<% tp.date.now("YYYY-MM-DD") %>")
SORT file.mtime DESC
```

---
*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
