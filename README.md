# fruit-SALAD
![SALAD_pipeline](SALAD_pipeline.png)

### Project Page: [https://style-aligned-artwork-datasets.github.io](https://style-aligned-artwork-datasets.github.io/)

**fruit-SALAD** is a synthetic image dataset with 10,000 generated images of fruit depictions. This combined semantic category and style benchmark comprises 100 instances each of 10 easily recognizable fruit categories and 10 easily distinguishable styles.

This repository contains the code to reproduce the fruit-SALAD dataset. Please see the Jupyter notebook [fruit-SALAD_pipeline.ipynb](fruit-SALAD_pipeline.ipynb) for more details.

---

## About

The Style Aligned Artwork Dataset (SALAD) provides a controlled and balanced platform for the comparative analysis of similarity perception in different computational models. The SALAD framework enables robust and interpretable comparison of semantic category and style recognition tasks.

We used [Stable Diffusion XL](https://arxiv.org/abs/2307.01952) and [StyleAligned](https://arxiv.org/abs/2312.02133) to create fruit-SALAD by carefully crafting text prompts and overseeing the image generation process. Original code by [Amir Hertz](https://github.com/amirhertz), [Andrey Voynov](https://github.com/anvoynov), and [Yuvraj Sharma](https://github.com/yvrjsharma). See [github.com/google/style-aligned](https://github.com/google/style-aligned/).

---

## Dataset Structure

The dataset is organized as follows:

```
fruit-SALAD_100/
    0_0.jpg
    0_1.jpg
    ...
    9_9.jpg
    0_0.json
    0_1.json
    ...
    9_9.json
```

- All images are stored directly in the `fruit-SALAD_100` directory.
- Each image file is named as `<category_id>_<style_id>.jpg`, where:
  - `category_id` is an integer from 0 to 9, representing the fruit type.
  - `style_id` is an integer from 0 to 9, representing the depiction style.
- For every image, there is a corresponding JSON annotation file with the same name (but `.json` extension).

### Category and Style Mapping

| category_id | Category Name | style_id | Style Name         |
|-------------|--------------|----------|--------------------|
| 0           | blueberries  | 0        | sketch             |
| 1           | figs         | 1        | oil painting       |
| 2           | strawberries | 2        | hard painting      |
| 3           | apples       | 3        | mosaic cartoon     |
| 4           | oranges      | 4        | knitted            |
| 5           | pineapples   | 5        | wooden             |
| 6           | bananas      | 6        | pencil drawing     |
| 7           | pears        | 7        | plastic            |
| 8           | avocados     | 8        | real               |
| 9           | kiwis        | 9        | multi real         |

---

## JSON Annotation Format

Each image has a corresponding JSON file containing its semantic and style information. The structure is as follows:

```
{
  "info": {
    "description": "data",
    "version": "1.0",
    "year": 2025,
    "contributor": "search engine",
    "source": "augmented",
    "license": {
      "name": "Creative Commons Attribution 4.0 International",
      "url": "https://creativecommons.org/licenses/by/4.0/"
    }
  },
  "images": [
    {
      "id": 1234567890,
      "width": 512,
      "height": 512,
      "file_name": "3_1.jpg",
      "size": 123456,
      "format": "JPEG",
      "url": "",
      "hash": "",
      "status": "success",
      "subcategory_id": 1,
      "subcategory_name": "oil painting apples"
    }
  ],
  "annotations": [
    {
      "id": 2345678901,
      "image_id": 1234567890,
      "category_id": 3,
      "segmentation": [],
      "area": 262144,
      "bbox": [0, 0, 512, 512]
    }
  ],
  "categories": [
    {
      "id": 3,
      "name": "apples",
      "supercategory": "apple"
    }
  ]
}
```

- `info`: General information about the dataset and license.
- `images`: List with a single entry describing the image and its style (subcategory).
  - `subcategory_id`: The style id (from the filename).
  - `subcategory_name`: The style and fruit combined (e.g., "oil painting apples").
- `annotations`: List with a single entry describing the annotation for the image (full image bounding box).
- `categories`: List with a single entry for the image's main category (plural name and singular supercategory).

---

## Download

You can access the complete fruit-SALAD_10k dataset at [Zenodo](https://doi.org/10.5281/zenodo.11158522).

```
Ohm, T. (2024). fruit-SALAD [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11158522
```

---

## Citation

See our research paper on [Scientific Data](https://www.nature.com/articles/s41597-025-04529-4).

```
@article{ohm2025FruitSALAD,
  title = {fruit-SALAD: A Style Aligned Artwork Dataset to reveal similarity perception in image embeddings},
  volume = {12},
  issn = {2052-4463},
  url = {https://doi.org/10.1038/s41597-025-04529-4},
  doi = {10.1038/s41597-025-04529-4},
  number = {1},
  journal = {Scientific Data},
  author = {Ohm, Tillmann and Karjus, Andres and Tamm, Mikhail V. and Schich, Maximilian},
  year = {2025},
  pages = {254},
}
```


