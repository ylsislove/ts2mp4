@echo off

python main.py

ffmpeg.exe -f concat -safe 0 -i .\result.txt -c copy output.mp4

pause