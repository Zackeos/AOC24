import shutil

for i in range(2, 25+1):
    shutil.copy('day-template.py', f'day{i}.py')
    with open(f'day{i}.py', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('day = today.day', f'day = {i}')
    with open(f'day{i}.py', 'w') as file:
        file.write(filedata)
    print(f'Created day{i}.py')
