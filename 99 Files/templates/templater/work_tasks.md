
> [!done]- Edited Today
> ```dataview
> LIST  
> FROM ""  
> WHERE file.mtime = date(<% tp.date.now("YYYY-MM-DD", 1) %>)  
> SORT file.mtime DESC
> ```
> 
> Total
> 
> ```dataview
> TABLE length(rows) AS "Notes Modified Today"
> FROM ""
> WHERE file.mtime >= date(<% tp.date.now("YYYY-MM-DD", 1) %>)
> ```




### OverDue



```tasks
not done
due before <% tp.date.now("YYYY-MM-DD", 1) %>
```
### Done Today

```tasks
done on <% tp.date.now("YYYY-MM-DD", 1) %>
```


### Due Today

```tasks
not done
due on <% tp.date.now("YYYY-MM-DD", 1) %>
```




