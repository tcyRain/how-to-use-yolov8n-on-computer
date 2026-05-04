from ultralytics import YOLO
from ultralytics.data.utils import check_det_dataset

# 加载你的yaml配置
data_info = check_det_dataset("fatigue.yaml")

print("训练集图片路径：", data_info["train"])
print("验证集图片路径：", data_info["val"])
print("类别数：", data_info["nc"])
print("类别名：", data_info["names"])