import os
import shutil
import random
from pathlib import Path

# === AYARLAR ===
SRC_DATASET = "dataset"     # Orijinal dataset klasörü
DST_DATASET = "dataset_small"   # Yeni küçük dataset
N_TRAIN = 300
N_VAL = 100

# === KLASÖRLERİ OLUŞTUR ===
for split in ["train", "valid"]:
    for sub in ["images", "labels"]:
        Path(f"{DST_DATASET}/{split}/{sub}").mkdir(parents=True, exist_ok=True)

def copy_samples(split, num_samples):
    img_dir = Path(f"{SRC_DATASET}/{split}/images")
    label_dir = Path(f"{SRC_DATASET}/{split}/labels")

    all_images = list(img_dir.glob("*.jpg")) + list(img_dir.glob("*.png"))
    random.shuffle(all_images)

    selected = all_images[:num_samples]

    for img_path in selected:
        label_path = label_dir / (img_path.stem + ".txt")

        # Hedef klasörler
        dst_img = Path(f"{DST_DATASET}/{split}/images/{img_path.name}")
        dst_label = Path(f"{DST_DATASET}/{split}/labels/{label_path.name}")

        shutil.copy(img_path, dst_img)
        if label_path.exists():
            shutil.copy(label_path, dst_label)

    print(f"{split}: {len(selected)} görüntü kopyalandı.")

# === KOPYALAMA ===
copy_samples("train", N_TRAIN)
copy_samples("valid", N_VAL)

# === mini data.yaml oluştur ===
yaml_content = f"""
train: {DST_DATASET}/train/images
val: {DST_DATASET}/valid/images

nc: 1
names: ['hardhat']
"""

with open("data_small.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_content)

print("\n✔ dataset_small oluşturuldu!")
print("✔ data_small.yaml dosyası yazıldı!")
