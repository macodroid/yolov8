# YOLOv8 Groceries segmentation

## Training

Before training we need to convert annoation data from standard coco format of yolo format.  
This was done by [JSON2YOLO](https://github.com/macodroid/yolov8-groceries/tree/main/JSON2YOLO) with bit of modification. (Dataset in yolo format are provided in google drive (see email)).

Training process was done in Jupyter Notebook [seg_groceries_yolov8.ipynb](https://github.com/macodroid/yolov8-groceries/blob/main/seg_groceries_yolov8.ipynb)

### How to train

1. Download pre-trained YOLOv8 model (google drive) ```yolov8x-seg.pt```. Download it to the root directory of this project (same level as this README.me).
2. Download groceries dataset in yolo format (google drive) and place them in root directory of this project.
3. In ```./ultralytic/datasets/groceries.yaml``` [groceries.yaml](https://github.com/macodroid/yolov8-groceries/blob/main/ultralytics/datasets/groceries.yaml) adjust paths training and validation dataset.
4. In file [seg_groceries_yolov8.ipynb](https://github.com/macodroid/yolov8-groceries/blob/main/seg_groceries_yolov8.ipynb) adjust path for pre trained model.
5. In same file [seg_groceries_yolov8.ipynb](https://github.com/macodroid/yolov8-groceries/blob/main/seg_groceries_yolov8.ipynb) one more adjusment need to be made and it is setting path to the [groceries.yaml](https://github.com/macodroid/yolov8-groceries/blob/main/ultralytics/datasets/groceries.yaml) file.

## Evaluation

Evaluation of trained model is done in [eval_yolov8_seg_groceries.ipynb](https://github.com/macodroid/yolov8-groceries/blob/main/eval_yolov8_seg_groceries.ipynb)

### How to evaluate and visualize

1. Download trained and exported YOLOv8 segment model (google drive).
2. In second cell of notebook adjust path of download model.
3. In third cell adjust paths to dataset (**yolo formated dataset**).
4. Run it.
