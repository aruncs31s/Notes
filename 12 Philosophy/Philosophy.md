---
aliases: 
Date: 12-10-2024
---
# Philosophy

## Linux
- [tmux](#tmux)
>On [[Linux]] all keybindings should match between applications and all bindings should make sense.
I mainly use `i3`, `tmux` ,`neovim` , `vimium` , `zen` , `obsidian` etc...whose workflow is entirely depends on the keybindings 


### Tmux
I mainly use tmux because it is more convenient to just **one** terminal , because opening too many terminal is a mess.

**Plugins i use on a daily basis**:
```bash
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'christoomey/vim-tmux-navigator'
set -g @plugin 'sainnhe/tmux-fzf
```
**tmux-fzf**: 
This is the most used plugin among this and
```bash
bind -n M-S run-shell "/home/aruncs/.tmux/plugins/tmux-fzf/scripts/pane.sh switch"
bind -n M-s run-shell "/home/aruncs/.tmux/plugins/tmux-fzf/scripts/session.sh switch"
bind -n M-f run-shell "/home/aruncs/.tmux/plugins/tmux-fzf/main.sh"
```
These are the bindings 
1. `M-S` which is the `Alt+Shift+s` -> which opens a small floating windows i which i can select which opened `pane` that is want to switch with
2.  

## Study 
- What is important is what assemptions in the problem leads to conclusion.
- Something becomes simple after you understand it -> It is not simple because  you dont understand 
- 