# Differential Tractography

![image](https://user-images.githubusercontent.com/275569/147860577-35e5b242-2991-4cdf-b6f7-91161d8b0c73.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/EWOGQ3QTrnw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Differential tractography compares one scan to another to capture neuronal change reflected by a decrease of anisotropy. Differential tractography integrates the  "tracking-the-difference" paradigm as opposed to the "tracking-the-existence" used in the conventional setting. This is realized by adding one criterion to screen if  trajectories have a decrease of anisotropy. Differential tractography greatly increases the sensitivity and specificity of the diffusion metrics by aggregating results along white matter pathways.

![image](https://user-images.githubusercontent.com/275569/170849962-ef2f90af-748a-4011-8610-508fa8e24645.png)

Differential tractography can be applied to DTI data, multi-shell data, and DSI data. The anisotropy can be derived from DTI or GQI. Higher b-value signals will be more sensitive to early-stage neuronal changes, whereas low b-value signals may include a lot of physiological fluctuations, and you may expect a higher false discovery rate (FDR). In the [original differential tractography study](https://pubmed.ncbi.nlm.nih.gov/31472253/), we used 256-direction grid sampling with b-max=4000 or even up to 7000 to get excellent FDR values lower than 0.05. Using DTI data may increase FDR to 0.2.

![image](https://user-images.githubusercontent.com/275569/147860680-74abdce8-81a3-47a6-9d01-3d93be355b0d.png)

There are 3 types of differential tractography, and the applicable types depend on the experiment design. 

## **Type 1: mapping longitudinal change in the native space:**

**Requirements**:
- repeat scans of the same subject, e.g. before/after treatment
- the subject's DWI data are good enough for fiber tracking

**Example**: 
- human subject study with repeated scans before and after treatment

**Steps using GUI**: 

|   |    |
|-----------|------------|
| 1. **Generate FIB Files** |  use the following steps to get a GQI-reconstructed FIB file for each scan, including |
|  | 1a. [creating SRC files](/doc/gui_t1.html): make sure to have a quality check to make sure the quality is good |
|  | 1b. [generating FIB files](/doc/gui_t2.html): at Step T2B(1), please use GQI method to get native space FIB file. |
| 2. **Export Mmetrics** | for each follow-up scan (i.e. 2nd scan), conduct the following: |
|  | 2a. open the FIB file of follow-up scan at **[Step T3: Fiber Tracking]** |
|  | 2b. use the **[Export]** to save the dti_fa or qa map in a NIFTI file (e.g. sub1.followup.fa.nii.gz). |
| 3. **Optimize Tractography** | (optional) using one baseline FIB file from the baseline scan to optimize tracking parameters|
|  | 3a. open one baseline scan's FIB file at **[Step T3 Fiber Tracking]**  |
|  | 3b. restore default fiber tracking settings using **[Options][Restore Tracking Settings]**. |
|  | 3c. set **[Step T3c Options][Tracking Parameters][Terminate if]** to `1,000,000` seeds |
|  | 3d. click the **[Step T3d: Tracts][Fiber Tracking]** button to see if you can get a good quality whole-brain fiber tracking.<br> If not, check out the troubleshooting section of the [whole brain fiber tracking document](https://dsi-studio.labsolver.org/doc/gui_t3_whole_brain.html).  |
|  | 3e. find out the best parameters until getting a good quality of the whole-brain track.|
| 4. **Differential Tracking** | for each subject, carry out the following steps: |
|  | 4a. open baseline scan's FIB file at **[Step T3 Fiber Tracking]**|
|  | 4b. use **[Slice][Insert Other Images]** and select the NIFTI file of the follow-up scan (e.g. sub1.followup.fa.nii.gz created above). |
|  | 4c. select dti_fa or qa at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics1]**. This assumes that the anisotropy in the baseline scan is larger than the followup.|
|  | 4d. select the loaded metric at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics2]** |
|  | 4e. select the **[Step T3c: Options][Tracking Parameters][Differential Tracking][Threshold Type]**. |
|  | 4f. adjust thresholds by setting **[Differential Tracking][Metric1>Metric2 Threshold]=0.1, 0.2, or 0.3**, which specify 10%, 20%, and 30% differences. For most metrics, the normal individual differences are around 10~20%. Higher threshold gives more specific results against individual variations. To use absolute value as the threshold, set the [Threshold Type] to **m1-m2**.|
|  | 4g. click on **[Step T3d Tracts][Fiber Tracking]** to get differential tractography.|

## **Type 2: mapping longitudinal change in the template space:**

**Requirements**: 
- repeat scans of the same subject, e.g. before/after treatment 

**Example**: 
- animal in-vivo study with repeated scans before and after treatment (DWI not good enough for fiber tracking)
- human study which DWI data are not good enough for fiber tracking

## **Type 3: mapping cross sectional change in the native space:**

**Requirements**: 
- age-sex-matched controls avilable
- DWI data good enough for fiber tracking

**Example**: 
- human case-control studies


**Steps**:

1. ***[Create a connectometry database](https://dsi-studio.labsolver.org/doc/gui_cx.html):*** from control subjects. 
  - ***Associate data with demographics:*** Open the conenctometry database file in **[Step C2]** and load control subject's demographics using **[File][Open demographics]**. This step associate demographics with the controls in the database. ***TIP 1*** You can save the db.fib.gz after loading the demographics so that the connectometry database will be imbued with demographics. There is no need to repeat this step again. ***TIP 2*** Before doing this step, I would use **[Step C3]** to open the db.fib.gz file and load the demographics, just to check if there is any mismatch.
  - ***Generated demographic-matched baseline metrics:***. Then in the same Step C2 window, select **[File][Save Matched Image as]** and input the demographics of a subject to be matched. The demographics values need to be separated by a space. If your demographics include age and sex (0: female 1:male), then an example of the input text is **63,1** which will generate a 63-year-old male control subject metric. 

- **Load demographic-imbued connectometry databse in [Slice][Insert Other Image]**: Once the connectometry database is imbued with demographics, you can load it using [Slice][Insert Other Images]. To further tell DSI Studio the age and sex, you can rename the FIB file to inform DSI Studio age and sex of the subject. An example of the filename is **20220808_M029Y_XXXX.src.gz.gqi.fib.gz**, which tells that the subject is a 29-year-old male.

**TIPS**
If you don't have controls subjects, there are publicly available connectometry database available at https://brain.labsolver.org. However, most dMRI metrics (especially DTI metrics) are very sensitive to acquisition parameters, and likely you will get many false positive results just due to acquisition differences. The following are public available connectometry databases:
  - [HCP Aging](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EvdTx_lhJJBCmek2G0IfNhkBmr7CkGKU79H6JC1OH2aWmA?e=xtSbtb) (age: 36+ y)
  - [HCP Development](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 5-21 y)
  - [developing HCP (neonate)](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 20-44 weeks post-conception)
  - HCP young adult (to be constructed)
  - Grid258 (under construction)


## **Type 4: mapping cross sectional change in the template space:**

**Requirements**:
- age-sex-matched controls avilable

**Example**: 
- animal in-vivo or ex-vivo study studies where DWI data are not good enough for fiber tracking
- human case-control studies with DWI not good enough for fiber tracking



 

## Advanced Features & Suggestions

- **Reporting**
I would recommend checking a range of [Metric1>Metric2 Threshold] (e.g. 0.1, 0.2, 0.3, 0.4) and eliminate fregments by increasing [Step T3c:Options][Tracking Prameters][Min Length]. The goal is to maximize sensitivity while retaining specificity. 

- **Add ROA or ROI to limit findings**
You can map the affected pathways that pass through the internal capsule by assigning the internal capsule as the ROI. The number and length of tracks can be compared between patients if other tracking parameters are fixed (be sure to fix the seed count).

- **Exclude cerebellum**
Many false results may be generated just because of different slice coverage at the cerebellum. To handle this issue, add a region from [Atlas][BrainSeg][Cerebellum] and assign it as ROA.

- **Segment results into bundles**
You can use [Tracts][Miscellaneous][Recognize Track] to recognize the name of the bundles.

- **Apply smoothing to metrics**
If tracking results change a lot in repeated analyses, it is likely that the image acquisition is not optimal (e.g. too noisy, has very thick slices), and thus registration errors are boosted. To minimize this variance, export both baseline and follow-up NQA images and smooth them using [Tool][O41 View image][Signals][Smoothing] (make sure to update DSI Studio to use this function). Save the smoothed images as new files to run differential tracking. After smoothing, add the smoothed image back using [Slices][Add Other images] and continue with further analysis.


## False discovery rate and statistical testing

One key question for differential tractography is the significance of the findings. For example, if we observe a lot of tracks showing up in differential tractography, how many of them are false positive? A way to quantify this reliability is by calculating the false discovery rate from a group of patients and a group of control subjects. The following steps illustrate how this can be carried out in DSI Studio.

**Example 1: calculate the false discovery rate using control subjects**

1. Apply **identical** steps and parameters to N patients and N matched controls, respectively. 
2. Calculate false discovery rate (FDR): if you can get a total of 1000 tracks from 5 patients and 10 tracks from 5 controls, then the false discovery rate of the findings in patients is 10/100 = 10%. An FDR lower than 0.05 can be considered as significant.

**Example 2: calculate the false discovery rate without control subjects** 

This is the alternative sham approach described in the original work in Yeh, Neuroimage, 2019.

1. Apply **identical** steps to all subjects. 
2. Apply **identical** steps to all subjects but with an opposite order metrics 1 and 2 (e.g. switch followup and baseline or switch healthy and patient)
3. Calculate false discovery rate (FDR): If you can get a total of 1000 tracks from 1. patients and 10 tracks from 2., then the false discovery rate of the findings is 10/100 = 10%. An FDR lower than 0.05 can be considered significant.

