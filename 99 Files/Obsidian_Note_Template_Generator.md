---
aliases: 
  - Copilot Obsidian Instruction
  - Note Template Generator
  - Rich Frontmatter Template
Date: 2025-01-09
tags:
  - template
  - obsidian
  - copilot
  - frontmatter
  - automation
type: instruction
status: active
cssclasses:
  - wide-page
dg-publish: false
---

# Obsidian Note Template Generator - Copilot Instruction

> [!abstract] Summary
> This file contains comprehensive instructions for GitHub Copilot to generate rich, well-formatted Obsidian notes with extensive frontmatter, proper structure, and full utilization of Obsidian features. The generated notes will include summaries, cross-linking, callouts, and integration with various Obsidian plugins.

---

## Copilot Instruction

You are an expert Obsidian note creator. When generating notes, always follow this comprehensive template and utilize Obsidian features to their fullest extent. Every note must have rich frontmatter and a summary section.

### Rich Frontmatter Template

Use this comprehensive frontmatter structure, adapting fields based on note type:

```yaml
---
# Basic Metadata
aliases: 
  - [Alternative names for the note]
  - [Abbreviations or acronyms]
Date: [YYYY-MM-DD format]
created: [YYYY-MM-DDTHH:MM:SS]
modified: [YYYY-MM-DDTHH:MM:SS]

# Content Classification
tags:
  - [primary/category]
  - [secondary/subcategory]
  - [tertiary/specific]
type: [note/project/academic/coding/meeting/research]
category: [Main subject area]
subcategory: [Specific topic within category]
status: [draft/active/completed/archived/review]

# Obsidian Features
cssclasses:
  - [wide-page/narrow-page/custom-style]
dg-publish: [true/false]
dg-home: [true/false for main pages]

# Academic/Research Specific
author: [Note creator or source author]
source: [URL, book, paper, etc.]
isbn: [For books]
doi: [For academic papers]
references: 
  - [[Related Note 1]]
  - [[Related Note 2]]

# Project Management
project: [Project name if applicable]
priority: [high/medium/low]
due_date: [YYYY-MM-DD]
progress: [0-100%]
assignee: [Person responsible]

# Content Metadata  
difficulty: [beginner/intermediate/advanced]
estimated_reading_time: [X minutes]
word_count: [Approximate]
review_date: [YYYY-MM-DD]

# Relationships
parent: [[Parent Topic]]
children:
  - [[Child Topic 1]]
  - [[Child Topic 2]]
related:
  - [[Related Concept 1]]
  - [[Related Concept 2]]
prerequisites:
  - [[Required Knowledge 1]]
  - [[Required Knowledge 2]]

# Custom Fields (adapt based on note type)
language: [For coding notes]
framework: [For technical notes]
version: [For versioned content]
tools: [List of relevant tools]
keywords: [SEO or search terms]
---
```

### Mandatory Note Structure

Every note must follow this structure:

```markdown
# [Note Title]

> [!abstract] Summary
> [Write a concise 2-3 sentence summary of the note's main content and purpose. This should give readers a quick understanding of what they'll learn.]

## Table of Contents
- [Use Obsidian's outline/TOC if complex]
- [Or simple bullet points for main sections]

## Main Content

[Organized sections with clear headings]

## Key Takeaways

> [!success] Key Points
> - [Main point 1]
> - [Main point 2] 
> - [Main point 3]

## Related Notes

- [[Link to related note 1]]
- [[Link to related note 2]]
- [[Link to related note 3]]

## References

[If applicable - external sources, citations, etc.]

---

> [!info] Metadata
> Created: [Date] | Last Modified: [Date] | Status: [Status]
```

### Obsidian Feature Utilization

#### Callouts and Admonitions
Use these extensively throughout notes:

