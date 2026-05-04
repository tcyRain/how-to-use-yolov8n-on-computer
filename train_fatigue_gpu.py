from ultralytics import YOLO

# 加载轻量 yolov8n 预训练权重
model = YOLO("yolov8n.pt")

if __name__ == "__main__":
    model.train(
        data="fatigue.yaml",
        epochs=10,
        imgsz=320,        # 关键！训练就用320，适配后续N6部署
        batch=16,         # 有显卡可以开大一点
        device='cpu',         # 0 = 使用GPU
        conf=0.25,
        iou=0.45,
        workers=4,
        save=True,
        verbose=True
    )