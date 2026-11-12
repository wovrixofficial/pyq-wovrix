with open('syllabus/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="blueprintContainer"' in l:
        for j in range(i, min(i+40, len(lines))):
            print(f'{j+1}: {lines[j]}', end='')
        break
