import os
import json
import shutil

# 경로 설정
# RAW_ROOT = "dataset/raw/AiDLabA100"
# OUTPUT_DIR = "dataset/images"
RAW_ROOT = r"C:\Users\willi\Documents\UNSW\2025\Term 2\COMP9444\Group Project - Chill Guys\dataset\raw\AiDLabA100"
OUTPUT_DIR = r"C:\Users\willi\Documents\UNSW\2025\Term 2\COMP9444\Group Project - Chill Guys\dataset\images"


# AAT, LAT json 파일 경로
json_paths = [
    os.path.join(RAW_ROOT, "AAT/label/AAT.json"),
    os.path.join(RAW_ROOT, "LAT/label/LAT.json")
]

# 이미지가 있는 디렉토리 경로 (AAT, LAT 둘 다 같다고 가정)
image_dirs = [
    os.path.join(RAW_ROOT, "AAT/image"),
    os.path.join(RAW_ROOT, "LAT/image")
]

# 출력 디렉토리 생성
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 처리 시작
all_filenames = set()

# 1. JSON 파일에서 이미지 이름 추출
for json_path in json_paths:
    with open(json_path, "r") as f:
        data = json.load(f)
        for item in data:
            # 'question' + 'answers' 에 있는 모든 이미지 ID 추출
            all_filenames.update(item["question"])
            all_filenames.update(item["answers"])

print(f"총 {len(all_filenames)}개의 이미지 이름 수집됨")

# 2. 이미지 디렉토리에서 이미지 복사
copied = 0
for img_name in all_filenames:
    img_file = img_name + ".jpg"  # 확장자 붙이기
    found = False
    for src_dir in image_dirs:
        src_path = os.path.join(src_dir, img_file)
        if os.path.exists(src_path):
            shutil.copy(src_path, os.path.join(OUTPUT_DIR, img_file))
            copied += 1
            found = True
            break
    if not found:
        print(f"[⚠️ 경고] 이미지 없음: {img_file}")

print(f"✅ 복사 완료: {copied}개 이미지 → {OUTPUT_DIR}")
