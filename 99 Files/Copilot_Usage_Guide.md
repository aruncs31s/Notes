---
aliases: 
  - Copilot Usage Guide
  - Template Instructions
Date: 2025-01-09
tags:
  - guide
  - copilot
  - template
  - obsidian
type: documentation
status: active
cssclasses:
  - wide-page
dg-publish: false
---

# Obsidian Rich Frontmatter Generator - Usage Guide

> [!abstract] Summary
> This guide explains how to use the Copilot instruction files to generate rich, well-formatted Obsidian notes with comprehensive frontmatter and full feature utilization.

## 📁 Available Files

### Main Files

1. **[[Obsidian_Note_Template_Generator]]** - Comprehensive instruction with detailed examples
2. **[[Copilot_Quick_Instruction]]** - Concise, copy-paste ready prompt
3. **This Guide** - Usage instructions and tips

## 🚀 Quick Start

### Method 1: Copy-Paste Instruction

1. Open [[Copilot_Quick_Instruction]]
2. Copy the instruction block 
3. Open GitHub Copilot Chat
4. Paste the instruction
5. Add your topic: "Create a note about [YOUR TOPIC]"

### Method 2: Reference the Full Template

1. Reference [[Obsidian_Note_Template_Generator]] for detailed examples
2. Ask Copilot: "Based on the Obsidian template in this vault, create a note about [YOUR TOPIC]"
3. Copilot will analyze the comprehensive template and generate accordingly

## 📋 Example Prompts

> [!example] Academic Notes
> ```
> Using the Obsidian template, create an academic note about:
> - Quantum mechanics principles
> - Machine learning algorithms
> - Economic theories
> ```

> [!example] Coding Notes
> ```
> Generate a coding note about:
> - Python data structures
> - React component patterns
> - Database normalization
> ```

> [!example] Project Notes
> ```
> Create a project note for:
> - Web development portfolio
> - Mobile app development
> - Research project planning
> ```

## 🎯 Generated Note Features

### Rich Frontmatter Includes:
- **Basic metadata**: aliases, dates, tags
- **Content classification**: type, category, status
- **Obsidian features**: CSS classes, publish settings
- **Relationships**: parent, children, related notes
- **Project management**: priority, progress, due dates
- **Academic fields**: author, source, DOI, references

### Obsidian Features Used:
- **Callouts**: Multiple types for different content
- **Cross-linking**: Extensive use of `[[]]` syntax
- **Dataview**: Dynamic content queries
- **Tasks**: Integrated task management
- **Multi-column**: Complex layouts
- **Code blocks**: Syntax highlighting
- **Math notation**: Inline and block formulas
- **Embedded content**: Images, diagrams, notes

## 🔧 Customization Tips

### Adapting for Different Note Types

> [!tip] Academic Notes
> - Include DOI, ISBN, citation information
> - Add methodology sections
> - Use more references and cross-links
> - Include review dates

> [!tip] Coding Notes  
> - Add language and framework fields
> - Include version information
> - Use extensive code examples
> - Add troubleshooting sections

> [!tip] Project Notes
> - Include stakeholder information
> - Add timeline and milestones
> - Use task management features
> - Include progress tracking

### Vault-Specific Adaptations

The templates are designed for this vault's structure:
- **Numbered directories** (00-17) for main content
- **Special directories** (90+) for utilities
- **Existing tagging** patterns and conventions
- **Integration** with Home.md dataview queries

## 📊 Quality Checklist

Before saving generated notes, verify:

> [!success] Frontmatter
> - [ ] All relevant fields completed
> - [ ] Tags follow hierarchical structure
> - [ ] Dates in correct format (YYYY-MM-DD)
> - [ ] Cross-links to related notes included

> [!success] Content Structure
> - [ ] Summary callout at the top
> - [ ] Clear section headings
> - [ ] Appropriate callouts used
> - [ ] Key takeaways section included
> - [ ] Related notes section populated

> [!success] Obsidian Features
> - [ ] Cross-links use correct syntax
> - [ ] Callouts are properly formatted
> - [ ] Code blocks have syntax highlighting
> - [ ] Tasks use proper format with dates
> - [ ] Math formulas render correctly

## 🛠️ Troubleshooting

### Common Issues

> [!warning] Frontmatter Problems
> - **Missing dashes**: Ensure `---` at start and end
> - **Incorrect syntax**: Check YAML formatting
> - **Invalid dates**: Use YYYY-MM-DD format
> - **Missing fields**: Add relevant metadata

> [!warning] Linking Issues
> - **Broken links**: Ensure target notes exist
> - **Incorrect syntax**: Use `[[Note Name]]` format
> - **Missing aliases**: Add alternative names for findability

### Performance Tips

> [!tip] Optimization
> - Use tags strategically (not too many)
> - Keep frontmatter relevant (remove unused fields)
> - Regular cleanup of outdated cross-links
- Utilize dataview queries for dynamic content

## 📈 Best Practices

### Content Creation Workflow

1. **Plan the note** - Determine type, category, and purpose
2. **Use the instruction** - Copy appropriate template
3. **Generate content** - Let Copilot create the structure
4. **Customize** - Adapt for specific needs
5. **Review** - Check against quality checklist
6. **Link** - Add cross-references to related notes
7. **Tag** - Apply appropriate hierarchical tags

### Maintenance

> [!note] Regular Tasks
> - Update modification dates when editing
> - Review and update related links
> - Check for outdated information
> - Maintain consistent tagging
> - Use dataview to find orphaned notes

## 🎉 Advanced Usage

### Creating Note Series

For related topics, use consistent:
- Naming conventions
- Tag hierarchies  
- Cross-linking patterns
- Frontmatter structure

### Integration with Plugins

The templates work well with:
- **Dataview**: For dynamic queries and organization
- **Tasks**: For todo management
- **Templater**: For even more automation
- **Calendar**: For date-based organization
- **Excalidraw**: For diagrams and sketches

## 📚 Examples

See the test file created: `/tmp/test_react_hooks_note.md` for a complete example of what the template generates.

---

> [!success] You're Ready!
> With these instructions and templates, you can now generate rich, well-structured Obsidian notes that fully utilize the platform's capabilities while maintaining consistency with your vault's organization system.

## Related Notes

- [[Obsidian_Note_Template_Generator]]
- [[Copilot_Quick_Instruction]]
- [[Home]]
- [[Obsidian Best Practices]]

---

> [!info] Metadata
> Created: 2025-01-09 | Last Modified: 2025-01-09 | Status: active | Type: documentation