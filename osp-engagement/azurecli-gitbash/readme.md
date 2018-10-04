# Installing Azure CLI within Gitbash
To install Azure Cli within Gitbash

1. Update the default version of pip
```bash
python -m pip install --upgrade pip
```
2. Install Azure CLI
```bash
pip install --user azure-cli
```
This will take a few minutes and will throw some warnings that should be ignored.
3. Put in the install directory in PATH
```bash
#Edit .bashrc
export PATH=/c/Users/<YourUsername>/AppData/Roaming/Python/Python36/Scripts:$PATH
```
4. Exit and let gitbash configure .bash_profile
5. Confirm install dirorty is within the path
```bash
$ which az
/c/Users/alhussai/AppData/Roaming/Python/Python36/Scripts/az
```