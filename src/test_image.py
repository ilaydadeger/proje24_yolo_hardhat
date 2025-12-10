from ultralytics import YOLO

MODEL_PATH = "../models/best.pt"
IMAGE_PATH = "../dataset_small/valid/images/004976_jpg.rf.4c33ed009755824eff507e01c41064dd.jpg"

def main():
    model = YOLO(MODEL_PATH)

    results = model.predict(
        source=IMAGE_PATH,
        save=True,
        conf=0.4
    )

    print("Tahmin tamamlandı! Sonuçlar runs/detect/predict*/ içinde.")

    for r in results:
        print("Sınıflar:", r.boxes.cls.tolist())
        print("Güven:", r.boxes.conf.tolist())

if __name__ == "__main__":
    main()
