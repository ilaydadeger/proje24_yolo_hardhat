from ultralytics import YOLO

# Model dosyasını models klasöründen yükle
model = YOLO("models/yolov8n.pt")   

model.train(
    data="configs/data_small.yaml",  # veya "configs/data.yaml"
    epochs=50,
    imgsz=640,
    batch=16
)
