# Explainable AI
A github project for XAI research: XAI in image classification

Author: Fernando, Yuyang

# Introduction
In this project, we applied the LIME
technique to explain a general-purpose, multi-class model called MobileNet in an effort to improve both
performance metrics and explainability. 
While the model’s accuracy was not improved, it was possible 
to increase the explainability of an augmented subset of the ImageNet dataset by the use of impact score.

This finding highlights the trade-off between accuracy and explainability that exists in XAI research area
and suggests that further XAI optimization method is necessary in order to improve both measures.
The results of this work highlight the importance of considering
both accuracy and explainability when selecting and applying image augmentation techniques in image
classification task


## LIME [Repo](https://github.com/marcotcr/lime)
pip install lime

## MobileNet
[Keras](https://keras.io/api/applications/mobilenet/)

## ImageNet

[ImageNet Object Localization Challenge](https://www.kaggle.com/competitions/imagenet-object-localization-challenge/data)

Kaggle [API](https://github.com/Kaggle/kaggle-api)

only the validation [set](https://www.kaggle.com/code/fbernuy/download-validation-set) 

**So in the end I just downloaded this [Imagenette](https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-320.tgz) lol**

## Milestone

- 11 November: analyze and improve the experimentation for better generalization.
- 28 November: final experiments and results.

- 29 November: presentation rehearsal, submit first draft of report and presentation.
- 16 December: final presentation.
- 23 December: possible peer feedback and improvement in written report.
- 16 January: finish the final report, which will be written in parallel during the above steps.

## Tasks
1. Find neibourhood paramters, determine which set of parameters affect most of the predictions // refers to LIME paras
1. Need some metrics, make more accurate(prob increase some top-1 prediction probabilities)
1. read the LIME documentation
1. More literatures about LIME research
    1. Explaining the [explainer](http://proceedings.mlr.press/v108/garreau20a/garreau20a.pdf)
1. Determine the parameters we are going to use in the experiments
1. develop a *pipeline*...kinda hard
1. Do some experiments, automate the process
> Benchmarking the explaination method
> Using [OpenXAI](https://open-xai.github.io/)  
> (LIME, SHAP, Vanilla Gradients, Gradient x Input, SmoothGrad, and Integrated Gradients)
> 
> **Note: In OPenXAI there are lots of metrics for explainer evaluation**

## Pipeline (Optional: Which will be replaced by OpenXAI API mentioned above)
1. select params for LIME, image (contrast, blur...)
1. predict all images in a floder
1. save the result explainations, compare and analyze (e.g. overlay all the explainations to see the results)
1. repeat step 1
1. metrics for LIME performance (OpenXAI)

