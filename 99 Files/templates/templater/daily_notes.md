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

<< [[Timestamps/<% tp.date.now("YYYY", -1) %>/<% tp.date.now("MM-MMMM", -1) %>/<% tp.date.now("DD-MM-YYYY", -1) %>|Yesterday]] | [[Timestamps/<% tp.date.now("YYYY", 1) %>/<% tp.date.now("MM-MMMM", 1) %>/<% tp.date.now("DD-MM-YYYY", 1) %>|Tomorrow]] >>

---

## Tasks Done

```tasks
done on <% tp.date.now("YYYY-MM-DD") %>

```

## 📅 Daily Questions

##### 🙌 One thing I'm excited about right now is...

-

##### 🚀 One+ thing I plan to accomplish today is...

- [ ]

##### 👎 One thing I'm struggling with today is...

- ***

## 📝 Notes

- <% tp.file.cursor() %>

---

### Notes created today

```dataview
List FROM "" WHERE file.cday = date("<%tp.date.now("YYYY-MM-DD")%>") SORT file.ctime asc

```

### Notes last touched today

```dataview
List FROM "" WHERE file.mday = date("<%tp.date.now("YYYY-MM-DD")%>") SORT file.mtime asc

```
