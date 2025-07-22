import os
import json
import random
import time
from PIL import Image

def gen_id():
    rand_part = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    ts_part = str(int(time.time()))[-3:]
    return int(rand_part + ts_part)

def get_image_info(img_path):
    with Image.open(img_path) as img:
        width, height = img.size
    size = os.path.getsize(img_path)
    file_name = os.path.basename(img_path)
    ext = os.path.splitext(file_name)[1][1:].upper()
    if ext == "JPG":
        ext = "JPEG"
    return width, height, size, file_name, ext

def main(root_dir):
    # category_id: (singular, plural)
    CATEGORIES = {
        0: ("blueberry", "blueberries"),
        1: ("fig", "figs"),
        2: ("strawberry", "strawberries"),
        3: ("apple", "apples"),
        4: ("orange", "oranges"),
        5: ("pineapple", "pineapples"),
        6: ("banana", "bananas"),
        7: ("pear", "pears"),
        8: ("avocado", "avocados"),
        9: ("kiwi", "kiwis")
    }
    STYLE_MAP = {
        0: "sketch",
        1: "oil painting",
        2: "hard painting",
        3: "mosaic cartoon",
        4: "knitted",
        5: "wooden",
        6: "pencil drawing",
        7: "plastic",
        8: "real",
        9: "multi real"
    }
    info = {
        "description": "data",
        "version": "1.0",
        "year": 2025,
        "contributor": "search engine",
        "source": "augmented",
        "license": {
            "name": "Creative Commons Attribution 4.0 International",
            "url": "https://creativecommons.org/licenses/by/4.0/"
        }
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
        category_singular, category_plural = CATEGORIES.get(category_id, ("unknown", "unknowns"))
        style_name = STYLE_MAP.get(subcategory_id, "unknown")
        subcategory_name = f"{style_name} {category_plural}"
        width, height, size, file_name, ext = get_image_info(os.path.join(root_dir, file))
        image_id = gen_id()
        annotation_id = gen_id()
        images = [{
            "id": image_id,
            "width": width,
            "height": height,
            "file_name": file_name,
            "size": size,
            "format": ext,
            "url": "",
            "hash": "",
            "status": "success",
            "subcategory_id": subcategory_id,
            "subcategory_name": subcategory_name
        }]
        annotations = [{
            "id": annotation_id,
            "image_id": image_id,
            "category_id": category_id,
            "segmentation": [],
            "area": width * height,
            "bbox": [0, 0, width, height]
        }]
        categories = [{
            "id": category_id,
            "name": category_plural,
            "supercategory": category_singular
        }]
        json_data = {
            "info": info,
            "images": images,
            "annotations": annotations,
            "categories": categories
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