# Visual calculator detecting basic handwritten arithmetic operations drew with Paint

This repository contains a "calculator_dataset" of numbers and "+", "-", "x", "÷" operators drew with a thin "Paint" style pen.

Use it in a similar way than the "mnist" implementation : 
- execute the "make_data.py" script
- use the "show_image.py" and "data_inspection.py" scripts to have an idea of the dataset structure
- train a YOLOV3 model to fit this dataset with the "train.py" script (the "configs.py" file is already configured, but you will need pretrained YOLOV3 weights in your model_data folder)
- use the "detect_operators.py" script to test the detection performances of the model trained
- and once your model detects numbers and operators correctly, you can use the "calculator.py" script to visually solve handwritten basic arithmetic operations

[![Visual calculator demo](https://j.gifs.com/zvDY6r.gif)](https://gifs.com/gif/visual-calculator-zvDY6r)

# TensorFlow-2.x-YOLOv3 tutorial (original README)

YOLOv3 implementation in TensorFlow 2.x, with support for training, transfer training.

## Installation
First, clode or download this GitHub repository.
Install requirements and download pretrained weights:
```
pip install -r ./requirements.txt

# yolov3
wget -P model_data https://pjreddie.com/media/files/yolov3.weights

# yolov3-tiny
wget -P model_data https://pjreddie.com/media/files/yolov3-tiny.weights
```

## Quick start
Start with using pretrained weights to test predictions on both image and video:
```
python detection_demo.py
```

<p align="center">
    <img width="100%" src="IMAGES/city_pred.jpg" style="max-width:100%;"></a>
</p>

## Quick training for custom mnist dataset
mnist folder contains mnist images, create training data:
```
python mnist/make_data.py
```
`./yolov3/configs.py` file is already configured for mnist training.

Now, you can train it and then evaluate your model
```
python train.py
tensorboard --logdir=log
```
Track training progress in Tensorboard and go to http://localhost:6006/:
<p align="center">
    <img width="100%" src="IMAGES/tensorboard.png" style="max-width:100%;"></a>
</p>

Test detection with `detect_mnist.py` script:
```
python detect_mnist.py
```
Results:
<p align="center">
    <img width="40%" src="IMAGES/mnist_test.jpg" style="max-width:40%;"></a>
</p>

## Custom Yolo v3 object detection training
Custom training required to prepare dataset first, how to prepare dataset and train custom model you can read in following link:<br>
https://pylessons.com/YOLOv3-TF2-custrom-train/

## Google Colab Custom Yolo v3 training
To learn more about Google Colab Free gpu training, visit my [text version tutorial](https://pylessons.com/YOLOv3-TF2-GoogleColab/)

## Yolo v3 Tiny train and detection
To get detailed instructions how to use Yolov3-Tiny, follow my text version tutorial [YOLOv3-Tiny support](https://pylessons.com/YOLOv3-TF2-Tiny/). Short instructions:
- Get YOLOv3-Tiny weights: ```wget -P model_data https://pjreddie.com/media/files/yolov3-tiny.weights```
- From `yolov3/configs.py` change `TRAIN_YOLO_TINY` from `False` to `True`
- Run `detection_demo.py` script.


To be continued...
--------------------
- [x] Detection with original weights [Tutorial link](https://pylessons.com/YOLOv3-TF2-introduction/)
- [x] Mnist detection training [Tutorial link](https://pylessons.com/YOLOv3-TF2-mnist/)
- [x] Custom detection training [Tutorial link1](https://pylessons.com/YOLOv3-TF2-custrom-train/), [link2](https://pylessons.com/YOLOv3-TF2-custrom-images/)
- [x] Google Colab training [Tutorial link](https://pylessons.com/YOLOv3-TF2-GoogleColab/)
- [x] YOLOv3-Tiny support [Tutorial link](https://pylessons.com/YOLOv3-TF2-Tiny/)
- [ ] Object tracking
- [ ] Converting to TensorFlow Lite
- [ ] Yolo v3 on Raspberry v3
- [ ] Yolo v3 on Android (Not sure about this)
- [ ] Convert to TensorRT model
- [ ] Generating anchors
- [ ] Mean Average Precision (mAP)
- [ ] YOLACT: Real-time Instance Segmentation
- [ ] Model pruning (Pruning is a technique in deep learning that aids in the development of smaller and more efficient neural networks. It's a model optimization technique that involves eliminating unnecessary values in the weight tensor.)
- [ ] Yolo v4
