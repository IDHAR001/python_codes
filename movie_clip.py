from moviepy.editor import VideoFileClip  
  
video = VideoFileClip("/Users/zhangzhicong/Downloads/1032825891_da2-1-16.mp4")  
audio = video.audio  
audio.write_audiofile("/Users/zhangzhicong/Downloads/真的爱你.mp3")