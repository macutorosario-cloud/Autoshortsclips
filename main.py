python
import subprocess

def cortar_video(input_file, output_file, start_time, duration):
command = [
"ffmpeg",
"-i",
input_file,
"-ss",
start_time,
"-t",
duration,
"-c",
"copy",
output_file,
]
subprocess.run(command)
cortar_video("input.mp4", "output_clip.mp4", "00:01:00", "00:00:30")
