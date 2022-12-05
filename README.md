# Explainable AI
A github project for XAI research

Markdown [Syntax](https://www.markdownguide.org/basic-syntax/#links)
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

## Pipeline
1. select params for LIME, image (contrast, blur...)
1. predict all images in a floder
1. save the result explainations, compare and analyze (e.g. overlay all the explainations to see the results)
1. repeat step 1
1. metrics for LIME performance (OpenXAI)

## Ideas for final reports
1. Less than 12 pages
1. Early bird, early draft
