# Differential Tractography

![image](https://user-images.githubusercontent.com/275569/147860577-35e5b242-2991-4cdf-b6f7-91161d8b0c73.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/EWOGQ3QTrnw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Differential tractography compares one scan to another and map capture neuronal change reflected by a decrease of anisotropy. Differential tractography integrates the  "tracking-the-difference" paradigm as opposed to the "tracking-the-existence" used in the conventional setting. This is realized by adding one tracking criterion to screen if trajectories have a decrease of anisotropy. Differential tractography greatly increases the sensitivity and specificity of the diffusion metrics by aggregating results along white matter pathways.

![image](https://user-images.githubusercontent.com/275569/170849962-ef2f90af-748a-4011-8610-508fa8e24645.png)

Differential tractography can be applied to DTI data, multi-shell data, and DSI data. The anisotropy can be derived from DTI or GQI. Higher b-value signals will be more sensitive to early-stage neuronal changes, whereas low b-value signals may include a lot of physiological fluctuations, and you may expect a higher false discovery rate (FDR). In the [original differential tractography study](https://pubmed.ncbi.nlm.nih.gov/31472253/), we used 256-direction grid sampling with b-max=4000 or even up to 7000 to get excellent FDR values lower than 0.05. Using DTI data may increase FDR to 0.2.

![image](https://user-images.githubusercontent.com/275569/147860680-74abdce8-81a3-47a6-9d01-3d93be355b0d.png)

There are 3 types of differential tractography, and the applicable types depend on the experiment design. 

# Type 1: mapping longitudinal change in the native space

**Requirements**:
- repeat scans of the same subject, e.g. before/after treatment
- the subject's DWI data are good enough for fiber tracking (if not, choose type 2)
- no deformation between repeats scans (if not, choose type 2)

**Example**: 
- human subject study with repeated scans before and after treatment

| **Steps** | Details  |
|-----------|------------|
| 1. **Generate GQI FIB Files** |  ```dsi_studio --action=rec --source=*.src.gz``` |
|  | 1a. [creating SRC files](/doc/gui_t1.html): make sure to have a quality check to make sure the quality is good |
|  | 1b. [generating FIB files](/doc/gui_t2.html): at Step T2b(1), please use GQI method to get native space FIB file. |
| 2. **Export Metrics** | ```dsi_studio --action=exp --source=*.fib.gz --export=dti_fa``` |
|  | 2a. open the FIB file of each **follow-up** scan at **[Step T3: Fiber Tracking]** |
|  | 2b. use the **[Export]** to save the dti_fa or qa map in a NIFTI file (e.g. sub1.followup.fa.nii.gz). |
| 3. **Optimize Tractography** | (optional manual checking) |
|  | 3a. open one baseline scan's FIB file at **[Step T3 Fiber Tracking]**  |
|  | 3b. restore default fiber tracking settings using **[Options][Restore Tracking Settings]**. |
|  | 3c. set **[Step T3c Options][Tracking Parameters][Terminate if]** to `1,000,000` seeds |
|  | 3d. click the **[Step T3d: Tracts][Fiber Tracking]** button to see if you can get a good quality whole-brain fiber tracking.<br> If not, check out the troubleshooting section of the [whole brain fiber tracking document](https://dsi-studio.labsolver.org/doc/gui_t3_whole_brain.html).  |
|  | 3e. find out the best parameters until getting a good quality of the whole-brain track.|
| 4. **Differential Tracking** | ```dsi_studio --action=trk --source=*_ses-01_dwi.src.gz.gqi.1.25.fib.gz --other_slices=*_ses-02_dwi.src.gz.gqi.1.25.fib.gz.dti_fa.nii.gz --dt_metric1=dti_fa --dt_metric2=*_ses-02_dwi --dt_threshold=0.2 --seed_count=10000000 --min_length=30 --output=*.tt.gz``` |
|  | 4a. for each subject, open their baseline scan's FIB file at **[Step T3 Fiber Tracking]**|
|  | 4b. use **[Slice][Insert Other Images]** and select the NIFTI file of the follow-up scan (e.g. sub1.followup.fa.nii.gz created above). |
|  | 4c. select dti_fa or qa at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics1]**. This assumes that the anisotropy in the baseline scan is larger than the followup.|
|  | 4d. select the loaded metric at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics2]** |
|  | 4e. adjust thresholds by setting **[Differential Tracking][Metric1>Metric2 Threshold]=0.1, 0.2, or 0.3**, which specify 10%, 20%, and 30% differences if [Threshold Type] is (m1-m2)/m1. For most metrics, the normal individual differences are around 10~20%. Higher threshold gives more specific results against individual variations. To use absolute value as the threshold, set the [Threshold Type] to **m1-m2**.|
|  | 4f. click on **[Step T3d Tracts][Fiber Tracking]** to get differential tractography.|


# Type 2: mapping longitudinal change in the template space

**Requirements**: 
- repeat scans of the same subject, e.g. before/after treatment 

**Example**: 
- animal in-vivo study with repeated scans before and after treatment (DWI not good enough for fiber tracking)
- human study which DWI data are not good enough for fiber tracking

| **Steps** | Details  |
|-----------|------------|
| 1. **Generate QSDR FIB Files** |  ```dsi_studio --action=rec --source=*.src.gz --method=7``` |
|  | 1a. [creating SRC files](/doc/gui_t1.html): make sure to have a quality check to make sure the quality is good |
|  | 1b. [generating FIB files](/doc/gui_t2.html): at Step T2b(1), please use QSDR method to get native space FIB file. |
| 2. **Export Metrics** | ```dsi_studio --action=exp --source=*.fib.gz --export=dti_fa``` |
|  | 2a. open the FIB file of **all** scans at **[Step T3: Fiber Tracking]** |
|  | 2b. use the **[Export]** to save the dti_fa or qa map in a NIFTI file (e.g. sub1.fa.nii.gz). |
| 3. **Differential Tracking** | ```dsi_studio --action=trk --source=0 --other_slices=sub1_baseline.dti_fa.nii.gz,sub1_followup.dti_fa.nii.gz --dt_metric1=sub1_baseline --dt_metric2=sub1_followup --dt_threshold=0.2 --seed_count=10000000 --min_length=30 --output=*.tt.gz```<br>0: ICBM152_adult<br>1: C57BL6_mouse<br>2: dHCP_neonate<br>3: INDI_rhesus<br>4: Pitt_marmoset<br>5: WHS_SD_rat |
|  | 4a. at **[Step T3 Fiber Tracking]**, choose the ICBM153_adult template for human studies and click on the Step T3 button. For animal studies, choose the corresponding animal template. |
|  | 4b. use **[Slice][Insert Other Images]** and select the NIFTI file of the baseline and follow-up metrics (dti_fa or qa) of a subject |
|  | 4c. select the baseline metrics at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics1]**. This assumes that the anisotropy in the baseline scan is larger than the followup.|
|  | 4d. select the follow-up metric at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics2]** |
|  | 4e. adjust thresholds by setting **[Differential Tracking][Metric1>Metric2 Threshold]=0.1, 0.2, or 0.3**, which specify 10%, 20%, and 30% differences if [Threshold Type] is (m1-m2)/m1. For most metrics, the normal individual differences are around 10~20%. Higher threshold gives more specific results against individual variations. To use absolute value as the threshold, set the [Threshold Type] to **m1-m2**.|
|  | 4f. click on **[Step T3d Tracts][Fiber Tracking]** to get differential tractography.|

# Type 3: mapping cross sectional change in the native space

**Requirements**: 
- age-sex-matched controls avilable
- DWI data good enough for fiber tracking

**Example**: 
- human case-control studies

| **Steps** | Details  |
|-----------|------------|
| 1. **Generate FIB Files** |  ```dsi_studio --action=rec --source=*.patients.src.gz ```<br> ```dsi_studio --action=rec --method=7 --source=*.controls.src.gz ``` |
|  | 1a. [creating SRC files](/doc/gui_t1.html): make sure to have a quality check to make sure the quality is good |
|  | 1b. [generating FIB files](/doc/gui_t2.html): at Step T2b(1), **choose GQI for patients and choose QSDR for controls** |
| 2. **Create Database File for Controls** | ```dsi_studio --action=atl --source=*.control.fib.gz --cmd=db --template=0 --demo=controls_age_sex.txt``` |
|  | 2a. [Create a database](https://dsi-studio.labsolver.org/doc/gui_cx.html) and inlucde **only controls** |
|  | 2b. Prepare a demographic file for the contgrols. The file can be space, tab, or comma-separated text file. example:<br>```age sex```<br>```32 1```<br>```29 0```<br>```45 0```<br>```25 0```|
|  | Associate database with demographics: Open the conenctometry database file in **[Step C2]** and load control subject's demographics using **[File][Open demographics]**. This step associates demographics with the controls in the database. Save the database using the [File] menu. **Before doing this step, I would use **[Step C3]** to open the db.fib.gz file and load the demographics, just to check if there is any mismatch.** |
| 3. **Differential Tracking** | ```dsi_studio --action=trk --source=*_ses-01_dwi.src.gz.gqi.1.25.fib.gz --other_slices=sub-control_only.dti_fa.db.fib.gz --dt_metric1=sub-control_only --dt_metric2=dti_fa --subject_demo=patient_age_sex.txt --dt_threshold=0.2 --seed_count=10000000 --min_length=30 --tip_iteration=16 --output=*.cross_sectional.tt.gz```<br>**patient_age_sex.txt is patients demographics file with an additional first column stroing FIB files's partial filename** |
|  | 4a. for each subject, open their baseline scan's FIB file at **[Step T3 Fiber Tracking]**|
|  | 4b. click **[Slice][Insert Other Images]** and select the database file created in the previous step. enter the patient's age and sex (e.g. 36 1 ). You may rename the FIB file to inform DSI Studio the age and sex of the subject. For example, 20220808_M029Y_XXXX.src.gz.gqi.fib.gz will inform DSI Studio that the subject is a 29-year-old male |
|  | 4c. select dti_fa or qa at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics1]**. This assumes that the anisotropy in the baseline scan is larger than the followup.|
|  | 4d. select the database metric at **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics2]** |
|  | 4e. adjust thresholds by setting **[Differential Tracking][Metric1>Metric2 Threshold]=0.1, 0.2, or 0.3**, which specify 10%, 20%, and 30% differences if [Threshold Type] is (m1-m2)/m1. For most metrics, the normal individual differences are around 10~20%. Higher threshold gives more specific results against individual variations. To use absolute value as the threshold, set the [Threshold Type] to **m1-m2**.|
|  | 4f. click on **[Step T3d Tracts][Fiber Tracking]** to get differential tractography.|


