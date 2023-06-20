# from ultralytics import YOLO

# # Load a model
# model = YOLO('yolov8x-seg.yaml')  # build a new model from YAML
# model = YOLO('/home/m/macko70/projects/yolov8/yolov8x-seg.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8x-seg.yaml').load('/home/m/macko70/projects/yolov8/yolov8x-seg.pt')  # build from YAML and transfer weights

# model.train(data='/home/m/macko70/projects/yolov8/ultralytics/datasets/groceries.yaml', epochs=100, imgsz=1024, batch=4)

from ultralytics import YOLO

model = YOLO('yolov8x-seg.pt')  # load an official model
model = YOLO('/home/m/macko70/projects/yolov8/runs/segment/train13/weights/best.pt')  # load a custom trained

# Export the model
model.export(format='onnx')