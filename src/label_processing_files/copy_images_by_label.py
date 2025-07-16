import os
import json
import shutil

# ===== 경로 설정 =====
AAT_LABELS_PATH = "../../dataset/aat_labels.json"
LAT_LABELS_PATH = "../../dataset/lat_labels.json"

AAT_IMAGE_SRC_DIR = "../../dataset/raw/AiDLabA100/AAT/image"
LAT_IMAGE_SRC_DIR = "../../dataset/raw/AiDLabA100/LAT/image"

AAT_IMAGE_DST_DIR = "../../dataset/processed_images/AAT"
LAT_IMAGE_DST_DIR = "../../dataset/processed_images/LAT"

# ===== 보조 함수 =====
def copy_images_from_labels(label_path, src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    with open(label_path, 'r') as f:
        data = json.load(f)

    missing = []
    copied = 0

    for entry in data:
        filename = entry["filename"]
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)

        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
            copied += 1
        else:
            missing.append(filename)

    print(f"✅ {copied} images copied to {dst_dir}")
    if missing:
        print(f"⚠️ {len(missing)} images not found in source directory.")
        for m in missing[:5]:  # 상위 5개만 보여주기
            print(f" - {m}")

# ===== 실행 =====
copy_images_from_labels(AAT_LABELS_PATH, AAT_IMAGE_SRC_DIR, AAT_IMAGE_DST_DIR)
copy_images_from_labels(LAT_LABELS_PATH, LAT_IMAGE_SRC_DIR, LAT_IMAGE_DST_DIR)
