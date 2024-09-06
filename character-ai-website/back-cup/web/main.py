import os
import platform

device_name = platform.system()

print("trước khi chạy hãy nhớ đặt ip máy chủ vào phần ALLOW_HOST trong file setting.py \
nếu muốn trang web đâm ra ngoài mạng.")

inp = input("chạy local hay công khai? : ").lower().strip()

if inp in ["local", "cục bộ"] and device_name in "Windows":
    os.system("python ./ai_character/manage.py runserver")
else:
    os.system("python3 ./ai_character/manage.py runserver")

if inp in ["public", "công khai"] and device_name in "Windows":
    os.system("python ./ai_character/manage.py runserver 0.0.0.0")
else:
    os.system("python3 ./ai_character/manage.py runserver 0.0.0.0")