---
id: Neovim
aliases: []
tags: []
---

# Neovim

- [[#Quick Fix List]]
- [[#Sessions]]
- [[#Tabs]]
- [[#Registers]]

### Contents

- [Good LSPs](#good%20lsps)

#### Good LSPs

- typos_lsp = https://github.com/tekumara/typos-lsp

##### Astronvim 4 Migration

###### Links

- https://github.com/aruncs31s/Astronvim_config_new
-

#### Buffer

- close buffer -> `bd`

#### Quick Fix List

[Source](https://youtu.be/AuXZA-xCv04?si=N08Jwg8wmCDbs7-G)

- `copen` to access quickfix list
- or i can do telescope search through everyfile for a current word and add it to quick list by pressing `Ctrl+Q`

##### Navigation

| Key        | Doing    |
| ---------- | -------- |
| <Leader>qn | next fix |
| qp         | Previous |

###### Search and Replace

```bash
cdo s/something/tosomething | update
```

## Keybindings

1. Increment and Decrement an integer

```
Control + A -> Increment
Control + X -> Decrement
```

2. To increment incrementing order

- Select the lines using `Ctrl+V` or `v  + j`
- Then type `g Ctrl + A `

#### Sessions

- Saving sessions

```bash
:mksession <session_name>.vim
```

To open the saved session

```bash
source <session_name>.vim
```

#### Tabs

1. Move the current window to a new tab

```bash
Ctrl+w T
```

#### Registers

1. Copy to a Register

```vim
"ay
```

Registers: There are named registers like `a-z` and numbers `0-9`
`0` -> last copied text
`1-9` -> last deleted texts
