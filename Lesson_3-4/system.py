
import os
import sys
import platform

os_name = platform.system()
os_version = platform.release()
python_version = platform.python_version()
work_dir = os.getcwd()
architecture = platform.machine()

results = [
    os_name,
    os_version,
    python_version,
    work_dir,
    architecture
]

menu = """
================================
 LCOS - SYSTEM DIAGNOSTICS
 Lobotomy Corporation
================================
1. Операционная система
2. Версия системы
3. Версия Python
4. Рабочая директория
5. Архитектура компьютера
0. Завершить работу

Выберите операцию: """

while True:
    sys.stdout.write(menu)
    choice = sys.stdin.readline().strip()

    if choice == "0":
        sys.stdout.write("LCOS: Сеанс завершён.\n")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        index = int(choice) - 1

        sys.stdout.write(results[index] + "\n")
    else:
        sys.stdout.write("Ошибка: выберите пункт от 0 до 5.\n")
