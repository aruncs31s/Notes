---
id: Git_API
aliases: []
tags:
  - coding
  - git
dg-publish: true
---

```go
package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

type Repository struct {
	Fork   bool   `json:"fork"`
	Name   string `json:"name"`
	Parent struct {
		FullName string `json:"full_name"`
	} `json:"parent"`
}

func main() {
	client := &http.Client{}
	req, err := http.NewRequest("GET", "https://api.github.com/repos/aruncs31s/ScrewFast", nil)
	if err != nil {
		log.Fatalf("Error creating request: %v", err)
	}
	req.Header.Add("Accept", "application/vnd.github+json")
	req.Header.Add("X-GitHub-Api-Version", "2022-11-28")

	resp, err := client.Do(req)
	if err != nil {
		log.Fatalf("Error making request: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		log.Fatalf("API request failed with status: %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatalf("Error reading response: %v", err)
	}

	var repo Repository
	err = json.Unmarshal(body, &repo)
	if err != nil {
		log.Fatalf("Error parsing JSON: %v", err)
	}

	// Option 1: Print raw JSON (formatted)
	var prettyJSON map[string]interface{}
	json.Unmarshal(body, &prettyJSON)
	fmt.Println("Available fields:")
	for key := range prettyJSON {
		fmt.Printf("- %s\n", key)
	}
	fmt.Println("\nFormatted JSON:")
	prettyBytes, _ := json.MarshalIndent(prettyJSON, "", "  ")
	fmt.Println(string(prettyBytes))

	if repo.Fork {
		fmt.Printf("Repository '%s' is a fork of '%s'\n", repo.Name, repo.Parent.FullName)
	} else {
		fmt.Printf("Repository '%s' is not a fork\n", repo.Name)
	}
}

```