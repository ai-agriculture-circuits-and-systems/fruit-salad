import os
import json

def main(root_dir):
    CATEGORIES = {
        0: "blueberries",
        1: "fig",
        2: "strawberry",
        3: "apple",
        4: "orange",
        5: "pineapple",
        6: "bananas",
        7: "pear",
        8: "avocado",
        9: "kiwi"
    }
    STYLE_MAP = {
        "0": "sketch",
        "1": "oil painting",
        "2": "hard painting",
        "3": "mosaic cartoon",
        "4": "knitted",
        "5": "wooden",
        "6": "pencil drawing",
        "7": "plastic",
        "8": "real",
        "9": "multi real"
    }
    for file in os.listdir(root_dir):
        if not file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")):
            continue
        name_part = os.path.splitext(file)[0]
        if "_" not in name_part:
            continue
        parts = name_part.split("_", 1)
        if len(parts) != 2 or not (parts[0].isdigit() and parts[1].isdigit()):
            continue
        category_id = int(parts[0])
        subcategory_id = int(parts[1])
        category_name = CATEGORIES.get(category_id, "unknown")
        style_name = STYLE_MAP.get(parts[1], "unknown")
        subcategory_name = f"{style_name} {category_name}"
        json_data = {
            "category_id": category_id,
            "category_name": category_name,
            "subcategory_id": subcategory_id,
            "subcategory_name": subcategory_name
        }
        json_name = os.path.splitext(file)[0] + ".json"
        json_path = os.path.join(root_dir, json_name)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        print(f"Generated: {json_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fruit_salad_dir = os.path.join(script_dir, "fruit-SALAD_100")
    main(fruit_salad_dir) 