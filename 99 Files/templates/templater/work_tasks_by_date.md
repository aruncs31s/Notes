<%*
let theDate = await tp.system.prompt("Date? = ");
%>
> [!done]- Edited Today
> ```dataview
> LIST  
> FROM ""  
> WHERE dateformat(file.mtime, "yyyy-MM-dd") = "<% theDate %>"
> SORT file.mtime DESC
> ```
> 
> Total
> 
> ```dataview
> TABLE length(rows) AS "Notes Modified Today"
> FROM ""
> WHERE dateformat(file.mtime, "yyyy-MM-dd") = "<% theDate %>"
> ```
### OverDue
```tasks
not done
due before <% theDate %>
```
### Done Today
```tasks
done on <% theDate %>
```
### Due Today
```tasks
not done
due on <% theDate %>
```