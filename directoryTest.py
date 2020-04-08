from pathlib import Path

path = Path() #current path
for file in path.glob('*'):
    print(file)

#glob method to search for files and directories in the current path
#the aterisk means everything: *.py --> every python file in path