# DSI Studio Cloud

<img src="https://user-images.githubusercontent.com/275569/166306915-3253113f-fe69-48bb-91a9-000cf5ae6822.png" width=500>

[DSI Studio Cloud](https://github.com/frankyeh/DSI-Studio-Cloud) is a GitHub repository that uses GitHub's cloud computing resource to analyze diffusion MRI data. It can construct tractography and analyze its diffusion and shape metrics. The code can be extended to accomplish any command line functions provided in DSI Studio.

DSI Studio Cloud makes uses of the GitHub-hosted runner, a virtual machine hosted by GitHub, to process dMRI data. The GitHub-Action scripts in the DSI Studio Cloud get data from OpenNeuro to the GitHub runners and processe them using DSI Studio.

## Advantages

- **Free computation resources**: GitHub action provides 20 concurrent jobs with 2-core each. The computation power is equal to a 40-core workstation, much faster than running it on most laptops/desktops.

- **Faster data transfer**: The raw dMRI data are usually huge and can be up to several GB per scan, but tractography and related metrics are substantially smaller at MB size. Using DSI Studio Cloud, the amount of data transfer can be dramatically reduced. 

## Requirements 

- dMRI data stored on [OpenNeuro](https://openneuro.org/)
- A [GitHub](https://github.com/) account (free)

## Limitations

- **Not more than 256 scans data**: There is a maximum of 256 jobs per workflow run. DSI Studio will still generate SRC and FIB files for downloading, but fiber tracking cannot be executed due to the this limit.
- **90-day data retention**: GitHub will retain workflor data only for 90 days before they are automatically deleted.

## Steps

1. **Fork the repository**: Click on the `Fork` button in the upper right corner.

<img src="https://user-images.githubusercontent.com/275569/157307065-a172c393-a4db-4cf3-92c8-b4482619a0e7.png" width=500>

2. **Enable Actions**: Click on the `Actions` menu and confirm `I understand my workflows, go ahead and enable them`. 

<img src="https://user-images.githubusercontent.com/275569/157596167-7d9ee687-2633-4d48-ba5f-c12c62b04b35.png" width=500>

3. **Run Actions**: Under the same `Actions` menu, click on `Auto-Track (OpenNeuro)` on the left and click run `workflow` on the right. Assign `OpenNeuro Accession Number` (e.g. ds000031) and also `Tract of Interest`, which support partial name, and multiple tracts can be assigned using comman separator (e.g. Arcuate,Optic_Radiation). Click on `Run workflow` to start. 

The full list of tracts supported:

```
Arcuate_Fasciculus_L
Arcuate_Fasciculus_R
Cingulum_Frontal_Parahippocampal_L
Cingulum_Frontal_Parahippocampal_R
Cingulum_Frontal_Parietal_L
Cingulum_Frontal_Parietal_R
Cingulum_Parahippocampal_Parietal_L
Cingulum_Parahippocampal_Parietal_R
Cingulum_Parahippocampal_L
Cingulum_Parahippocampal_R
Cingulum_Parolfactory_L
Cingulum_Parolfactory_R
Extreme_Capsule_L
Extreme_Capsule_R
Frontal_Aslant_Tract_L
Frontal_Aslant_Tract_R
Inferior_Fronto_Occipital_Fasciculus_L
Inferior_Fronto_Occipital_Fasciculus_R
Inferior_Longitudinal_Fasciculus_L
Inferior_Longitudinal_Fasciculus_R
Middle_Longitudinal_Fasciculus_L
Middle_Longitudinal_Fasciculus_R
Parietal_Aslant_Tract_L
Parietal_Aslant_Tract_R
Superior_Longitudinal_Fasciculus1_L
Superior_Longitudinal_Fasciculus1_R
Superior_Longitudinal_Fasciculus2_L
Superior_Longitudinal_Fasciculus2_R
Superior_Longitudinal_Fasciculus3_L
Superior_Longitudinal_Fasciculus3_R
Uncinate_Fasciculus_L
Uncinate_Fasciculus_R
Vertical_Occipital_Fasciculus_L
Vertical_Occipital_Fasciculus_R
Acoustic_Radiation_L
Acoustic_Radiation_R
Corticobulbar_Tract_L
Corticobulbar_Tract_R
Corticopontine_Tract_Frontal_L
Corticopontine_Tract_Frontal_R
Corticopontine_Tract_Parietal_L
Corticopontine_Tract_Parietal_R
Corticopontine_Tract_Occipital_L
Corticopontine_Tract_Occipital_R
Corticospinal_Tract_L
Corticospinal_Tract_R
Corticostriatal_Tract_Anterior_L
Corticostriatal_Tract_Anterior_R
Corticostriatal_Tract_Posterior_L
Corticostriatal_Tract_Posterior_R
Corticostriatal_Tract_Superior_L
Corticostriatal_Tract_Superior_R
Thalamic_Radiation_Anterior_L
Thalamic_Radiation_Anterior_R
Thalamic_Radiation_Posterior_L
Thalamic_Radiation_Posterior_R
Thalamic_Radiation_Superior_L
Thalamic_Radiation_Superior_R
Dentatorubrothalamic_Tract_L
Dentatorubrothalamic_Tract_R
Fornix_L
Fornix_R
Medial_Lemniscus_L
Medial_Lemniscus_R
Optic_Radiation_L
Optic_Radiation_R
Reticular_Tract_L
Reticular_Tract_R
Anterior_Commissure
Corpus_Callosum_Forceps_Minor
Corpus_Callosum_Body
Corpus_Callosum_Tapetum
Corpus_Callosum_Forceps_Major
Cerebellum_L
Cerebellum_R
Inferior_Cerebellar_Peduncle_L
Inferior_Cerebellar_Peduncle_R
Middle_Cerebellar_Peduncle
Superior_Cerebellar_Peduncle
Vermis
CNII_L
CNII_R
CNIII_L
CNIII_R
CNV_L
CNV_R
CNVII_L
CNVII_R
CNVIII_L
CNVIII_R
```

4. **Download Results**: Once completed, the intermediate results (e.g. SRC files, FIB files), tract files, and tract metrics can be downloaded. SRC, FIB, TT files  can be [inspected in DSI Studio](https://dsi-studio.labsolver.org/doc/gui_t3_whole_brain.html).

<img src="https://user-images.githubusercontent.com/275569/157700442-6fae3601-9208-4607-af56-eb4b44d43877.png" width=500>
