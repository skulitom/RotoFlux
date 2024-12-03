import ffmpeg
import os

def extract_frames(input_video_path, output_folder, fps=None):
    """
    Extract frames from a video file.
    
    Args:
        input_video_path (str): Path to input video file
        output_folder (str): Path to output folder for frames
        fps (float, optional): Frames per second to extract. If None, extracts all frames
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    try:
        # Get video information
        probe = ffmpeg.probe(input_video_path)
        video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
        
        # Build the ffmpeg command
        stream = ffmpeg.input(input_video_path)
        
        # Add fps filter if specified
        if fps:
            stream = ffmpeg.filter(stream, 'fps', fps=fps)
            
        # Output to PNG sequence
        stream = ffmpeg.output(stream, 
                             os.path.join(output_folder, 'frame_%06d.png'),
                             format='image2',
                             **{'qscale:v': 2})  # High quality images
        
        # Run the command
        ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)
        
        print(f"Frames extracted successfully to {output_folder}")
        
    except ffmpeg.Error as e:
        print('An error occurred: ', e.stderr.decode())
        raise

if __name__ == "__main__":
    # Example usage
    input_video = "input.mp4"
    output_folder = "frames"
    
    # Extract frames at 30 fps
    extract_frames(input_video, output_folder, fps=30) 