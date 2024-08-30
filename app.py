import ffmpeg
import os

def create_vr_video(input_file, output_file, zoom_factor=1.1, shift_amount=0.05):
    # Get video properties
    probe = ffmpeg.probe(input_file)
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    width = int(video_info['width'])
    height = int(video_info['height'])

    # Calculate new dimensions after zoom
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    # Calculate crop values
    crop_x = (new_width - width) // 2
    crop_y = (new_height - height) // 2

    # Calculate shift amount in pixels
    shift_pixels = int(width * shift_amount)

    # Process left eye (shifted right)
    left_eye = (
        ffmpeg
        .input(input_file)
        .filter('scale', new_width, new_height)
        .filter('crop', width, height, crop_x + shift_pixels, crop_y)
    )

    # Process right eye (shifted left)
    right_eye = (
        ffmpeg
        .input(input_file)
        .filter('scale', new_width, new_height)
        .filter('crop', width, height, crop_x - shift_pixels, crop_y)
    )

    # Combine left and right eye videos side by side
    output = ffmpeg.filter([left_eye, right_eye], 'hstack', inputs=2)

    # Write output file
    output.output(output_file).overwrite_output().run()

if __name__ == "__main__":
    # Get input file from user
    input_file = input("Enter the path to the input video file: ")
    
    # Validate input file
    while not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        input_file = input("Enter the path to the input video file: ")
    
    # Generate output file name in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "output_vr_video.mp4")
    
    # Get zoom and shift values from user (optional)
    zoom = input("Enter zoom factor (default 1.1, press Enter to use default): ")
    zoom = float(zoom) if zoom else 1.1
    
    shift = input("Enter shift amount as fraction of width (default 0.05, press Enter to use default): ")
    shift = float(shift) if shift else 0.05

    create_vr_video(input_file, output_file, zoom, shift)
    print(f"VR video created: {output_file}")