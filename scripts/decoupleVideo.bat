@echo off
REM Navigate to the FFmpeg directory (adjust path if necessary)
cd /d "path\to\ffmpeg"

REM Execute the FFmpeg command
..\bin\ffmpeg -i "..\in\in.mp4" -vf "fps=30" "..\intermediate\output_frame_%%04d.jpeg"

REM Notify user of completion
echo Frame extraction completed.
pause