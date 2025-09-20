---
id: Weechat
aliases: []
tags:
  - os
  - tools
dg-publish: true
---
#Hacks
1. Hide Buffers
	[Source](https://superuser.com/questions/1343608/how-to-hide-weechat-nickname-list-and-channel-names)

```bash
bar toggle nicklist
bar toggle buflist

```

	
	- /set weechat.look.buffer_time_format "" : To hide Timestamps