import moviepy
from moviepy.editor import AudioFileClip
# import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

audio = input("输入要提取的视频源文件（包括后缀）：")
voice = input("输入要转化成的文件名（包括后缀）：")
my_audio = AudioFileClip(audio)
my_audio.write_audiofile(voice)