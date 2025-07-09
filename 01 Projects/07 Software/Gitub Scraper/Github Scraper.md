---
tags:
  - project
  - software
---

# Github Scraper

> [!check]+ **Things Done**
> - [ ] d

There is now huge confusion in whether i should scrape the `README.md` file or just create a `ci/cd` (`github automation`) pipeline so that , i dont have to do the polling mechanism instead i can just create some form of tocken mechanism and let the `github automation` update each project when an update is pushed.

### Current mechanism 
```mermaid
sequenceDiagram
	participant User
	participant Github
	participant Scraper

	User->>Github: Create/Update Pushes a commit 
	Github-->>Github: check if there is version increment
	Github->>Scraper: SEND INITIATE Request 
	Scraper-->>Github: Update Project Info
```



![[Pasted image 20250710015226.png]]




## Scraping Github 


