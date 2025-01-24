# **Security CLI**

A small personal project designed to showcase and test scripting skills. This CLI tool includes functionality for generating secure passwords and scanning ports.

---

## **Features**
- 🔑 **Password Generator**: Quickly generate secure passwords.
- 🔍 **Port Scanner**: Scan for open ports on a target system.

---

## **Dependencies**
Ensure the following are installed before running the script:
1. **Python**: Version `>= 3.9`
2. **Figlet**: For ASCII art (optional but recommended).
   - Install via your package manager:
     ```bash
     sudo apt install figlet  # For Debian-based systems
     ```
3. **Required Python Libraries**:
   - Install using `pip`:
     ```bash
     pip3 install -r requirements.txt
     ```

---

## **How to Use**

### **Password Generator**
Generate a secure password:
```bash
./sec-cli pass_gen
# or
./sec-cli -p
```

### **Port Scanner**
Scan ports for a given target:
```bash
./sec-cli scan
# or
./sec-cli -s
```

---

## **Examples**

1. **Generate a Password**:
   ```bash
   ./sec-cli -p
   ```

2. **Run a Port Scan**:
   ```bash
   ./sec-cli scan
   ```

---

## **Pre-commit Tutorial**
This project uses `pre-commit` to ensure code quality and consistency. Follow these steps to set it up:

### **Install Pre-commit**
1. Install the `pre-commit` package:
   ```bash
   pip install pre-commit
   ```

2. Install the hooks defined in the `.pre-commit-config.yaml` file:
   ```bash
   pre-commit install
   ```

3. Run `pre-commit` on all files to ensure they pass:
   ```bash
   pre-commit run --all-files
   ```

### **Pre-commit Configuration**
Here is the `.pre-commit-config.yaml` used in this project:
```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.9.2
  hooks:
    # Run the linter.
    - id: ruff
    # Run the formatter.
    - id: ruff-format
```

### **How It Works**
- **Ruff**: This configuration uses `Ruff` for linting and formatting Python code.
- Every time you commit code, `pre-commit` will automatically run these hooks to ensure your code meets the project's standards.

---

## **Future Improvements**
This is a work in progress. Planned improvements include:
- Adding support for more CLI tools.
- Enhancing the user interface.
- Adding more configuration options for port scanning and password generation.

---

