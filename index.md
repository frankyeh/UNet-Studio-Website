# UNet-Studio: A Brain Segmentation Software Tool 
 
<img src="https://user-images.githubusercontent.com/275569/233228920-b0bee64b-8bc1-4d56-b139-0dea185f8777.png" width="400"/>


## Introduction

U-Net Studio is a powerful tool that segments brain tissues in human and animal scan data. It uses a data augmentation strategy to achieve accurate and efficient segmentation with just one population-averaged training dataset.

U-Net Studio provides highly adaptive models for customizing region segmentation in both humans and animals, including rodents, marmosets, rhesus monkeys, and human. These models are easily adaptable and retrainable for various imaging modalities, streamlining the segmentation process and reducing the need for manual annotation.


## Output

<img src="images/examples3.png" width="300"/>

U-Net Studio can output 3D labels or 4D probablistic maps for quantifying tissue characteristics. The tissue segmentation includes white matter, gray matter (excluding basal ganglion), basal ganglion, and others.

## Available models

Currently available models and training data used

| Model Name | Modality | Source |
|------------|----------|--------|
| human.t1w.seg5.net.gz      | t1w      | [ICBM152 2009a t1w template](https://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009) | 
| human.t2w.seg5.net.gz      | t2w      | [ICBM152 2009a t2w template](https://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009) | 
| rhesus.t1w.seg5.net.gz     | t1w      | [ONPRC18 t1w template](https://pubmed.ncbi.nlm.nih.gov/33137475/) | 
| rhesus.t2w.seg5.net.gz     | t2w      | [ONPRC18 t2w template](https://pubmed.ncbi.nlm.nih.gov/33137475/) | 
| marmoset.t1w.seg5.net.gz     | t1w      | [Marmoset Brain Mapping v3.0 t1w template](https://www.sciencedirect.com/science/article/pii/S1053811920311058)| 
| marmoset.t2w.seg5.net.gz     | t2w      | [Marmoset Brain Mapping v3.0 t2w template](https://www.sciencedirect.com/science/article/pii/S1053811920311058)| 
| rat.t2w.seg4.net.gz | t2w | [SIGMA wistar Rat template](https://www.nitrc.org/projects/sigma_template) | 
| mouse.t2w.seg5.net.gz | t2w, t1w | [Hikishima template](https://pubmed.ncbi.nlm.nih.gov/28273899/) | 

