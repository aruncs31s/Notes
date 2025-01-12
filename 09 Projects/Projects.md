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
Table aliases as Nick , Date.Started as Started , Date.Target as Target , Date.End as End , Status.Working_ON as "State"  , Status.Completed as isComplete 
FROM #project
```
## How to structure a project well 
### Single ton project 
- They should contain `starting date` and `target date` and when they are finished in the format 
```yaml
Date
  Started: DD-MM-YYYY
  Target: DD-MM-YYYY
  End: DD-MM-YYYY
```
