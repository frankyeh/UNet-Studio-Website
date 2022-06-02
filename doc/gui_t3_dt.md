# Differential Tractography

![image](https://user-images.githubusercontent.com/275569/147860577-35e5b242-2991-4cdf-b6f7-91161d8b0c73.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/EWOGQ3QTrnw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Differential tractography compares scans to capture neuronal change reflected by a decrease of anisotropy. Compared with conventional tractography, differential integrates the  "tracking-the-difference" paradigm as opposed to the "tracking-the-existence" one used in the conventional setting. It is realized by adding one criterion to track along trajectories only if a decrease of anisotropy is found between repeat scans. This approach greatly increases the sensitivity and specificity of the diffusion metrics by aggregating results along white matter pathways. 

![image](https://user-images.githubusercontent.com/275569/170849962-ef2f90af-748a-4011-8610-508fa8e24645.png)


Differential tractography can be applied to DTI data, multi-shell data, and DSI data. However, we found that higher b-value signals will be more sensitive to early-stage neuronal changes, whereas low b-value signals may include a lot of physiological fluctuations. If data are acquired at a low b-value (e.g., < 3000), then you may expect to have a higher false discovery rate (FDR). In the original study, we used 256-direction grid sampling with b-max=4000 or even up to 7000 to get excellent FDR values lower than 0.05. Using DTI data may increase FDR to 0.2.

Open the main window and click on [Step T3: Fiber Tracking] to select a GQI-reconstructed FIB file from [Step T1](/doc/gui_t1.html) and [Step T2](/doc/gui_t2.html). 

## Data Preparation 

We first need to identify two key data elements in differential tractography:

### 0a. A FIB file 
A FIB file is needed as the tracking framework. The FIB file can be constructed from the subject's baseline scan (most common).

If the individual scans are not good enough for tracking (e.g., in-vivo animal scans), then an existing [population-averaged template (*.FIB.GZ)](https://brain.labsolver.org/hcp_template.html) can be used instead. If you cannot find a suitable template, please feel free to contact Frank to identify one.

### 2. Metrics to be compared

The metrics can be those stored within a subject's FIB file or from a NIFTI file exported from another FIB (e.g. same subject's follow-up scans) or any source. The **[Export]** menu allows for exporting a metric as a NIFTI file from a FIB file. If the FIB file is reconstructed by GQI, the exported metrics is in the native space. If the FIB file is reconstructed by QSDR, the exported metrics is stored in the MNI space. 

For cross-sectional studies, you can generate an age-sex matched NIFTI file for each subject. First you will need to [create a connectometry database](https://dsi-studio.labsolver.org/doc/gui_cx.html) using your control subjects. Then open the database file in ***[Step C2]*** and load demographics using ***[File][Open demographics]***. Select ***[File][Save Matched Image as]***. Input the matching demographics separated by a space to export the matched metric as an NIFTI file.


If your data were acquired using the [258-direction GRID](/doc/how_to_acquire_dmri.html), you can use a publicly available [***Grid258 NQA connectometry database***]. 

Examples:
|Study Type | FIB file | Baseline metrics | Baseline source | Follow-up metrics | Follow-up source |
|----------|--------|------------------|------------------|----------------|-----------------|
| Longitudinal | Subject's baseline FIB | `nqa` in FIB file | in the baseline FIB file | `nqa` NIFTI file | exported from the GQI-reconstructed FIB file constructed from follow-up scan |
| Longitudinal| HCP1065.2mm.fib.gz (from brain.labsolver.org) |  Subject's baseline `nqa` NIFTI file in ICBM152 space | exported from QSDR-reconstructed FIB files | Subject's follow-up `nqa` NIFTI file in ICBM152 space in ICBM152 space | exported from QSDR-reconstructed FIB files |
| Cross-sectional | Subject's baseline FIB | age-sex-matched control `nqa` in the MNI space | generated from healthy controls's connectometry database | `nqa`  | in the subject's FIB file |

## Quality check on FIB file using whole-brain tracking

Open the FIB file in [Step T3: fiber tracking], restore default settings using **[Options][Restore Tracking Settings]**

In the tracking parameters (right upper window), set **[Step T3c: Options][Tracking Parameters][Min length]** to "30 mm",  **[Terminate if]** to `100,000` seeds

Click the **[Step T3d: Tracts][Fiber Tracking]** button to see if you can get a good quality whole-brain fiber tracking 

If there are too many noisy fibers, consider increasing the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.

If missing too many branches, considers lowering the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.

Adjust other parameters until you get a good quality of the whole-brain track. (You may check out [whole brain fiber tracking](/doc/gui_t3_whole_brain.html) to see how to evaluate the tractography quality and adjust parameters)

## Load metrics

**If you are using DSI Studio with a version dated earlier than 5/28/2022, please update DSI Studio to reduce the misalignment errors.**


A FIB file opened in **[Step T3: Fiber Tracking]** includes a list of metrics under the **[Slices]** droplist on the top of the 3D window. A typical list includes `qa`, `nqa`, `dti_fa`, ...etc. Those metrics are ready to be used. ***we recommend using NQA (normalized quantitative anisotropy) or DTI_FA to find neuronal changes***.

An external native-space NIFTI files can be imported by **[Slices][Insert Other Images]**. DSI Studio will ask whether a rotation alignment is needed. In most cases, you should choose yes, and DSI Studio will alignment the image with the subject's existing scans. 

An MNI-space NIFTI file can be loaded by **[Slices][Insert MNI images]**. DSI Studio will apply nonlinear registration to warp the image to subject's native space.

After loading the external NIFTI files, they should appear in the **[Slices]** droplist on the top of the 3D window.

## 2. Compare Metrics

Add a new tracking metric at **[Analysis][Add Tracking Metrics]** and input the names of two comparing metrics connected by a minus sign. 

For cross-sectional study, input ***external_nqa-nqa*** to study the decrease of QA in the subject, and input ***nqa-external_nqa*** for increase of QA in the subject. Here ***external_nqa*** is the name of the metric loaded from the external NIFTI file. Be default, DSI Studio will use file name as the metrics name.

For a longitudinal study, input ***nqa-followup_nqa*** to study the decrease of QA in the follow-up, and input ***followup_nqa-nqa*** for increase of QA in the follow-up. Here ***followup_nqa*** is the name of the metric loaded from the external NIFTI file. Be default, DSI Studio will use file name as the metrics name.

A new differential tracking metrics will be added to the **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics]**

Differential tractography can compare any metrics stored in the NIFTI files. For example, we can load DKI_base.nii.gz and DKI_followup.nii.gz and compare their differences.  

<iframe width="560" height="315" src="https://www.youtube.com/embed/RkWui6NlLqw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## 3. Tracking the difference

Clear all tracks from the tract list using [Tracts][Delete Tracts][Delete all].

In the tracking parameters, set **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics]** from *none* to the newly added comparison metric.

1. Set [Differential Tracking][Threshold]=0.2,

    0.1 means 10% increase or decrease, 0.2 means 20%. 

2. Set [Tracking Parameters][Min Length (mm)]=30

   For animal studies, you may need to use a smaller value (e.g. 5)

    A lower value like 20 mm is more sensitive, whereas 40 mm is more specific. 
    
3. Click [Step T3d][Fiber Tracking] to map the differential stratigraphy. 

4. Test different [Differential Tracking][Threshold] (e.g. 0.05, 0.10, ... 0.25) and [Tracking Parameters][Min Length (mm)] (20, 25, 30, 35, 40, 45)

    The goal is to maximize sensitivity while retaining specificity. The following example suggests [Min Length (mm)]=40 has the best trade-off.

    ![image](https://user-images.githubusercontent.com/275569/147860680-74abdce8-81a3-47a6-9d01-3d93be355b0d.png)


**TIPS**

- Add ROA or ROI to limit findings. 

    For example, you can map the affected pathways that pass through the internal capsule by assigning the internal capsule as the ROI. The number and length of tracks can be compared between patients if other tracking parameters are fixed (be sure to fix the seed count).

- Avoid lower cerebellum due to different slice coverage.

- Use [Tracts][Miscellaneous][Recognize Track] to know the name of the findings.

- Any misalignment between the comparing metrics (due to either distortion or deformation) will lead to false results. To minimize this problem, export two comparing metrics and use [Tools][R2: Nonlinear Registration Toolbox] and its [Save Warpped Image] to reduce the misalignment issue.

- If tracking results change a lot in repeated analyses, it is likely that the image acquisition is not optimal (e.g. too noisy, has very thick slices), and thus registration errors are boosted. To minimize this variance, export both baseline and follow-up NQA images and smooth them using [Tool][O41 View image][Signals][Smoothing] (make sure to update DSI Studio to use this function). Save the smoothed images as new files to run differential tracking.

After smoothing, add the smoothed image back using [Slices][Add Other images] and continue with further analysis.

## 4. False discovery rate and statistical testing

One key question for differential tractography is the significance of the findings. For example, if we observe a lot of tracks showing up in differential tractography, how many of them are false positive? A way to quantify this reliability is by calculating the false discovery rate from a group of patients and a group of control subjects. The following steps illustrate how this can be carried out in DSI Studio.

**Example 1: calculate the false discovery rate using control subjects**

1. Apply **identical** steps and parameters for N patients and N matched controls, respectively. 

2. Calculate false discovery rate (FDR) 

    if you can get a total of 1000 tracks from 5 patients and 10 tracks from 5 controls, then the false discovery rate of the findings in patients is 10/100 = 10%. An FDR lower than 0.05 can be considered as significant.

**Example 2: calculate the false discovery rate without control subjects** 

This is the alternative sham approach described in the original work in Yeh, Neuroimage, 2019.

1. Apply **identical** steps to all subjects. 

2. Apply **identical** steps to all subjects but with an opposite comparison metrics (e.g. for `follow_up_qa-qa`, the opposite is `qa-follow_up_qa` )

3. Calculate false discovery rate (FDR) 

    If you can get a total of 1000 tracks from 1. patients and 10 tracks from 2., then the false discovery rate of the findings is 10/100 = 10%. An FDR lower than 0.05 can be considered significant.

