# ft_package

A simple Python package that counts occurrences of an item in a list.

## Example
```python
from ft_package import count_in_list
print(count_in_list(["a", "b", "a"], "a"))  # ➜ 2
```


# 🧰 Manual Build & Install Guide (No Makefile Needed)

This guide walks you through building, installing, and testing your Python package manually, using Python 3.10 and a virtual environment.

## 🧼 Step 1: Clean Everything

Remove all previously generated files, caches, and the virtual environment.

```bash
rm -rf dist build *.egg-info venv
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete
python3.10 -m pip uninstall -y ft_package
```

### 🧽 This deletes:
Build artifacts (dist/, build/)Metadata (*.egg-info)Python cache filesVirtual environment (venv/)Uninstalls the package ft_package if it was installed globally
## 🐍 Step 2: Create Virtual Environment
```bash
python3.10 -m venv venv
```

### 🔒 This isolates your environment so dependencies don't leak into your system Python.
## 📦 Step 3: Install Build Tools Inside Virtualenv
```bash
venv/bin/pip install --upgrade pip setuptools wheel build
```

### 🛠️ These tools are required to build your package:
setuptools and wheel handle packagingbuild triggers the actual package build
## 🏗️ Step 4: Build Your Package
```bash
venv/bin/python3.10 -m build
```

### 📦 This creates:
dist/ft_package-0.0.1.whl → wheel distributiondist/ft_package-0.0.1.tar.gz → source distribution
## 📥 Step 5: Install the Wheel
```bash
venv/bin/pip install $(ls dist/*.whl | head -n 1)
```

### ✅ Installs the generated .whl file directly into your virtual environment.
## ✅ Step 6: Run Your Test Script
```bash
venv/bin/python3.10 tester.py
```

### 🧪 Verifies the installation by running your tester.py file.
## 🧾 Full Command Summary
Copy-paste this to go from scratch to test in one go:
```bash
rm -rf dist build *.egg-info venv
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete
python3.10 -m pip uninstall -y ft_package

python3.10 -m venv venv
venv/bin/pip install --upgrade pip setuptools wheel build
venv/bin/python3.10 -m build
venv/bin/pip install $(ls dist/*.whl | head -n 1)
```
