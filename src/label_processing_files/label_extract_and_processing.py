import os
import json

# 📁 입력 JSON 경로
lat_path = "../../dataset/raw/AiDLabA100/LAT/label/LAT.json"
aat_path = "../../dataset/raw/AiDLabA100/AAT/label/AAT.json"
output_path = "../../dataset/labels.json"

# 중복 제거를 위해 dict 사용
unique_labels = {}

def extract_parts(entry):
    """
    Handles both:
    - "Shoes/Heels_001A03"
    - "Shoes_005A07"
    """
    category_sub, image_id = entry.split("_")
    
    if "/" in category_sub:
        category, subcategory = category_sub.split("/")
    else:
        category = category_sub
        subcategory = "unknown"  # 또는 "general", "none" 등 원하는 대로

    return image_id + ".jpg", category.lower(), subcategory.lower()


def process_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
        for entry in data:
            for item in entry["question"] + entry["answers"]:
                fname, label, specific = extract_parts(item)
                unique_labels[fname] = {
                    "filename": fname,
                    "label": label,
                    "specific_category": specific
                }

# 실행
process_json(lat_path)
process_json(aat_path)

# 저장
output_data = list(unique_labels.values())
with open(output_path, 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"✅ labels.json 생성 완료: 총 {len(output_data)}개 이미지 라벨링됨")
print(f"→ 저장 위치: {output_path}")
print("LAT exists?", os.path.exists(lat_path))
print("AAT exists?", os.path.exists(aat_path))