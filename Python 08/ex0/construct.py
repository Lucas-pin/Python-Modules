#!/usr/bin/env python3
from sys import version_info, prefix, base_prefix
import os
import site

virtual_env: bool = (prefix != base_prefix)
construct_welcome: str = "You 're still plugged in"
virtual_welcome: str = "Welcome to the construct"
py_version = f"{version_info.major}.{version_info.minor}.{version_info.micro}"

unix_cmd: str = "'source <environment name>/bin/activate' # On Unix"
windows_cmd: str = "'<environment name>\\Scripts\\activate' # On Windows"
create_venv: str = "python -m venv <environment name>"

venv_path = os.environ.get('VIRTUAL_ENV', 'N/A')
venv_name = os.path.basename(venv_path)
print("MATRIX STATUS: "
      f"{virtual_welcome if virtual_env else construct_welcome}\n")

print(f"Current Python: {py_version}")

print("Virtual Enviroment: "
      f"{venv_name if virtual_env else 'None detected'}")

if (virtual_env):
    print(f"Enviroment Path: {venv_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print(site.getusersitepackages())

else:
    unix_so: bool = True if os.name == 'posix' else False
    activation_cmd: str = f"{unix_cmd if unix_so else windows_cmd}"

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print(f"If you havne't created a virtual env yet, execute {create_venv}")
    print(f"followed by {activation_cmd}")
    print(f"Otherwise, just run: {activation_cmd}")
    print("Then run this program again.")
