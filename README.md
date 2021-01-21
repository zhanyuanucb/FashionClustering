- To reproduce:
  - PCA + K-Means: open and run k-means.ipynb
  - SCAN: 
  ```
  cd Unsupervised-Classification
  ./run_cluster.sh
  ```
- Why are you designing the solution in this way?
  - We are given a collection of images without labels, so I would frame it as a unsupervised image clustering problem.
- What are the aspects that you considered when designing?
  - Input size: the image size are not the same, so I either need to crop or resize them to the same sizes
  - Dimensionality reduction: Given the high dimensionality in images, it would be helpful to do reduction and only keep significant information
  - How to utilise the text information in the item descriptions
  - Will the background in the images affect the results?

- What are the cases your solution covers, how are they covered and why are they
  important?
  - I deployed two algorithms on this problem:
    - PCA + K-Means
    - [SCAN](https://github.com/wvangansbeke/Unsupervised-Classification)
  - They both utilise image information:
    - PCA + K-Means use the images themselves and cluster images based on the l2-norm among them
    - SCAN use deep neural network to extract features from images and then cluster them.
- What are the cases your solution does not cover and what are the ways you can
  extend your current solution for them?
  - I didn't take advantage of the text information in the descriptions
  - One possible way to extend my solution will be using some language models to encode the descriptions, and then using them as extra dimension of features for clustering.

- The following 8 images are duplicated in the JSON file:
      d38d479a018cca58d715108448e1966d5a7c0357.jpg   
      d35dc566420b8d9479c3859ead684753feec6423.jpg   
      a8f373af391ccf4ad90d32488dbf97f44925e4d5.jpg   
      5703a5992d0ca90fc335f4b3eff23bbbbd5a43ce.jpg   
      f169ba80f810f057755b11feb1efff3513efbf8a.jpg   
      2b2d8774a97155b0785557671822da01cf7e18dd.jpg   
      73af7ea268ac04809e898d6972e5730a83b246db.jpg   
      f79e7301d689d5640201e85f919cc47ccb110694.jpg   