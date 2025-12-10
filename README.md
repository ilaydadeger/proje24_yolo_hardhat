# YOLOv8 ile Baret (Hard Hat) Tespiti

Bu projede, inşaat sahalarında çalışan işçilerin **baret takıp takmadığını tespit eden** bir nesne tespit modeli geliştirdim.  
Model, Roboflow üzerinden alınan **Hard Hat Workers** veri seti kullanılarak YOLOv8 ile eğitilmiştir.

---

## 📌 Proje Özeti

- Roboflow'dan baret / işçi görüntüleri içeren veri seti indirildi.
- Veri seti çok büyük olduğu için, eğitim süresini kısaltmak amacıyla **küçük bir alt veri seti (`dataset_small`)** oluşturuldu.
- YOLOv8 (Ultralytics) kullanılarak model eğitildi.
- Eğitim sonrası model, valid setten seçilen bir görüntü üzerinde test edildi.
- Tahmin sonuçları `runs/detect/` klasörü altında saklandı.

Bu proje, CV’de göstermek üzere **uçtan uca bir bilgisayarla görü projesi** (veri → eğitim → tahmin → görsel çıktı) sunmaktadır.

---

## 🧱 Kullanılan Teknolojiler

- Python 3.10
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- Roboflow (veri seti yönetimi)
- PyTorch
- OpenCV (isteğe bağlı, gerçek zamanlı demo için kullanılabilir)
- VS Code

---

## 📂 Proje Yapısı

```text
proje24_yolo_hardhat/
├─ configs/
│  └─ data_small.yaml          # YOLO veri seti konfig dosyası
├─ dataset_small/              # Küçültülmüş eğitim veri seti
│  ├─ train/
│  ├─ valid/
│  └─ test/
├─ models/
│  └─ best.pt                  # Eğitilmiş YOLOv8 model ağırlıkları (lokal)
├─ runs/
│  └─ detect/                  # Eğitim / tahmin çıktıları (lokal, git'e dahil değil)
├─ src/
│  ├─ train.py                 # YOLOv8 eğitim scripti
│  └─ test_image.py            # Tek bir görüntüde tahmin yapan script
├─ utils/
│  └─ create_small_dataset.py  # Büyük veri setinden küçük alt küme oluşturan yardımcı script
├─ README.md
