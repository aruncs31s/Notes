---
dg-publish: true
banner: "09 Projects/Common/banner.jpg"
banner_y: 0.552
cssclasses:
  - wide-page
banner_x: 0.49653
---
# Projects

```dataview
Table alias as Nick , Date.Started as Started , Date.Target as Target , Date.End as End , Status.Working_ON as "State"  ,  Status.Completed as "Complete" , Status.isStall as "Stall"
FROM #project
SORT file.mtime DESC 

```

## How to structure a project well 
**Example Structure**
```
dg-publish: true
id: 29-11-2024-Project
aliases:
  - Smart Watch
tags:
  - project,embedded
Date:
  Started: 29-11-2024
  Target: 01-01-2025
  End:
Status:
  isStall: false
  Working_ON: true
  Completed: false
github: https://github.com/aruncs31s/Smart-Watch-for-Ladies-Protection
cssclasses:
  - wide-page
```

```dataview 
Table  
From #project and #iot
```
```dataview
Table 
file.ctime as "Created" , Date.Started as "Started" , Date.Target as "Completed"
Where file = this.file
```
### Single ton project 
```yaml
Date
  Started: DD-MM-YYYY
  Target: DD-MM-YYYY
  End: DD-MM-YYYY
```

- They Should contain their working github repo as 
```
github:
  - github.com/repolink
```