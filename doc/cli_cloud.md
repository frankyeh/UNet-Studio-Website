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

3. **Run Actions**: Under the same `Actions` menu, click on `Auto-Track (OpenNeuro)` on the left and click run `workflow` on the right. 

*Setup Parameters*:

|Parameters | Descriptions |
|-----------|---------------|
| OpenNeuro Accession Number | the DS number of the OpenNeuro data. |
| Save SRC Files | specify whether to save SRC files for downloading. |
| QC report | specify whether to run a quality check on the dMRI data. |
| Region Analysis | the region analysis pipeline calculates the averages value of metrics in the atlas regions. | 
| Connectivity Matrix | the connectivity matrix pipeline calculates the whole-brain connectivity matrix using the atlas parcellations. | 
| Automatic Fiber Tracking | the automatic fiber tracking pipeline maps tracts of interests and calculates their diffusion and shape metrics. | 
| Options: Atlases | specify the atlases to be used in region analysis or connectivity matrix. [Full list of atlases](https://github.com/frankyeh/DSI-Studio-atlas/tree/main/ICBM152)  |
| Options: Tracts of Interest | specify the tracts to be mapped used in automatic fiber tracking. Partial name accepted. [Full list of tracts](https://github.com/frankyeh/DSI-Studio-atlas/blob/main/ICBM152/ICBM152.tt.gz.txt)|

Click on `Run workflow` to start. 

4. **Download Results**: Once completed, the intermediate results (e.g. SRC files, FIB files), tract files, and tract metrics can be downloaded. SRC, FIB, TT files  can be [inspected in DSI Studio](https://dsi-studio.labsolver.org/doc/gui_t3_whole_brain.html).

<img src="https://user-images.githubusercontent.com/275569/157700442-6fae3601-9208-4607-af56-eb4b44d43877.png" width=500>
