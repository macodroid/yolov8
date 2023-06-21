import os
import posixpath
import shutil

from pycocotools.coco import COCO

if __name__ == "__main__":
    root_train_dir = "/home/maco/Documents/photoneo/data/groceries/train"
    root_test_dir = "/home/maco/Documents/photoneo/data/groceries/test"

    destination_train_dir = "/home/maco/Documents/photoneo/yolo_format_dataset/train/images"
    destination_test_dir = "/home/maco/Documents/photoneo/yolo_format_dataset/val/images"

    train_ann_file = "/home/maco/Documents/photoneo/data/groceries/train/.exports/coco-1686932861.coco.json"
    test_ann_file = "/home/maco/Documents/photoneo/data/groceries/test/.exports/coco-1686932837.coco.json"

    coco_train = COCO(train_ann_file)
    coco_test = COCO(test_ann_file)

    # train images
    for i in range(len(coco_train.imgs)):
        origin_img_path = posixpath.join(root_train_dir, coco_train.imgs[i]['file_name'])
        shutil.copy(origin_img_path, destination_train_dir)

    # test images
    for i in range(len(coco_test.imgs)):
        origin_img_path = posixpath.join(root_test_dir, coco_test.imgs[i]['file_name'])
        shutil.copy(origin_img_path, destination_test_dir)
