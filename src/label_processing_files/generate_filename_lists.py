import os

# === 현재 위치: src/label_processing_files/ 기준으로 경로 설정 ===
AAT_IMAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                  "../../../project_root/data/processed_images/AAT"))
LAT_IMAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                  "../../../project_root/data/processed_images/LAT"))

# 결과 저장 경로
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                               "../../../project_root/data/filename_lists"))
AAT_FILENAME_PATH = os.path.join(OUTPUT_DIR, "aat_filenames.txt")
LAT_FILENAME_PATH = os.path.join(OUTPUT_DIR, "lat_filenames.txt")

# === 파일명 저장 함수 ===
def save_filenames(image_dir, output_path):
    if not os.path.exists(image_dir):
        print(f"❌ Directory not found: {image_dir}")
        return

    filenames = sorted([
        fname for fname in os.listdir(image_dir)
        if fname.lower().endswith((".jpg", ".png"))
    ])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        for fname in filenames:
            f.write(fname + "\n")

    print(f"✅ Saved {len(filenames)} filenames to {output_path}")


# === 실행 ===
save_filenames(AAT_IMAGE_DIR, AAT_FILENAME_PATH)
save_filenames(LAT_IMAGE_DIR, LAT_FILENAME_PATH)