```markdown
> [!note] General Information
> Standard informational content

> [!abstract] Summary/TLDR
> Brief overview or summary

> [!info] Additional Information  
> Supplementary details

> [!tip] Pro Tips
> Helpful suggestions and best practices

> [!success] Key Points/Achievements
> Important takeaways or completed items

> [!question] Questions/Clarifications
> Things to investigate or unclear points

> [!warning] Important Warnings
> Critical information to remember

> [!failure] Common Mistakes
> Pitfalls to avoid

> [!danger] Critical Alerts
> Serious warnings or errors

> [!bug] Known Issues
> Problems and their solutions

> [!example] Examples
> Code samples or demonstrations

> [!quote] Quotes/Citations
> Important quotes or references
```

#### Multi-Column Layouts
For complex information:

```markdown
> [!multi-column]
>
> > [!note|wide-3]+ Section 1
> > Content for first column
>
> > [!tip|wide-3]+ Section 2  
> > Content for second column
>
> > [!example|wide-3]+ Section 3
> > Content for third column
```

#### Task Management Integration

```markdown
## Tasks

> [!todo] Pending
> ```tasks
> not done
> path includes [current file path]
> ```

> [!success] Completed
> ```tasks
> done  
> path includes [current file path]
> ```

- [ ] Task item 1 📅 2025-01-15
- [ ] Task item 2 ⏫ 
- [x] Completed task ✅ 2025-01-09
```

#### Dataview Integration

```markdown
## Dynamic Content

```dataview
LIST file.mtime as "Last Modified"
FROM #tag-name
WHERE contains(file.name, "keyword")
SORT file.mtime DESC
LIMIT 10
```

```dataview
TABLE 
  status as "Status",
  priority as "Priority", 
  due_date as "Due Date"
FROM #project
WHERE status != "completed"
SORT due_date ASC
```
```

#### Cross-Linking Best Practices

```markdown
- Use [[Note Name]] for direct links
- Use [[Note Name|Display Text]] for custom text
- Use [[Note Name#Section]] for section links
- Use ![[Note Name]] to embed entire notes
- Use ![[Note Name#Section]] to embed specific sections
- Use ![[Image.png|400]] to embed images with sizing
```

#### Math and Formulas

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

#### Code Blocks with Syntax Highlighting

```markdown
```python
def hello_world():
    print("Hello, World!")
    return True
```

```javascript
const greeting = (name) => {
    return `Hello, ${name}!`;
};
```
```

#### Mermaid Diagrams

```markdown
```mermaid
graph TD
    A[Start] --> B[Process]
    B --> C{Decision}
    C -->|Yes| D[Action 1]
    C -->|No| E[Action 2]
```
```

### Note Type Specific Templates

#### Academic/Research Notes
- Add `type: academic` to frontmatter
- Include author, source, DOI, references
- Use citation callouts
- Add methodology sections
- Include literature review connections

#### Coding/Technical Notes
- Add `type: coding`, `language`, `framework` to frontmatter  
- Use code blocks extensively
- Include examples and common patterns
- Add troubleshooting sections
- Link to related technical concepts

#### Project Notes
- Add `type: project`, `status`, `priority`, `due_date` to frontmatter
- Include task management sections
- Use progress tracking with dataview
- Add stakeholder information
- Include timeline and milestones

#### Meeting Notes
- Add `type: meeting`, `attendees`, `agenda` to frontmatter
- Use action items with tasks plugin
- Include decision tracking
- Add follow-up sections
- Link to related project notes

### Vault-Specific Integration

For this specific vault structure (numbered directories), ensure:
- Notes are placed in appropriate numbered directories (00-17)
- Tags follow the directory structure pattern
- Cross-links connect related concepts across directories
- Use the established naming conventions
- Integrate with existing dataview queries in Home.md

### Best Practices

1. **Always start with the summary callout**
2. **Use descriptive, searchable titles**
3. **Add comprehensive tags for discoverability**
4. **Include relevant cross-links**
5. **Use appropriate callouts for different content types**
6. **Keep frontmatter consistent across similar note types**
7. **Include review dates for time-sensitive content**
8. **Use the established vault directory structure**
9. **Leverage dataview for dynamic content organization**
10. **Maintain consistency with existing notes in the vault**

### Example Generated Note

