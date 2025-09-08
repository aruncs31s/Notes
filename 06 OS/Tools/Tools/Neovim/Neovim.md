---
id: Neovim
aliases: []
tags: []
---

# Neovim

- [[#Tricks]]
- [[#Quick Fix List]]
- [[#Sessions]]
- [[#Tabs]]
- [[#Registers]]

- [Good LSPs](#good%20lsps)

#### Good LSPs

- typos_lsp = https://github.com/tekumara/typos-lsp

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

## Tricks

### Shell Commands

It is easy to do things using this way

1. Executing programs

```
:!./program.sh
```

simple, but it is boring to type everytime i want to do this , what if i can simplify this like

```
:!!
```

more convenient, but it requires for me to type the command first
So simplify things further

```vim
vim.api.nvim_set_keymap("n", "<A-q>", ":!!<CR>", { noremap = true, silent = true }),
```

2. Previous Commands

```
q:
```

this will bring up the previously executed commands




### Shell Commands
In one of my projects , when i was running a python script the output of a `print()` was not showing
i was running ![[Flask#^14bd6e]] and this ![[curl POST examples#^00546a]]
![[Pasted image 20250707015515.png]]
But if i run in the terminal 
![[Pasted image 20250707015557.png]]

