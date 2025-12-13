import sys
import platform
print("--- Проверка системы ---")
print(f"Версия Python: {sys.version}")
print(f"Операционная система: {platform.system()} {platform.release()}")
print("Всё работает!")