[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

This is YOLOv4-tiny implemented in Tensorflow 2.0 with pretrained weights on the COCO Dataset.
Credit to original creator https://github.com/hunglc007/tensorflow-yolov4-tflite

### Link to set up and configure Pi Camera
https://www.raspberrypi.com/documentation/computers/configuration.html

First, clone this Git repo onto your Raspberry Pi:
```bash
git clone https://github.com/UTDL-Robodog/robodog/tree/xxx
```

Then, install the required packages
### Pip to install required packages
```bash
# This will let you install requirements on the Raspberry Pi
python3 -m pip install -r requirements.txt

# TensorFlow GPU (don't use this for now)
pip install -r requirements-gpu.txt
```

### Running the model

# Note: before running on video, you may want to save outputs somewhere:
if you do, add this to the end of the command
```
--output ./detections/results.avi
```

# Run yolov4-tiny tensorflow model
```bash
python3 detect.py --weights ./checkpoints/yolov4-tiny-416 --size 416 --model yolov4 --images ./data/images/kite.jpg --tiny
```
# Run yolov4-tiny on video
```bash
python3 detect_video.py --weights ./checkpoints/yolov4-tiny-416 --size 416 --model yolov4 --video ./data/video/video.mp4
```
# Run yolov4 on webcam
```bash
python3 detect_video.py --weights ./checkpoints/yolov4-tiny-416 --size 416 --model yolov4 --video 0
```

## Command Line Args Reference

```bash
save_model.py:
  --weights: path to weights file
    (default: './data/yolov4.weights')
  --output: path to output
    (default: './checkpoints/yolov4-416')
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'False')
  --input_size: define input size of export model
    (default: 416)
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)

detect.py:
  --images: path to input images as a string with images separated by ","
    (default: './data/images/kite.jpg')
  --output: path to output folder
    (default: './detections/')
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'False')
  --weights: path to weights file
    (default: './checkpoints/yolov4-416')
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
  --size: resize images to
    (default: 416)
  --iou: iou threshold
    (default: 0.45)
  --score: confidence threshold
    (default: 0.25)
    
detect_video.py:
  --video: path to input video (use 0 for webcam)
    (default: './data/video/video.mp4')
  --output: path to output video (remember to set right codec for given format. e.g. XVID for .avi)
    (default: None)
  --output_format: codec used in VideoWriter when saving video to file
    (default: 'XVID)
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'false')
  --weights: path to weights file
    (default: './checkpoints/yolov4-416')
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
  --size: resize images to
    (default: 416)
  --iou: iou threshold
    (default: 0.45)
  --score: confidence threshold
    (default: 0.25)
```

