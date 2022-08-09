# Differential Tractography

![image](https://user-images.githubusercontent.com/275569/147860577-35e5b242-2991-4cdf-b6f7-91161d8b0c73.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/EWOGQ3QTrnw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Differential tractography compares scans to capture neuronal change reflected by a decrease of anisotropy. Compared with conventional tractography, differential integrates the  "tracking-the-difference" paradigm as opposed to the "tracking-the-existence" one used in the conventional setting. It is realized by adding one criterion to track along trajectories only if a decrease of anisotropy is found between repeat scans. This approach greatly increases the sensitivity and specificity of the diffusion metrics by aggregating results along white matter pathways. 

![image](https://user-images.githubusercontent.com/275569/170849962-ef2f90af-748a-4011-8610-508fa8e24645.png)


Differential tractography can be applied to DTI data, multi-shell data, and DSI data. In practice, we will use both DTI and GQI metrics to study the neronal change. Each of the metrics has its intepretation. Moreover, we found that higher b-value signals will be more sensitive to early-stage neuronal changes, whereas low b-value signals may include a lot of physiological fluctuations. If data are acquired at a low b-value (e.g., < 3000), then you may expect to have a higher false discovery rate (FDR). In the original study, we used 256-direction grid sampling with b-max=4000 or even up to 7000 to get excellent FDR values lower than 0.05. Using DTI data may increase FDR to 0.2.

## Step dT0: Prepare a FIB file

**The QA calculation was revised on Aug, 2022, if you have earlier version of DSI Studio, please update it**

First, we need a FIB file as the tracking framework. The FIB file is usually constructed from the subject's scan (most common).

To generate the subject's FIB file, please follows steps to get a GQI-reconstructed FIB file, including

- Step T1: [creating SRC files](/doc/gui_t1.html)
- Step T2: [generating FIB files](/doc/gui_t2.html). At Step T2B(1), please use GQI method to get native space FIB file.

If the individual scans are not good enough for tracking (e.g., in-vivo animal scans), then an existing [population-averaged template (FIB.GZ)](https://brain.labsolver.org/hcp_template.html) can be used instead. If you cannot find a suitable template, please feel free to contact Frank to identify one.

## Step dT1: Prepare subject metrics

The metrics we usually use include DTI's FA and GQI's QA, RDI, NRDI. The following is the implication behind them:

- **FA** decreases during acute neuronal injury or chronic neurodegeneration. It has a moderate sensitivity and is "nonspecific" because the decreases of FA can be due to vasogenic edeam, demyelination, inflammation, axonal loss. We often uses FA as the first-pass screening. 
 
- **QA** decreases when there is demyelination or axonal loss. It usually does NOT change at acute axonal injury or edema and thus is much more specific than FA. In acute neuronal injury or inflammation, we may see FA decreasing with QA staying the same, potentially indicNating that the axonal injury is reversible.
- **RDI** increases when there is cell infiltration, which happens in tumor or during inflammation. You need to have multishell or DSI acquisitions to use this metric.
- **NRDI** increases when there is tissue edema. You need to have multishell or DSI acquisitions to use this metric.

We usually run differential fiber tracking on FA, QA, RDI, and NRDI, respectively. This will give a comprehensive clinical picture of the neuronal change. For more detailed discussion, please refer to [how to intepret dMRI metrics](/doc/how_to_interpret_dmri.html).

After opening the FIB file in **[Step T3: fiber tracking]**, all metrics that can be compared are listed under the Slices droplist: 

<img src="https://user-images.githubusercontent.com/275569/183502862-fbf8b003-8239-425b-b5cc-bfcf321fd91e.png" width="400"/>

You can export any of them to a NIFTI file using the **[Export]** menu. 

A new metric can be added to the list from a NIFTI file:
  - If the NIFTI file is already in subject's native slice, you can insert it using **[Slices][Insert Other Images]**.
  - If the NIFTI file is in the template space (presumbly ICBM152 2009), you can insert it using **[Slices][Insert MNI images]**. DSI Studio will apply nonlinear registration to warp the image to subject's native space.

**If you are using DSI Studio with a version dated earlier than 5/28/2022, please update DSI Studio to reduce the misalignment errors.**
**Make sure to add a prefix or postfix to the NIFTI file name so that after loading them, they will not be confused with the existing metrics** 

## Step dT2: Prepare normative values for comparison

The subject's metrics will be compared with normative values. For example, to know whether a subject's FA decreases at a pathways, we need a normal FA map to know that is the normal values for FA. 

There are several ways to get the normative values:

- Step dT2a: If you are conducting a longitudinal study, the perfect normal values are from baseline scans. You can export the metrics from baseline FIB file as NIFTI files, which can be loaded in a follow-up FIB file for comparison.
- Step dT2b: If you have controls subjects, then [create a connectometry database](https://dsi-studio.labsolver.org/doc/gui_cx.html) from your control subjects. Once you have the connectometry database created, there are two ways that DSI Studio can generate age-sex-matched metrics for each of your subjects. 
  - Step dT2b(1): If you used DSI Studio to rename DICOM and generate the FIB file, the FIB file's filename name will look like this: 20220808_M029Y_XXXX.src.gz.gqi.fib.gz, which indicates the subject is a 29-year-old male. Both the connectometry database and your subject's FIB file will thus carry age and sex information. Once you create a connectometry database (db.fib.gz), you can directly insert it to any subject's FIB file using [Slices][Insert Other Images] and DSI Studio will automatically add an metrics matching the subject's age and sex.
  - Step dT2b(2): If your FIB file does not include age sex information in the file name, or if you have other demographics to be considered. There are two additional steps needed to tell DSI Studio the demographics of your control and study subjects. First, open the conenctometry database file in ***[Step C2]*** and load subject's demographics using ***[File][Open demographics]***. This step associated demographics with the controls in the database. Then in the same Window, select ***[File][Save Matched Image as]*** and input the demographics of a subject to be matched. The demographics values need to be separated by a space. Then DSI Studio will save age-sex-matched metric as a NIFTI file, which can be loaded In Step T3 using **[Slices][Insert MNI images]**. Each subject will need his/her own age-sex-matched NIFTI file.
- Step dT2c: If you don't have controls subjects, there are publicly available connectometry database available at https://brain.labsolver.org. However, most dMRI metrics (especially DTI metrics) are very sensitive to acquisition parameters, and likely you will get many false positive results just due to acquisition differences. The following are public available connectometry databases:
  - [HCP Aging](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EvdTx_lhJJBCmek2G0IfNhkBmr7CkGKU79H6JC1OH2aWmA?e=xtSbtb) (age: 36+ y)
  - [HCP Development](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 5-21 y)
  - [developing HCP (neonate)](https://pitt-my.sharepoint.com/:f:/g/personal/yehfc_pitt_edu/EgTq8mpY5zZEhKhwHhZMbPABMzRLckaiaRnwm4tMWSg3Fw?e=4m95Mf) (age: 20-44 weeks post-conception)
  - HCP young adult (to be constructed)
  - Grid258 (under construction)

## Step dT3: Quality check on the FIB file using whole-brain tracking

After loading a needed metrics in [Step T3: fiber tracking], we need to first check if the fiber tracking framework looks okay.

First, restore default settings using **[Options][Restore Tracking Settings]**

In the tracking parameters (right upper window), set **[Step T3c: Options][Tracking Parameters][Min length]** to "30 mm",  **[Terminate if]** to `1,000,000` seeds

Click the **[Step T3d: Tracts][Fiber Tracking]** button to see if you can get a good quality whole-brain fiber tracking 

If there are too many noisy fibers, consider increasing the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.

If missing too many branches, considers lowering the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.

Adjust other parameters until you get a good quality of the whole-brain track. (You may check out [whole brain fiber tracking](/doc/gui_t3_whole_brain.html) to see how to evaluate the tractography quality and adjust parameters)

## Step dT4: Compare metrics

After loading the external NIFTI files or connectometry db, all metrics that can be compared should appear in the **[Slices]** droplist on the top of the 3D window.

<img src="https://user-images.githubusercontent.com/275569/183502862-fbf8b003-8239-425b-b5cc-bfcf321fd91e.png" width="400"/>

Click on the top menu **[Analysis][Add Tracking Metrics]** and input the equation for comparing the metrics: 

For example, if you have two metrics to be compared named as ***qa*** and ***normal_qa***. Input ***normal_qa-qa*** to map pathways with ***qa*** lower than ***normal_qa***. 

A new differential tracking metrics will be added to the **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics]**

Differential tractography can compare any metrics stored in the NIFTI files. For example, we can load DKI_base.nii.gz and DKI_followup.nii.gz and compare their differences.  

<iframe width="560" height="315" src="https://www.youtube.com/embed/RkWui6NlLqw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Step dT5: Differential fiber tracking

Clear all tracks from the tract list using [Tracts][Delete Tracts][Delete all].

In the tracking parameters, set **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics]** from *none* to the newly added comparison metric.

1. Set **[Differential Tracking][Threshold]=0.2**, which specify 20% differences. For most metrics, the normal individual differences are around 10~20%. Higher threshold gives more specific results against individual variations.
2. Set **[Tracking Parameters][Min Length (mm)]=30**. For animal studies, you may need to use a smaller value (e.g. 5). A lower value is more sensitive to short-ranged changes. 
3. Click [Step T3d][Fiber Tracking] to map the differential stratigraphy. 


I would recommend checking a rnage of [Differential Tracking][Threshold] (e.g. 0.1, 0.2, 0.3, 0.4). The goal is to maximize sensitivity while retaining specificity. 

![image](https://user-images.githubusercontent.com/275569/147860680-74abdce8-81a3-47a6-9d01-3d93be355b0d.png)


**TIPS**

- **Add ROA or ROI to limit findings**: You can map the affected pathways that pass through the internal capsule by assigning the internal capsule as the ROI. The number and length of tracks can be compared between patients if other tracking parameters are fixed (be sure to fix the seed count).
- **Exclude cerebellum**: Add a region from [Atlas][BrainSeg][Cerebellum] and assign it as ROA.
- **Segment results into bundles**: you can use [Tracts][Miscellaneous][Recognize Track] to recognize the name of the bundles.
- If tracking results change a lot in repeated analyses, it is likely that the image acquisition is not optimal (e.g. too noisy, has very thick slices), and thus registration errors are boosted. To minimize this variance, export both baseline and follow-up NQA images and smooth them using [Tool][O41 View image][Signals][Smoothing] (make sure to update DSI Studio to use this function). Save the smoothed images as new files to run differential tracking.

After smoothing, add the smoothed image back using [Slices][Add Other images] and continue with further analysis.

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

