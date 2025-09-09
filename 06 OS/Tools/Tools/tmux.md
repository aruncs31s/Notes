---
id: tmux
aliases: []
tags:
  - os
  - tools
dg-publish: true
---
# TMUX 

#git [Github](https://github.com/tmux/tmux)

[[i3]] Like Keybindings

#Keybinding

## **Keybindings**

- I'm Using **`Ctrl + b`** (default Leader) as my leader key or **`prefix`** and i will use **`^`** to denote Control.
- And i Use **`M`** to denote _`Alt`_

- **_Navigation_**

| Combination | Used                |
| ----------- | ------------------- |
| M-Left      | Select Left Pane    |
| M-h         | Select Left Pane    |
| M-Right     | Select Right Pane   |
| M-l         | Select Right Pane   |
| M-Down      | Select Bottom Pane  |
| M-j         | Select Bottom Pane  |
| M-Up        | Select Top Pane     |
| M-k         | Select Top Pane     |
| Shift-Left  | Select Left Window  |
| Shift-Right | Select Right Window |

- **_Spliting_**

| Combination | Used               |
| ----------- | ------------------ |
| M-v         | Split Vertically   |
| M-g         | Split Horizontally |

\*You can also use default `^b + "` and `^b + %` to split

- **workflow**

| Combination | Used             |
| ----------- | ---------------- |
| M-1         | Move to Window 1 |
| M-2         | Move to Window 2 |
| M-3         | Move to Window 3 |
| M-4         | Move to Window 4 |
| M-5         | Move to Window 5 |
| M-6         | Move to Window 6 |
| M-7         | Move to Window 7 |
| M-8         | Move to Window 8 |
| M-9         | Move to Window 9 |

| Combination | Used               |
| ----------- | ------------------ |
| M-c         | New-Window         |
| M-r         | Rotate Window      |
| M-z         | Toggle Zoom        |
| M-t         | Toggle Clock       |
| M-w         | Window Chooser     |
| M-f         | tmux-fzf           |
| M-s         | Create New Session |

#wholeCode

```bash
# Do not close when detaching
set-option -g detach-on-destroy off
# set-option -sa terminal-overrides ",xterm*:Tc"
# set -g default-terminal "screen-256color"
set -g default-terminal "xterm-256color"
set-option -ga terminal-overrides ",xterm-256color:Tc"
# Start windows and panes at 1, not 0
set -g base-index 1

set -g pane-base-index 1

set-window-option -g pane-base-index 1

set-option -g renumber-windows on

# Enable Mouse Support
set -g mouse on

# Zoom selected pane

bind -n M-z resize-pane -Z

# Open Clock
bind -n M-t clock-mode

# Rotate window
bind -n M-r rotate-window

## Splitting Windows
bind -n M-v splitw
bind -n M-g splitp -h

# Windoe chooser

bind -n M-w choose-window

# reload the config
bind C-r source ~/.tmux.conf

# Create New Window
bind -n M-c neww

# Create New Session
bind -n M-x new-session

### open obsidian with default file
bind -n M-n display-popup -E "nvim ~/obsidian-vault/Linux/Linux/Linux.md"

# Switch to fav session
bind -n M-o new-session -A -s Obsidian
bind -n M-p new-session -A -s Git

# Toggle the Status bar
bind -n M-u set -g status off
bind -n M-U set -g status on

# Vim style pane selection

# bind h select-pane -L
# bind j select-pane -D
# bind k select-pane -U
# bind l select-pane -R
#

# Use Alt-arrow keys without prefix key to switch panes
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D
bind -n M-h select-pane -L
bind -n M-l select-pane -R
bind -n M-k select-pane -U
bind -n M-j select-pane -D

# Shift arrow to switch windows
bind -n S-Left  previous-window
bind -n S-Right next-window

# Shift Alt vim keys to switch windows
bind -n M-H previous-window
bind -n M-L next-window

# Plugins
# set -g @plugin 'wfxr/tmux-fzf-url'
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'christoomey/vim-tmux-navigator'
set -g @plugin 'sainnhe/tmux-fzf'

### i3 Like Window Switching

bind -n M-1 select-window -t 1
bind -n M-2 select-window -t 2
bind -n M-3 select-window -t 3
bind -n M-4 select-window -t 4
bind -n M-5 select-window -t 5
bind -n M-6 select-window -t 6
bind -n M-7 select-window -t 7
bind -n M-8 select-window -t 8
bind -n M-9 select-window -t 9
bind -n M-0 select-window -t 10

#### catppuccin
# By https://github.com/omerxx/dotfiles/blob/master/tmux/tmux.conf

set -g @plugin 'omerxx/catppuccin-tmux'
set -g @catppuccin_flavour 'mocha'
set -g @catppuccin_window_left_separator ""
set -g @catppuccin_window_right_separator " "
set -g @catppuccin_window_middle_separator " █"
set -g @catppuccin_window_number_position "right"
set -g @catppuccin_window_default_fill "number"
set -g @catppuccin_window_default_text "#W"
set -g @catppuccin_window_current_fill "number"
set -g @catppuccin_window_current_text "#W#{?window_zoomed_flag,(),}"
set -g @catppuccin_status_modules_right "directory date_time"
set -g @catppuccin_status_modules_left "session"
set -g @catppuccin_status_left_separator  " "
set -g @catppuccin_status_right_separator " "
set -g @catppuccin_status_right_separator_inverse "no"
set -g @catppuccin_status_fill "icon"
set -g @catppuccin_status_connect_separator "no"
set -g @catppuccin_directory_text "#{b:pane_current_path}"
# set -g @catppuccin_meetings_text "#($HOME/.config/tmux/scripts/cal.sh)"
set -g @catppuccin_date_time_text "%H:%M"

bind -n M-f run-shell "~/.tmux/plugins/tmux-fzf/main.sh"
bind -n M-s run-shell "/home/aruncs/.tmux/plugins/tmux-fzf/scripts/session.sh switch"

# bind -n M-f run "fzf-tmux"

TMUX_FZF_LAUNCH_KEY="C-f"

run '~/.tmux/plugins/tpm/tpm'

set -g status-position top

# set vi-mode
set-window-option -g mode-keys vi
# keybindings
bind-key -T copy-mode-vi v send-keys -X begin-selection
bind-key -T copy-mode-vi C-v send-keys -X rectangle-toggle
bind-key -T copy-mode-vi y send-keys -X copy-selection-and-cancel

## match the working directory of new pane to current one
bind '"' split-window -v -c "#{pane_current_path}"
bind % split-window -h -c "#{pane_current_path}"

```

