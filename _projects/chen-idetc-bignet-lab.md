---
title: Automating Style Analysis and Visualization With Explainable AI - Case Studies on Brand Recognition
description: |
  A deep learning, data-driven way to automatically learn brand-related features 

people:
  - SeanC

layout: project
image: img/idetc-bigner-lab.png
last-updated: 2023-05-30
status: active

---
​
Incorporating style-related objectives into shape design has been centrally important to maximize product appeal. However, stylistic features such as aesthetics and semantic attributes are hard to codify even for experts. As such, algorithmic style capture and reuse have not fully benefited from automated data-driven methodologies due to the challenging nature of design describability. This paper proposes an AI-driven method to fully automate the discovery of brand-related features. Our approach introduces BIGNet, a two-tier Brand Identification Graph Neural Network (GNN) to classify and analyze scalar vector graphics (SVG). First, to tackle the scarcity of vectorized product images, this research proposes two data acquisition workflows: parametric modeling from small curve-based datasets, and vectorization from large pixel-based datasets. Secondly, this study constructs a novel hierarchical GNN architecture to learn from both SVG's curve-level and chunk-level parameters. In the first case study, BIGNet not only classifies phone brands but also captures brand-related features across multiple scales, such as the location of the lens, the height-width ratio, and the screen-frame gap, as confirmed by AI evaluation. In the second study, this paper showcases the generalizability of BIGNet learning from a vectorized car image dataset and validates the consistency and robustness of its predictions given four scenarios. The results match the difference commonly observed in luxury vs. economy brands in the automobile market. Finally, this paper also visualizes the activation maps generated from a convolutional neural network and shows BIGNet’s advantage of being a more human-friendly, explainable, and explicit style-capturing agent. Code and datasets are available on Github:

* [Phone](https://github.com/parksandrecfan/bignet-phone)
* [Car](https://github.com/parksandrecfan/bignet-car)