import os
from pathlib import Path

ROOT = Path('./')
FILE = Path('./name_to_files.txt')
exercises = {}


for root, dirs, files in os.walk(ROOT):
    
    for file in files:
        if 'venv' in root:
            continue
        if dirs:
            continue
        if file.endswith('.py'):
            file_name = Path(root, file)
            with open(file_name, 'r', encoding='UTF-8') as opened_file:
                for idx, line in enumerate(opened_file):
                    if line.startswith('* Assignment'):
                        name = line[13:].strip()
                        exercises.setdefault(root[2:], []).append((name, file))
                    if idx > 0:
                        break

with open(FILE, 'w') as f:
    for subject, names in exercises.items():
        f.write(f'{subject}\n')
        f.write('-' * len(subject) + '\n')
        names.sort()
        for name, file in names:
            f.write(f'\t{name} - {file}\n')
        f.write('\n\n')

