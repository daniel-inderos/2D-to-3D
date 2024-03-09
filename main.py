import cv2

# Open the input video
cap = cv2.VideoCapture('input_video.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_vr.mp4', fourcc, fps, (width*2, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame
    resized_frame = cv2.resize(frame, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)

    # Crop left and right parts
    left_frame = resized_frame[int(0.05*height):int(1.05*height), 0:width]
    right_frame = resized_frame[0:height, int(0.2*width):int(1.2*width)]

    # Stack frames side by side
    output_frame = cv2.hconcat([left_frame, right_frame])

    # Write the output frame
    out.write(output_frame)

# Release everything when the job is finished
cap.release()
out.release()
