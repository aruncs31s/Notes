---
dg-publish: true
banner: "09 Projects/Common/banner.jpg"
banner_y: 0.432
cssclasses:
  - wide-page
banner_x: 0.49653
---


# Taks
**Todays Tasks**
>[!multi-column]
>
>>[!Important] Just do 
>>```tasks
>>not done 
>>path includes Projects 
>>not done
>>due on today
>>
>>```
>
>>[!Important] Completed Tasks
>> ```tasks
>> done
>> path includes Projects
>> due on today
>>```
>[!float|right-small]
>```dataview
>LIST
>from #project 
>
>```


**This Month**
>[!multi-column]
>
>>[!Important] Just do 
>>```tasks
>>not done 
>>path includes Projects 
>>not done
>>happens in this month
>>
>>```
>
>>[!Important] Completed Tasks
>> ```tasks
>> done
>> path includes Projects
>> happens in this month
>>```




**Total**






```tasks
not done 
path includes Projects 
not done
```



# Projects

```dataview
Table  
Date.Started as Start ,Date.End as End , date(now) as "Remaining"
FROM #project


SORT file.mtime DESC

```

```dataview
TABLE 
date(now). as KK
FROM #project



```