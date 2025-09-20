---
id: Obsidian Project Widget
aliases: []
tags:
  - projects
  - linux
  - conky
  - obsidian_project_widget
Status: 
dg-publish: true
---
# Obsidian Project Widget

## Features

- [ ] List Projects from my vault
- [ ] categorize projects according to their status

Status = {Done , Acticve , Dropped}

```python
files = get_md_files(notes_dir)
    for root, file in zip(files[0], files[1]):# root and file_name
        file_path = os.path.join(root, file)  
        print(file_path)

```

## Coding
#### Searching For `#project`
Searching for `#project` in a file is will also select any file that uses `#project` tag , for example a `dataview` query may contain `#project` tag .

So in order to do that ,
1. extract a specific part

```

---
// properties
---

```

more specifically the properties of files. which start with `---` and ends with `---`
