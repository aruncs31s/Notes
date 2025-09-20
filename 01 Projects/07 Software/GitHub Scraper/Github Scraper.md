---
id: Github_Scraper
aliases: []
tags:
  - projects
  - software
  - gitub_scraper
dg-publish: true
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
	Github-->>Scraper: SEND INITIATE Request 
	Scraper-->>Github: Scrape README.md
	Scraper-->>Scraper: convert to required format. 
	Scraper-->>Github: download attachements
	Scraper-->>FrontEnd Server: Initiate Update
	FrontEnd Server-->>FrontEnd Server: create backup of the current state
	FrontEnd Server-->> Scraper: SEND INITIATE 
	Scraper-->>FrontEnd Server: send the updated data
	FrontEnd Server-->>FrontEnd Server: Update the site. 

```

![[Pasted image 20250710015226.png]]

## Scraping Github 

