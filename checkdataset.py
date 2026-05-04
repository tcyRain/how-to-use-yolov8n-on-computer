import os

# ========= 这里改成你自己的路径 =========
img_dir  = r"D:\yolov8n_fatigue\fatigue\images\val"
label_dir = r"D:\yolov8n_fatigue\fatigue\labels\val"
# ========================================

# 支持的图片后缀
img_suffix = [".jpg", ".jpeg", ".png", ".bmp"]

# 获取所有图片纯文件名
img_names = []
for f in os.listdir(img_dir):
    name, ext = os.path.splitext(f)
    if ext.lower() in img_suffix:
        img_names.append(name)

# 获取所有标签纯文件名
label_names = []
for f in os.listdir(label_dir):
    name, ext = os.path.splitext(f)
    if ext.lower() == ".txt":
        label_names.append(name)

print("===== 没有标签的图片 =====")
for name in img_names:
    if name not in label_names:
        print(name)

print("\n===== 没有图片的标签 =====")
for name in label_names:
    if name not in img_names:
        print(name)