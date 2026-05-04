# ====================== 只需要改这里！======================
# 把这里换成你自己训练的模型绝对路径
MODEL_PATH = r"D:\yolov8n_fatigue\runs\detect\train\weights\best.pt"
# ==========================================================

from ultralytics import YOLO
import cv2

# 加载你自己训练的模型（最稳定的官方方式，不会报错）
model = YOLO(MODEL_PATH).to('cpu')

# 打开摄像头（0 = 默认摄像头）
cap = cv2.VideoCapture(0)

# 判断摄像头是否成功打开
if not cap.isOpened():
    print("摄像头打开失败！")
    exit()

print(" 摄像头已启动，实时检测中... 按 Q 退出")

# 循环读取每一帧
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 模型推理（核心）
    results = model(frame, stream=True)

    # 绘制检测框
    for r in results:
        frame = r.plot()

    # 显示画面
    cv2.imshow("自定义模型 - 实时检测", frame)

    # 按 Q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()