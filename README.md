# fruit-SALAD
![SALAD_pipeline](SALAD_pipeline.png)

### Project Page: [https://style-aligned-artwork-datasets.github.io](https://style-aligned-artwork-datasets.github.io/)

**fruit-SALAD** is a synthetic image dataset with 10,000 generated images of fruit depictions. This combined semantic category and style benchmark comprises 100 instances each of 10 easily recognizable fruit categories and 10 easy distinguishable styles. 

This repository contains the code to reproduce the fruit-SALAD dataset. Please see the jupyter notebook [fruit-SALAD_pipeline.ipynb](fruit-SALAD_pipeline.ipynb) for more details.    

### About
The carefully designed Style Aligned Artwork Dataset (SALAD) provides a controlled and balanced platform for the comparative analysis of similarity perception of different computational models. The SALAD framework allows the comparison of how these models perform semantic category and style recognition tasks, going beyond the level of anecdotal knowledge, making them robustly quantifiable and qualitatively interpretable.

We used [Stable Diffusion XL](https://arxiv.org/abs/2307.01952) and [StyleAligned](https://arxiv.org/abs/2312.02133) to create the fruit-SALAD by carefully crafting text prompts and overseeing the image generation process. Original code by [Amir Hertz](https://github.com/amirhertz), [Andrey Voynov](https://github.com/anvoynov) and [Yuvraj Sharma](https://github.com/yvrjsharma). See [github.com/google/style-aligned](https://github.com/google/style-aligned/).


### Dataset
You can access the complete fruit-SALAD_10k dataset at [Zenodo](https://doi.org/10.5281/zenodo.11158522).
```
Ohm, T. (2024). fruit-SALAD [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11158522
```

### Cite
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


