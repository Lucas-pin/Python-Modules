# venv and pip Commands

## Create and Activate an Environment

```bash
# Create an isolated environment in the current project.
python3 -m venv .venv

# Activate it on Linux or macOS.
source .venv/bin/activate

# Confirm that the environment's Python and pip are active.
which python
which pip
python --version
python -m pip --version

# Leave the active environment.
deactivate
```

## Manage Packages

```bash
# Update pip in the active environment.
python -m pip install --upgrade pip

# Install packages.
python -m pip install requests pandas numpy matplotlib

# Install a fixed version or a version range.
python -m pip install "requests==2.32.3"
python -m pip install "pandas>=2.0,<3.0"

# Upgrade or uninstall a package.
python -m pip install --upgrade requests
python -m pip uninstall requests

# Inspect installed packages.
python -m pip list
python -m pip show requests
```

## Save and Recreate Dependencies

```bash
# Export the exact packages installed in the active environment.
python -m pip freeze > requirements.txt

# Install the packages listed in requirements.txt.
python -m pip install -r requirements.txt
```

## Typical Workflow

```bash
cd project_directory
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python loading.py
deactivate
```

## Useful Files

```text
requirements.txt  # Installed packages and their versions; commit this file.
.venv/            # Local virtual environment; do not commit it.
```