---
id: Data View
aliases:
  - data-view
tags: []
---

## Data View

- Dataview consists of two big building blocks: **Data Indexing** and **Data Querying**
- Dataview cannot query all content of your vault. In order to be able to search, filter and display content, this content needs to be _indexed_.
-

#### Fields

##### Inline Fields

_Dataview supports `inline` fields via a `Key::` Value syntax that you can use everywhere in your file. This allows you to write your queryable data right where you need it - for example in the middle of a sentence._

- _If your inline field has an own line, without any content beforehand, you can write it like this:_

```markdown
# Markdown Page

Basic Field:: Some random Value
**Bold Field**:: Nice!
```

_All content after the :: is the value of the field until the next line break._

- _If you want to embed metadata inside sentences, or multiple fields on the same line, you can use the bracket syntax and wrap your field in square brackets:_
  #example

```markdown
I would rate this a [rating:: 9]! It was [mood:: acceptable].
```

- [ ] [Check Out](https://blacksmithgu.github.io/obsidian-dataview/annotation/add-metadata/#inline-fields)


#### References

- https://blacksmithgu.github.io/obsidian-dataview/
- https://dannyhatcher.com/obsidian-dataview-for-beginners/
- https://obsidian.rocks/dataview-in-obsidian-a-beginners-guide/
- https://obsidian.rocks/obsidian-search-five-hidden-features/#embedded-search
-
