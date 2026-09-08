# Poetry Commands

## Start or Configure a Project

```bash
# Create a new project with a package structure.
poetry new project_name

# Initialize Poetry in an existing directory.
cd project_directory
poetry init

# Use Python 3.10 for this project's virtual environment.
poetry env use python3.10

# Keep the virtual environment in the project as .venv/.
poetry config virtualenvs.in-project true --local
```

## Manage Dependencies

```bash
# Add runtime dependencies.
poetry add requests pandas numpy matplotlib

# Add development-only dependencies.
poetry add --group dev flake8 mypy

# Remove a dependency.
poetry remove requests

# Install the dependencies from pyproject.toml and poetry.lock.
poetry install

# Install dependencies without installing this project as a package.
poetry install --no-root

# Resolve versions and update poetry.lock without installing packages.
poetry lock

# Update dependencies within their allowed version ranges.
poetry update
```

## Run and Inspect

```bash
# Run a command in Poetry's virtual environment.
poetry run python loading.py
poetry run flake8
poetry run mypy .

# Open a shell using the virtual environment.
poetry shell

# Show the installed dependency tree.
poetry show --tree

# Show virtual environment information and location.
poetry env info
poetry env info --path
poetry env list
```

## Remove Environments

```bash
# Remove the environment for a specific interpreter.
poetry env remove python3.10

# Remove every Poetry environment for the current project.
poetry env remove --all
```

## Useful Files

```text
pyproject.toml  # Declared dependencies and project configuration.
poetry.lock     # Exact resolved versions; commit this file.
.venv/          # Local virtual environment; do not commit it.
```
