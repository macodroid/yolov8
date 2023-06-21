# YOLOv8 Groceries segmentation

## Training
Before training we need to convert annoation data from standard coco format of yolo format.  
This was done by [JSON2YOLO](https://github.com/macodroid/yolov8-groceries/tree/main/JSON2YOLO) with bit of modification. (Dataset in yolo format are provided in google drive (see email)).

Training process was done in Jupyter Notebook [seg_groceries_yolov8.ipynb](https://github.com/macodroid/yolov8-groceries/blob/main/seg_groceries_yolov8.ipynb)

### How to
1. Download pre-trained YOLOv8 model (google drive) ```yolov8x-seg.pt```. Download it to the root directory of this project (same level as this README.me).
2. Download groceries dataset in yolo format (google drive) and place them in root directory of this project.
3. 

