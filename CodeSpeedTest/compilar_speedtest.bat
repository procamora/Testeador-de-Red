pyinstaller.exe --onefile speedtest_cli.py
rmdir /Q /S build
move dist\speedtest_cli.exe ../
rmdir /Q /S dist
del speedtest_cli.spec