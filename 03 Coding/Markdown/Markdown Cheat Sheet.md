# Markdown Cheat Sheet

This is a comprehensive cheat sheet for Markdown syntax. Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents.

## Headers

Use `#` symbols to create headers. The number of `#` symbols determines the header level.

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

## Emphasis

You can add emphasis by making text **bold** or *italic*.

```markdown
**Bold text**
*Italic text*
***Bold and italic text***
```

## Lists

### Unordered Lists

Use `-`, `*`, or `+` to create unordered lists.

```markdown
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3
```

### Ordered Lists

Use numbers followed by a period.

```markdown
1. First item
2. Second item
   1. Subitem 2.1
   2. Subitem 2.2
3. Third item
```

## Links

Create links using `[link text](URL)`.

```markdown
[GitHub](https://github.com)
[Link with title](https://example.com "Optional title")
```

## Images

Similar to links, but with an exclamation mark `!` at the beginning.

```markdown
![Alt text](image-url.jpg)
![Alt text](image-url.jpg "Optional title")
```

## Code

### Inline Code

Use backticks `` ` `` to create inline code.

```markdown
Use the `print()` function in Python.
```

### Code Blocks

Use triple backticks ``` for code blocks. You can specify the language for syntax highlighting.

```markdown
```python
def hello_world():
    print("Hello, World!")
ww```
```

## Blockquotes

Use `>` to create blockquotes.

```markdown
> This is a blockquote.
>
> It can span multiple lines.
```

## Tables

Create tables using pipes `|` and hyphens `-`.

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |
```

## Horizontal Rules

Use three or more hyphens `---`, asterisks `***`, or underscores `___`.

```markdown
---
```

## Line Breaks

End a line with two spaces or use a backslash `\` for a line break.

```markdown
First line  
Second line

First line\
Second line
```

## Escaping Characters

Use backslashes `\` to escape special characters.

```markdown
\*Not italicized\*
```

## Task Lists

Use `- [ ]` for unchecked tasks and `- [x]` for checked tasks.

```markdown
- [ ] Task 1
- [x] Task 2
- [ ] Task 3
```

## Footnotes

Create footnotes using `[^1]` and define them at the bottom.

```markdown
This is a sentence with a footnote.[^1]

[^1]: This is the footnote.
```

## Strikethrough

Use double tildes `~~` to strikethrough text.

```markdown
~~Strikethrough text~~
```

## Highlighting

Some platforms support highlighting with `==`.

```markdown
==Highlighted text==
```

## Mathematical Expressions

Use `$` for inline math and `$$` for display math (requires MathJax or similar).

```markdown
Inline math: $E = mc^2$

Display math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

## HTML

You can use HTML tags directly in Markdown.

```markdown
<p>This is a paragraph.</p>
```

## Comments

Use HTML comments `<!-- -->` for comments that won't appear in the rendered output.

```markdown
<!-- This is a comment -->
```

## Reference-Style Links

Define links separately and reference them.

```markdown
[Link text][ref]

[ref]: https://example.com
```

## Automatic Links

URLs and email addresses are automatically converted to links.

```markdown
https://github.com
user@example.com
```

## Emojis

Use emoji shortcodes or Unicode.

```markdown
:smile: or 😀
```

## Abbreviations

Some Markdown processors support abbreviations.

```markdown
*[HTML]: HyperText Markup Language
```

## Definition Lists

Use `:` for definition lists.

```markdown
Term 1
: Definition 1

Term 2
: Definition 2
```

## Keyboard Shortcuts

Use `<kbd>` tags for keyboard shortcuts.

```markdown
Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.
```

## Subscripts and Superscripts

Use HTML tags `<sub>` and `<sup>`.

```markdown
H<sub>2</sub>O
E = mc<sup>2</sup>
```

## Fenced Code Blocks with Attributes

Specify attributes for code blocks.

```markdown
```python {linenos=true}
def hello():
    print("Hello")
```
```

## Tables with Alignment

Align columns in tables.

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| A    | B      | C     |
```

## Collapsible Sections

Some platforms support collapsible sections.

```markdown
<details>
<summary>Click to expand</summary>
Hidden content here.
</details>
```

This cheat sheet covers the most common Markdown features. Different platforms (like GitHub, GitLab, or various editors) may support additional extensions or have slight variations in syntax.
