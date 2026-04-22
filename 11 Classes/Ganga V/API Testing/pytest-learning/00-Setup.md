---
id: 00-Setup
tags:
  - pytest
  - setup
  - installation
  - virtual-environment
dg-publish: true
---

# Setup & Installation

This guide covers setting up `pytest` for your development environment.

## Why Use a Virtual Environment?

A **virtual environment** is an isolated Python environment that keeps your project dependencies separate from other projects and your system Python.

### Problems Without Virtual Environments

```
Project A needs: django==3.0
Project B needs: django==4.0

System Python has: django==2.0  ❌ Conflict!
```
So its better to separate these two.


### With Virtual Environments

```
Project A venv: django==3.0   ✅
Project B venv: django==4.0   ✅
System Python: django==2.0    ✅
```

### Benefits

- **Isolation** - Each project has its own dependencies
- **No conflicts** - Different projects can use different versions
- **Clean system** - System Python stays untouched
- **Reproducible** - Easy to share requirements
- **Easy cleanup** - Delete venv folder to remove everything

---

## Installation Steps

### 1. Create a Project Directory

```bash
mkdir pytest-demo
cd pytest-demo
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

The `venv` is just a folder name (you can name it anything):

```bash
python3 -m venv .venv       # Common
python3 -m venv env       # Short
python3 -m venv myenv     # Custom
```

### 3. Activate the Environment

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**After activating, you'll see the venv name in your terminal:**
```
(venv) user@computer:~/pytest-demo$
```

### 4. Install pytest

```bash
pip install pytest
```

### 5. Verify Installation

```bash
pytest --version
```

Expected output:
```
pytest 8.x.x
```

### 6. Deactivate When Done

```bash
deactivate
```

---

## Managing Dependencies

### Install Multiple Packages

```bash
pip install pytest requests pytest-cov
```

### Save Dependencies

```bash
pip freeze > requirements.txt
```

This creates a file with all installed packages and versions.

### Install from Requirements

```bash
pip install -r requirements.txt
```

### Requirements.txt Example

```
pytest==8.0.0
requests==2.31.0
pytest-cov==4.1.0
```

---

## Common Issues

| Issue | Solution |
|-------|----------|
| pytest: command not found | Activate venv or use `python -m pytest` |
| Permission denied | Use `pip install --user pytest` |
| Wrong Python version | Use `python3` explicitly |
| Already exists | Use `--upgrade` or delete existing venv |

---

## Quick Reference

| Command | Description |
|---------|-----------|
| `python3 -m venv venv` | Create venv |
| `source venv/bin/activate` | Activate (Linux/Mac) |
| `venv\Scripts\activate` | Activate (Windows) |
| `deactivate` | Deactivate |
| `pip install pytest` | Install pytest |
| `pip freeze > requirements.txt` | Save dependencies |
| `pip install -r requirements.txt` | Install from file |

---

## Best Practices

1. **Always use a venv** - Never install packages globally
2. **One venv per project** - Keeps things isolated
3. **Add venv to .gitignore** - Don't commit venv folder
4. **Keep requirements.txt** - For reproducibility

### .gitignore Entry

```
# .gitignore
venv/
.env/
*.pyc
__pycache__/
```

---

## Using with Different Tools

### VS Code

1. Activate venv
2. Select Python interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter"

### PyCharm

1. File → Settings → Project → Python Interpreter
2. Click gear → Add → Existing venv

### Jupyter

```bash
pip install ipykernel
python -m ipykernel install --user --name=venv
```

---

**Next:** [[01-First-Test]] - Write your first test

**See Also:** [[python/python]] - Python reference