#### Tmux Litle hacks

source : https://aliquote.org/post/tmux-little-hacks/

```bash
bind-key -n M-q display-menu -x W -y S \
    "New Session"                        S "command-prompt -p \"New Session:\" \"new-session -A -s '%%'\"" \
    "Kill Session"                       x "kill-session" \
    "Kill Other Session(s)"              X "kill-session -a" \
    "" \
    "New Window"                         ␍ new-window \
    "Kill Window"                        k "killw"  \
    "Choose Window"                      w choose-window \
    "Previous Window"                    🡠 previous-window \
    "Next Window"                        🡢 next-window \
    "Swap Window Right"                  ↑ "swap-window -t -1" \
    "Swap Window Left"                   ↓ "swap-window -t +1" \
    "Horizontal Split"                   v "split-window -h" \
    "Vertical Split"                     s "split-window -v"  \
    "" \
    "Layout Horizontal"                  h "select-layout even-horizontal"  \
    "Layout Vertical"                    k "select-layout even-horizontal"  \
    "" \
    "Swap Pane Up"                       < "swap-pane -U" \
    "Swap Pane Down"                     > "swap-pane -D" \
    "Break Pane"                         t break-pane \
    "Join Pane"                          j "choose-window 'join-pane -h -s \"%%\"'" \
    "#{?window_zoomed_flag,Unzoom,Zoom}" z "resize-pane -Z"

```

```bash
bind-key -n M-! split-window -f -l 10 -c "#{pane_current_path}"
bind-key -n M-: command-prompt
bind-key -n M-< swap-pane -U
bind-key -n M-= choose-buffer
bind-key -n M-> swap-pane -D
bind-key -n M-D choose-client
bind-key -n M-Down swap-window -t +1
bind-key -n M-Enter new-window
bind-key -n M-Left previous-window
bind-key -n M-O switch-client -l
bind-key -n M-S command-prompt -p "New Session:" "new-session -A -s '%%'"
bind-key -n M-Right next-window
bind-key -n M-Up swap-window -t -1
bind-key -n M-k select-layout even-vertical
bind-key -n M-j choose-window 'join-pane -h -s "%%"'
bind-key -n M-h select-layout even-horizontal
bind-key -n M-l last-window
bind-key -n M-m command-prompt -p "Search man pages for:" "new-window 'exec man %%'"
bind-key -n M-o selectp -t :.+
bind-key -n M-p run "tmux split-window -p 10 'tmux send-keys -t #{pane_id} \"$(locate ~/ | fzf -m | paste -sd\\  -)\"'"
bind-key -n M-s split-window -v
bind-key -n M-t break-pane
bind-key -n M-v split-window -h
bind-key -n M-w choose-window
# bind-key -n M-x confirm-before -p "kill-pane #P? (y/n)" kill-pane
bind-key -n M-y copy-mode
bind-key -n M-z resize-pane -Z

```

#### Frequently Used

1. Change current working dir

```bash
:attach-session -t . -c new_working_dir

```
