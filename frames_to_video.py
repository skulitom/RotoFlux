import ffmpeg
import os

def create_video_from_frames(input_folder, output_video_path, fps=30, codec='libx264'):
    """
    Create a video from a sequence of PNG frames.
    
    Args:
        input_folder (str): Path to folder containing PNG frames
        output_video_path (str): Path for output video file
        fps (int): Frames per second for output video
        codec (str): Video codec to use
    """
    try:
        # Build the ffmpeg command
        stream = ffmpeg.input(os.path.join(input_folder, 'frame_%06d.png'),
                            pattern_type='sequence',
                            framerate=fps)
        
        # Configure video encoding settings
        stream = ffmpeg.output(stream,
                             output_video_path,
                             vcodec=codec,
                             pix_fmt='yuv420p',  # Standard pixel format for compatibility
                             **{'crf': 23,       # Constant Rate Factor (18-28 is good)
                                'preset': 'medium'})  # Encoding speed preset
        
        # Run the command
        ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)
        
        print(f"Video created successfully: {output_video_path}")
        
    except ffmpeg.Error as e:
        print('An error occurred: ', e.stderr.decode())
        raise

if __name__ == "__main__":
    # Example usage
    input_folder = "frames"
    output_video = "output.mp4"
    
    # Create video at 30 fps
    create_video_from_frames(input_folder, output_video, fps=30) 