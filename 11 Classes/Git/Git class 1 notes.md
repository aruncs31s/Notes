---
id: Git_class_1_notes
aliases: []
tags:
  - classes
  - git
dg-publish: true
---
# Git Class 1 Notes 

## Creating Alices Game
1. Goto https://github.com/aruncs31s?tab=repositories
2. Create new Repo  ![[crate repo.png]]
![[alices game.png]]

![[click create repocitory.png]]

3. Clone the repository 

```bash
cd ~/Class/Alice
git clone https://github.com/aruncs31s/alice-s-game
cd alice-s-game

```

4. Create new game 

```python
class Game1:
	def level_1(args):
		...
	def items():
		...
	def characters:
		...

```

5. Add that game to git 

```bash
git add game.py 
git push origin main

```

6. Send the link to alice 

## John Obtaining the game 

```bash
cd ~/Class/John/
git clone https://github.com/aruncs31s/alice-s-game
cd alice-s-game

```

- Check the game

```bash
ls 

```

https://f-droid.org/en/packages/com.termux/