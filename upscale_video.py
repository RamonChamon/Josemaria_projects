from moviepy.editor import VideoFileClip

# 👉 Replace this with the path to your original video file
input_path = "Who is Josemaría Escriva_ What is Opus Dei_.mp4"
output_path = "Who_is_Josemaria_Escriva_1080p.mp4"

# Load the video
clip = VideoFileClip(input_path)

# Resize to 1080p (maintains aspect ratio)
clip_resized = clip.resize(height=1080)

# Export the video with audio
clip_resized.write_videofile(output_path, codec="libx264", audio_codec="aac")

print("✅ Upscale complete! Saved to:", output_path)
