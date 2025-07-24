---
aliases: 
Date: 15-06-2025
tags:
  - python_module
  - python
---
# Position Finder.py
[depends_on:: [ai-robot-position-scraper](https://pypi.org/project/ai-robot-position-scraper/)]
- [[gui.py]]



```dataviewjs
const file = dv.page("03 Coding/Python/01 My Modules/Position Finder.py"); 
if (file && file.file) {
    const content = await dv.io.load(file.file.path); 
    const headings = content.match(/^#+\s.+/gm); 
    if (headings) {
        headings.forEach(heading => {
            const headingText = heading.replace(/^#+\s/, ""); 
            const link = `[[${file.file.name}#${headingText}]]`; 
            dv.paragraph(link); 
        });
    } else {
        dv.paragraph("No headings found.");
    }
} else {
    dv.paragraph("Note not found.");
}
```


