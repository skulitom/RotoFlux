@echo off
REM Navigate to the FFmpeg directory (adjust path if necessary)
cd /d "path\to\ffmpeg"

REM Execute the FFmpeg command
..\bin\ffmpeg -framerate 30 -i "..\intermediate\output_frame_%%04d.jpeg" -c:v libx264 -pix_fmt yuv420p "..\out\out.mp4"

REM Notify user of completion
echo Video creation completed.
pause