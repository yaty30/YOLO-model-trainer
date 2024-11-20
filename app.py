from ultralytics import YOLO
import os
from PIL import Image
import time
import threading

# Load a model
model = YOLO(r"C:\Users\James\Desktop\Codes\YOLO\Models\lionfish\weights\best.pt")

def run(video_path, imgsz):
    start = time.time()    
    # Process video frames
    results = model(source=video_path, conf=0.45, imgsz=imgsz, stream=False)  # predict on a video
    for idx, result in enumerate(results):
        boxes = result.boxes  # Boxes object for bounding box outputs
        result.show()  # display to screen
        result.save(filename=f"./Models/detect_results/result_{idx}.jpg")  # save to disk

    end = time.time()
    print(round(end-start, 2))

run(r"C:\Users\James\Desktop\Codes\HaarCascade\source_frames\lionfish.mp4", (432, 848))

# for idx, file in enumerate(os.listdir(r"C:\Users\James\Desktop\Codes\HaarCascade\source_frames\lionfish")):
#     img = Image.open(f"C:/Users/James/Desktop/Codes/HaarCascade/source_frames/lionfish/{file}")
#     width, height = img.size
#     print(height, width)
    
#     run(f"C:/Users/James/Desktop/Codes/HaarCascade/source_frames/lionfish/{file}", (height, width))

#     if idx == 10:
#         input("next")

# img = Image.open(r"C:\Users\James\Desktop\Codes\HaarCascade\source_frames\clownfish\frame_25.jpg")
# width, height = img.size
# print(height, width)

# run(r"C:\Users\James\Desktop\Codes\HaarCascade\source_frames\clownfish\frame_25.jpg", (height, width))

