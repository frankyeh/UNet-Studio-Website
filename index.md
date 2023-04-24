# UNet-Studio: A Brain Segmentation Software Tool 
 
<img src="https://user-images.githubusercontent.com/275569/233228920-b0bee64b-8bc1-4d56-b139-0dea185f8777.png" width="800"/>


U-Net Studio is a powerful tool that segments brain tissues in human and animal scan data. It uses a unique data augmentation strategy combines visual simulation and negative output saturation to achieve accurate and efficient segmentation with just one population-averaged training dataset. The training results demonstrate that U-Net Studio is highly adaptive to previously unseen data, accurately segmenting subjects with large lesions. Moreover, U-Net Studio provides highly adaptive models for customizing region segmentation in both humans and animals, including rodents, rhesus monkeys, and marmosets. These pre-trained models are easily adaptable and retrainable for various imaging modalities, streamlining the segmentation process and reducing the need for manual annotation. U-Net Studio represents a valuable tool for improving the analysis of neuroimaging data.


Currently available models and training data used

| Model Name | Modality | Source |
|------------|----------|--------|
| human(test).t1w.seg5.net.gz      | t1w      | [ICBM152 2009a t1w template](https://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009) | 
| human(test).t2w.seg5.net.gz      | t2w      | [ICBM152 2009a t2w template](https://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009) | 
| rhesus.t1w.seg5.net.gz     | t1w      | [ONPRC18 t1w template](https://pubmed.ncbi.nlm.nih.gov/33137475/) | 
| rhesus.t2w.seg5.net.gz     | t2w      | [ONPRC18 t2w template](https://pubmed.ncbi.nlm.nih.gov/33137475/) | 
| marmoset.seg5.net.gz     | t2w,t1w      | [Marmoset Brain Mapping v3.0 t2w t1w template](https://www.sciencedirect.com/science/article/pii/S1053811920311058)| 
| rat(test).seg4.net.gz | t2w | [RESILIENT template image](https://osf.io/U4GTW/) | 
| mouse(test).seg5.net.gz | t2w, t1w | [Hikishima template](https://pubmed.ncbi.nlm.nih.gov/28273899/) | 