**TIPS**
If you don't have controls subjects, there are publicly available connectometry database available at https://brain.labsolver.org. However, most dMRI metrics (especially DTI metrics) are very sensitive to acquisition parameters, and likely you will get many false positive results just due to acquisition differences. The following are public available connectometry databases:
  - [HCP Aging](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EvdTx_lhJJBCmek2G0IfNhkBmr7CkGKU79H6JC1OH2aWmA?e=xtSbtb) (age: 36+ y)
  - [HCP Development](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 5-21 y)
  - [developing HCP (neonate)](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 20-44 weeks post-conception)
  - HCP young adult (to be constructed)
  - Grid258 (under construction)

# Type 4: mapping cross sectional change in the template space

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


- **Multi-metrics analysis**

The metrics we usually use include DTI's FA and GQI's QA, RDI, NRDI (see [interpretations](https://dsi-studio.labsolver.org/doc/how_to_interpret_dmri.html)). The following is the implication behind them:

- **FA** decreases during acute neuronal injury or chronic neurodegeneration. It has high sensitivity and low specificity because the decreases of FA can be due to vasogenic edeam, demyelination, inflammation, axonal loss. We often uses FA as the first-pass screening. 
- **QA** decreases when there is demyelination or axonal loss. It usually does NOT change at acute axonal injury or edema and thus is much more specific to axonal loss. In acute neuronal injury or inflammation, we may see FA decreasing with QA staying the same, potentially indicNating that the axonal injury is reversible.
- **RDI** increases when there is cell infiltration, which happens in tumor or during inflammation. You need to have multishell or DSI acquisitions to use this metric.
- **NRDI** increases when there is tissue edema. You need to have multishell or DSI acquisitions to use this metric.

We usually run differential fiber tracking on FA, QA, RDI, and NRDI, respectively. This will give a comprehensive clinical picture of the neuronal change. For more detailed discussion, please refer to [how to intepret dMRI metrics](/doc/how_to_interpret_dmri.html).

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