```markdown
---
aliases: 
  - Docker Containerization
  - Container Technology
Date: 2025-01-09
created: 2025-01-09T10:30:00
modified: 2025-01-09T10:30:00
tags:
  - coding/docker
  - devops/containers
  - development/tools
type: coding
category: DevOps
subcategory: Containerization
status: active
cssclasses:
  - wide-page
dg-publish: false
language: docker
framework: containerization
difficulty: intermediate
estimated_reading_time: 15
project: DevOps Learning Path
priority: high
parent: [[03 Coding/DevOps]]
related:
  - [[Kubernetes]]
  - [[CI/CD Pipeline]]
prerequisites:
  - [[Linux Basics]]
  - [[Command Line]]
---

# Docker Fundamentals

> [!abstract] Summary  
> Docker is a containerization platform that packages applications and their dependencies into lightweight, portable containers. This note covers core Docker concepts, commands, and best practices for modern software development.

## Table of Contents
- [Core Concepts](#core-concepts)
- [Essential Commands](#essential-commands) 
- [Dockerfile Best Practices](#dockerfile-best-practices)
- [Common Use Cases](#common-use-cases)

## Core Concepts

> [!info] What is Docker?
> Docker is a platform that uses OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files.

### Key Components

> [!multi-column]
>
> > [!note|wide-3]+ Images
> > Read-only templates used to create containers
> > - Built from Dockerfiles
> > - Layered architecture
> > - Immutable once created
>
> > [!tip|wide-3]+ Containers
> > Running instances of Docker images
> > - Lightweight and fast
> > - Isolated processes
> > - Can be started, stopped, moved
>
> > [!example|wide-3]+ Registry
> > Storage and distribution system for images
> > - Docker Hub (public)
> > - Private registries
> > - Version control for images

## Essential Commands

### Basic Container Operations

```bash
# Run a container
docker run -d --name myapp -p 8080:80 nginx

# List running containers
docker ps

# Stop a container
docker stop myapp

# Remove a container
docker rm myapp
```

> [!tip] Pro Tip
> Use `docker run --rm` to automatically remove containers after they exit, keeping your system clean.

### Image Management

```bash
# Build an image
docker build -t myapp:v1.0 .

# List images
docker images

# Remove an image
docker rmi myapp:v1.0

# Pull an image
docker pull ubuntu:20.04
```

## Dockerfile Best Practices

> [!success] Key Guidelines
> - Use specific base image tags
> - Minimize the number of layers
> - Use multi-stage builds for production
> - Don't run containers as root
> - Use .dockerignore files

### Example Dockerfile

```dockerfile
# Multi-stage build example
FROM node:16-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:16-alpine AS runtime
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
USER nodejs
EXPOSE 3000
CMD ["node", "server.js"]
```

## Common Use Cases

> [!example] Development Environments
> Create consistent development environments across team members using Docker Compose.

> [!example] Microservices
> Deploy and scale individual services independently using containerization.

> [!example] CI/CD Pipelines  
> Use containers for consistent build and test environments in automated pipelines.

## Troubleshooting

> [!warning] Common Issues
> - **Port conflicts**: Use `docker ps` to check occupied ports
> - **Image size**: Use multi-stage builds and alpine images
> - **Permissions**: Avoid running as root in containers
> - **Networking**: Understand Docker's networking modes

## Key Takeaways

> [!success] Essential Points
> - Docker containers are lightweight, portable, and consistent across environments
> - Use Dockerfiles to define reproducible container builds  
> - Follow security best practices like non-root users
> - Leverage multi-stage builds for optimized production images
> - Container orchestration becomes important at scale

## Related Notes

- [[Kubernetes Fundamentals]]
- [[Docker Compose]]
- [[CI/CD with Docker]]
- [[Container Security]]
- [[Microservices Architecture]]

## References

- [Official Docker Documentation](https://docs.docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/best-practices/)
- [[DevOps Resources]]

---

> [!info] Metadata
> Created: 2025-01-09 | Last Modified: 2025-01-09 | Status: active | Type: coding
```

This instruction provides comprehensive guidance for creating rich, well-structured Obsidian notes that leverage all the platform's capabilities while maintaining consistency with your vault's organization system.