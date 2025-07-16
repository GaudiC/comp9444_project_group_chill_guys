import os
import json

# 입력 경로
lat_path = "../../dataset/raw/AiDLabA100/LAT/label/LAT.json"
aat_path = "../../dataset/raw/AiDLabA100/AAT/label/AAT.json"

# 출력 경로
lat_output_path = "../../dataset/lat_labels.json"
aat_output_path = "../../dataset/aat_labels.json"

def extract_parts(entry, expect_subclass=True):
    """
    - If expect_subclass is True: expect format like "Shoes/Heels_001A03"
    - If False: expect format like "Shoes_001Q03"
    """
    category_sub, image_id = entry.split("_")

    if expect_subclass and "/" in category_sub:
        major_class, sub_class = category_sub.split("/")
    else:
        major_class = category_sub
        sub_class = None  # No subclass info

    return image_id + ".jpg", major_class.lower(), sub_class.lower() if sub_class else None

def process_json(json_path, expect_subclass):
    label_dict = {}
    with open(json_path, 'r') as f:
        data = json.load(f)
        for entry in data:
            for item in entry["question"] + entry["answers"]:
                fname, major_class, sub_class = extract_parts(item, expect_subclass)
                label_dict[fname] = {
                    "filename": fname,
                    "major_class": major_class
                }
                if sub_class:
                    label_dict[fname]["sub_class"] = sub_class
    return list(label_dict.values())

# 각 JSON 처리
lat_labels = process_json(lat_path, expect_subclass=False)
aat_labels = process_json(aat_path, expect_subclass=True)

# 저장
with open(lat_output_path, 'w') as f:
    json.dump(lat_labels, f, indent=2)

with open(aat_output_path, 'w') as f:
    json.dump(aat_labels, f, indent=2)

print(f"✅ LAT 라벨 {len(lat_labels)}개 → {lat_output_path}")
print(f"✅ AAT 라벨 {len(aat_labels)}개 → {aat_output_path}")
