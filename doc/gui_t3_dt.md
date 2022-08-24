# Differential Tractography

![image](https://user-images.githubusercontent.com/275569/147860577-35e5b242-2991-4cdf-b6f7-91161d8b0c73.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/EWOGQ3QTrnw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Differential tractography compares scans to capture neuronal change reflected by a decrease of anisotropy. Compared with conventional tractography, differential integrates the  "tracking-the-difference" paradigm as opposed to the "tracking-the-existence" one used in the conventional setting. It is realized by adding one criterion to track along trajectories only if a decrease of anisotropy is found between repeat scans. This approach greatly increases the sensitivity and specificity of the diffusion metrics by aggregating results along white matter pathways. 

![image](https://user-images.githubusercontent.com/275569/170849962-ef2f90af-748a-4011-8610-508fa8e24645.png)


Differential tractography can be applied to DTI data, multi-shell data, and DSI data. In practice, we will use both DTI and GQI metrics to study the neronal change. Each of the metrics has its intepretation. Moreover, we found that higher b-value signals will be more sensitive to early-stage neuronal changes, whereas low b-value signals may include a lot of physiological fluctuations. If data are acquired at a low b-value (e.g., < 3000), then you may expect to have a higher false discovery rate (FDR). In the original study, we used 256-direction grid sampling with b-max=4000 or even up to 7000 to get excellent FDR values lower than 0.05. Using DTI data may increase FDR to 0.2.

## Step dT1: Prepare a FIB file

**The calculation of QA was revised on Aug, 2022 (replaced by nQA), if you have earlier version of DSI Studio, please update it**

First, we need a FIB file that will be used as the tracking framework. There are two choices: native FIB and template FIB.

1. **Native FIB:** For human studies, the FIB file is usually constructed from the subject's own scan because of substantial individual differences. To generate the subject's FIB file, please follows steps to get a GQI-reconstructed FIB file, including [creating SRC files](/doc/gui_t1.html) and [generating FIB files](/doc/gui_t2.html). At Step T2B(1), please use GQI method to get native space FIB file.
2. **Template FIB:** For animal studies, often the scans are not good enough for tracking, and thus using the template FIB as the "common tracking framework" would be a better choice. DSI Studio after the August 23 2022 version provides built-in template FIB for human and animals. To use them, select the appropriate template FIB at [Step T3 Fiber Tracking][Action] and click on the [Step T3] button.


## [Optional but recommended] Quality check using whole-brain tracking

We can use whole brain tracking to check if the fiber tracking framework has good quality for differential tracking.

First, restore default settings using **[Options][Restore Tracking Settings]**. Then in the tracking parameters (right upper window), set **[Terminate if]** to `1,000,000` seeds and click the **[Step T3d: Tracts][Fiber Tracking]** button to see if you can get a good quality whole-brain fiber tracking 

If there are too many noisy fibers, consider increasing the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.
If missing too many branches, considers lowering the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.

Adjust other parameters until you get a good quality of the whole-brain track. (You may check out [whole brain fiber tracking](/doc/gui_t3_whole_brain.html) to see how to evaluate the tractography quality and adjust parameters)

## Step dT1: Load metrics for comparison

The metrics we usually use include DTI's FA and GQI's QA, RDI, NRDI. The following is the implication behind them:

- **FA** decreases during acute neuronal injury or chronic neurodegeneration. It has a moderate sensitivity and is "nonspecific" because the decreases of FA can be due to vasogenic edeam, demyelination, inflammation, axonal loss. We often uses FA as the first-pass screening. 
- **QA** decreases when there is demyelination or axonal loss. It usually does NOT change at acute axonal injury or edema and thus is much more specific to axonal loss. In acute neuronal injury or inflammation, we may see FA decreasing with QA staying the same, potentially indicNating that the axonal injury is reversible.
- **RDI** increases when there is cell infiltration, which happens in tumor or during inflammation. You need to have multishell or DSI acquisitions to use this metric.
- **NRDI** increases when there is tissue edema. You need to have multishell or DSI acquisitions to use this metric.

We usually run differential fiber tracking on FA, QA, RDI, and NRDI, respectively. This will give a comprehensive clinical picture of the neuronal change. For more detailed discussion, please refer to [how to intepret dMRI metrics](/doc/how_to_interpret_dmri.html).

There are several different approaches for differential fiber tracking. Each of them has its own application scenario. Their steps are detailed in the following:

### **Approach 1: mapping neuronal change in longitudinal studies:**

The first approach is applicable to longitudinal studies, such as those with pre- and post- treatment scans. Each subject will have baseline and followup scans at two different time point. The following is the steps to obtain differential tractography based on FA.

0. ***Preprocessing:*** [Create SRC files](/doc/gui_t1.html) from DICOM or NIFTI files and [Reconstruct FIB files](/doc/gui_t2.html) using GQI or QSDR. GQI reconstructs in the native space and is the method of choice for human studies. QSDR reconstruct in the template space and is the method of choice for animal studies. Complete this step for each of the MRI scan. 
1. ***Select tracking framework:*** For GQI-FIB, open baseline scan's FIB file at **[Step T3 Fiber Tracking]** as the tracking framework. For QSDR-FIB, select the **built-in template FIB** at [Step T3: Fiber Tracking][Action] and click on the [Step T3: Fiber Tracking].
2. ***Select metric 1:*** For GQI-FIB, the FIB file has included baseline scan's metrics such as FA, QA, RDI, ...etc. Select the metric you would like to compare at **[Step T3c: Options][Tracking Parameters][Differential Tractography][Metrics1]**. For QSDR-FIB, the built-in template FIB does not have you scan's metrics. Thus you will need to export them from baseline's FIB file by opening the baseline FIB file at **[Step T3 Fiber Tracking]** and export the metrics using the **[Export]** menu on the top. I would save the metrics with a file name such as baseline_fa.nii.gz to avoid confusion. The exported NIFTI files can then be loaded using **[Slices][Insert Other Images]**
3. ***Select metric 2:*** For both GQI-FIB and QSDR-FIB, export followup scan's metric in a NIFTI file by opening the followup FIB file and using the **[Export]** to save the metric map in a file name that clearly marks its origin to avoid confusion (e.g. followup_fa.nii.gz). Now we can insert the exported metric to our tracking framework using **[Slice][Insert Other Images]**. Select the loaded metric at **[Step T3c: Options][Tracking Parameters][Differential Tractography][Metrics2]**. The loaded NIFTI files will be listed using its file name.
4. ***Adjust thresholds:*** Set **[Differential Tracking][Metric1>Metric2 Threshold]=0.1, 0.2, or 0.3**, which specify 10%, 20%, and 30% differences. For most metrics, the normal individual differences are around 10~20%. Higher threshold gives more specific results against individual variations. To use absolute value as the threshold, set the [Threshold Type] to **m1-m2**.
5. ***Differential fiber tracking:*** Click on **[Step T3d Tracts][Fiber Tracking]** to get differential tractography.

I would recommend checking a range of [Metric1>Metric2 Threshold] (e.g. 0.1, 0.2, 0.3, 0.4) and eliminate fregments by increasing [Step T3c:Options][Tracking Prameters][Min Length]. The goal is to maximize sensitivity while retaining specificity. 

![image](https://user-images.githubusercontent.com/275569/147860680-74abdce8-81a3-47a6-9d01-3d93be355b0d.png)

### **Approach 2: comparing each human subject scan with a normative value:**

The second approach compares subject's metrics with normative values and is applicable to study that only acquires one scan for a subject. The steps are mostly identical to Approach 1 except for the ***Select metric 1:*** step, in which we need to get normative values as the baseline metrics. 

There are several ways to get the normative values as the metric 1:

#### Normative values from control subjects
If you have a group of control subjects, DSI Studio can use them to create a sex-age-matched normative metric matching each of the study subject. The steps are the following:
  - ***[Create a connectometry database](https://dsi-studio.labsolver.org/doc/gui_cx.html):*** from your control subjects. 
  - ***Associate data with demographics:*** Open the conenctometry database file in **[Step C2]** and load control subject's demographics using **[File][Open demographics]**. This step associate demographics with the controls in the database. ***TIP 1*** You can save the db.fib.gz after loading the demographics so that the connectometry database will be imbued with demographics. There is no need to repeat this step again. ***TIP 2*** Before doing this step, I would use **[Step C3]** to open the db.fib.gz file and load the demographics, just to check if there is any mismatch.
  - ***Generated demographic-matched baseline metrics:***. Then in the same Step C2 window, select **[File][Save Matched Image as]** and input the demographics of a subject to be matched. The demographics values need to be separated by a space. If your demographics include age and sex (0: female 1:male), then an example of the input text is **63,1** which will generate a 63-year-old male control subject metric. 

 
#### Normative values from existing database
If you don't have controls subjects, there are publicly available connectometry database available at https://brain.labsolver.org. However, most dMRI metrics (especially DTI metrics) are very sensitive to acquisition parameters, and likely you will get many false positive results just due to acquisition differences. The following are public available connectometry databases:
  - [HCP Aging](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EvdTx_lhJJBCmek2G0IfNhkBmr7CkGKU79H6JC1OH2aWmA?e=xtSbtb) (age: 36+ y)
  - [HCP Development](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 5-21 y)
  - [developing HCP (neonate)](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 20-44 weeks post-conception)
  - HCP young adult (to be constructed)
  - Grid258 (under construction)

## TIPS

- **Load MNI space metric to the native space**: If the NIFTI file is in the template space (presumbly ICBM152 2009) and you are using GQI-FIB, you can insert MNI-space NIFTI using **[Slices][Insert MNI images]**. DSI Studio will apply nonlinear registration to warp the image to subject's native space.
- **Use filename to avoid confusion**: Make sure to add a prefix or postfix to the NIFTI file name so that after loading them, they will not be confused with the existing metrics 
- **Add ROA or ROI to limit findings**: You can map the affected pathways that pass through the internal capsule by assigning the internal capsule as the ROI. The number and length of tracks can be compared between patients if other tracking parameters are fixed (be sure to fix the seed count).
- **Exclude cerebellum**: Add a region from [Atlas][BrainSeg][Cerebellum] and assign it as ROA.
- **Segment results into bundles**: you can use [Tracts][Miscellaneous][Recognize Track] to recognize the name of the bundles.
- **Apply smoothing to metrics**: If tracking results change a lot in repeated analyses, it is likely that the image acquisition is not optimal (e.g. too noisy, has very thick slices), and thus registration errors are boosted. To minimize this variance, export both baseline and follow-up NQA images and smooth them using [Tool][O41 View image][Signals][Smoothing] (make sure to update DSI Studio to use this function). Save the smoothed images as new files to run differential tracking. After smoothing, add the smoothed image back using [Slices][Add Other images] and continue with further analysis.
- **Load demographic-imbued connectometry databse in [Slice][Insert Other Image]**: Once the connectometry database is imbued with demographics, you can use [Slice][Insert Other Images]. To further tell DSI Studio the age and sex, you can rename the FIB file to inform DSI Studio age and sex of the subject. An example of the filename is **20220808_M029Y_XXXX.src.gz.gqi.fib.gz**, which tells that the subject is a 29-year-old male.

## False discovery rate and statistical testing

One key question for differential tractography is the significance of the findings. For example, if we observe a lot of tracks showing up in differential tractography, how many of them are false positive? A way to quantify this reliability is by calculating the false discovery rate from a group of patients and a group of control subjects. The following steps illustrate how this can be carried out in DSI Studio.

**Example 1: calculate the false discovery rate using control subjects**

1. Apply **identical** steps and parameters for N patients and N matched controls, respectively. 
2. Calculate false discovery rate (FDR): if you can get a total of 1000 tracks from 5 patients and 10 tracks from 5 controls, then the false discovery rate of the findings in patients is 10/100 = 10%. An FDR lower than 0.05 can be considered as significant.

**Example 2: calculate the false discovery rate without control subjects** 

This is the alternative sham approach described in the original work in Yeh, Neuroimage, 2019.

1. Apply **identical** steps to all subjects. 
2. Apply **identical** steps to all subjects but with an opposite comparison metrics (e.g. for `follow_up_qa-qa`, the opposite is `qa-follow_up_qa` )
3. Calculate false discovery rate (FDR): If you can get a total of 1000 tracks from 1. patients and 10 tracks from 2., then the false discovery rate of the findings is 10/100 = 10%. An FDR lower than 0.05 can be considered significant.

