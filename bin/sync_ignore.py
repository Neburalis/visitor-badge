#!/usr/bin/env python3

import os

SYNC_START_MARKER = '# Synced from .gitignore'
SYNC_END_MARKER = '# End of synced content'

def read_ignore(file_path):
    lines = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
    return lines

def remove_synced_part(dockerignore_content):
    clean_content = []
    in_synced_section = False
    for line in dockerignore_content:
        if line.strip() == SYNC_START_MARKER:
            in_synced_section = True
            continue
        if line.strip() == SYNC_END_MARKER:
            in_synced_section = False
            continue
        if not in_synced_section:
            clean_content.append(line)
    return clean_content

def main():
    gitignore_path = ".gitignore"
    dockerignore_path = ".dockerignore"

    gitignore_lines = read_ignore(gitignore_path)
    dockerignore_content = remove_synced_part(read_ignore(dockerignore_path))

    # Подготавливаем строки для добавления
    append_lines = [SYNC_START_MARKER, '# Do not edit the section below']

    # Собираем существующие записи из .dockerignore для проверки
    existing_entries = [line.strip() for line in dockerignore_content if line.strip() and not line.strip().startswith('#')]

    for line in gitignore_lines:
        stripped_line = line.strip()
        if stripped_line in existing_entries:
            # Строка уже есть в .dockerignore, комментируем её
            append_lines.append('# ' + line.rstrip('\n'))
        else:
            # Строки нет в .dockerignore, добавляем как есть
            append_lines.append(line.rstrip('\n'))

    append_lines.append(SYNC_END_MARKER)
    append_lines.append("")

    # Записываем обновлённый .dockerignore
    with open(dockerignore_path, 'w') as f:
        f.writelines(dockerignore_content)
        # Если файл не оканчивается переносом строки, добавим его
        if dockerignore_content and not dockerignore_content[-1].endswith('\n'):
            f.write('\n')
        f.write('\n'.join(append_lines))
        f.write('\n')

    print(f"[INFO] Синхронизация '{gitignore_path}' с '{dockerignore_path}' завершена.")

if __name__ == '__main__':
    main()
