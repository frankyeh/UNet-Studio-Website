# Differential Tractography

![image](https://user-images.githubusercontent.com/275569/147860577-35e5b242-2991-4cdf-b6f7-91161d8b0c73.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/EWOGQ3QTrnw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Differential tractography compares scans to capture neuronal change reflected by a decrease of anisotropy. Compared with conventional tractography, differential integrates the  "tracking-the-difference" paradigm as opposed to "tracking-the-existence" one used in the conventional setting. It is realized by adding one criterion to track along trajectories only if a decrease of anisotropy is found between repeat scans. This approach greatly increase the sensitivity and specificity of the diffusion metrics by aggregating results along white matter pathways. 

Differential tractography can be applied to DTI data, multi-shell data, and DSI data. But, we found that higher b-value signals will be more sensitive to early-stage neuronal changes, whereas low b-value signals may include a lot of physiological fluctuations. If your data are acquired at a low b-value (e.g., < 3000), then you may expect to have a higher false discovery rate (FDR). In the original study, we used 256-direction grid sampling with b-max=4000 or even up to 7000 to get excellent FDR values lower than 0.05. Using DTI data may increase FDR to 0.2.

Open the main window and click on [Step T3: Fiber Tracking] to select a GQI-reconstructed FIB file from [Step T1](/doc/gui_t1.html) and [Step T2](/doc/gui_t2.html). 

## 0. Quality check using whole-brain tracking

In the tracking parameters (right upper window), set **[Step T3c: Options][Tracking Parameters][Min length]** to "30 mm",  **[Terminate if]** to `100,000` seeds

Click the **[Step T3d: Tracts][Fiber Tracking]** button to see if you can get a good quality of whole-brain fiber tracking.

If there are too many noisy fibers, consider increasing the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.

If missing too many branches, considers lowering the **[Step T3c: Options][Tracking Parameters][Threshold]** or **[Min length]**.

You may also need to adjust other parameters (check out [Step T3 Whole brain fiber tracking](/doc/gui_t3_whole_brain.html) ) until you get a good quality of the whole-brain track.

## 1. Load metrics

A FIB file opened in **[Step T3: Fiber Tracking]** includes a list of metrics under the **[Slices]** droplist on the top of the 3D window. 

Although differential tractography can use any metrics, ***we recommend using NQA (normalized quantitative anisotropy) and FA to find neuronal changes***.

The **[Export]** menu allows for exporting a  metric as a NIFTI file, whereas the exported NIFTI files can be imported using **[Slices][Insert Other Images]**. 

For loading template images, use **[Slices][Insert MNI images]**. 

The followings are steps for cross-sectional and longitudinal studies, respectively.

- **for cross-sectional studies**

    We will compare subject's metrics with a group average template. You can [download templates](https://brain.labsolver.org/hcp_template.html) for comparison. 
    
    - If your data were acquired using HCP-style multishell, choose the ***HCP-1065 NQA*** or ***HCP-1065 FA*** templates. 
    - If your data were acquired using the [258-direction DSI](/doc/how_to_acquire_dmri.html), choose the ***Grid258 NQA*** or ***Grid258 FA*** templates. 
    - To use an age-sex adjusted template for your subject, download ***Grid258 NQA connectometry database*** and open it in ***[Step C2a]*** and select ***[File][Save Matched Image as]***. Input age and sex (1 for male, 0 for female) separated by a space to export the age-sex adjusted NQA template.
    
    Load the template image (e.g. template_nqa.nii.gz) using **[Slices][Insert MNI Images]**. The newly added metrics will be listed in the [Slices] droplist on the top of the 3D window, and the name will be the basename of the template file (i.e. template_nqa).
      
**TIP**

The ideal template should be constructed from your control subjects to avoid possible site differences. To create group-average images from a control group, follow the **[Step C1: Reconstruct SRC files for connectometry]** to generate ODF-containing FIB files. Then open [**Tools**][**P1: Create template/skeleton**] and select the ODF-containing FIB files of the control subjects to create a group-averaged template FIB file. The generated template FIB file can be opened in **[Step T3 Fiber Tracking]** and export metrics using **[Export].**   

    
- **for longitudinal studies**

    Export metrics from the follow-up FIB files using the **[Step T3][Export]**, and rename the exported files (e.g. followup_xxx.nii.gz) so that it won't be confused with the baseline metrics.
    
    Open the FIB file of the baseline study and load NIFTI files from the follow-up study. Now in the **[Slices]** droplist on the top of the 3D window will have both the metrics in the baseline and followup study 

## 2. Compare Metrics

Add a new tracking metric at **[Analysis][Add Tracking Metrics]** and input the names of two comparing metrics connected by a minus sign. 

For cross sectional study, input ***template_nqa-nqa*** to study the decrease of QA in the subject, and input ***nqa-template_nqa*** for increase of QA in the subject.

For longitudinal study, input ***nqa-followup_nqa*** to study the decrease of QA in the followup, and input ***followup_nqa-nqa*** for increase of QA in the followup.

A new differential tracking metrics will be added to the **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics]**

Differential tractography can compare any metrics stored in the NIFTI files. For example, we can load DKI_base.nii.gz and DKI_followup.nii.gz and compare their differences.  

<iframe width="560" height="315" src="https://www.youtube.com/embed/RkWui6NlLqw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## 3. Tracking the difference

Clear all tracks from the tract list using [Tracts][Delete Tracts][Delete all].

In the tracking parameters, set **[Step T3c: Options][Tracking Parameters][Differential Tracking][Metrics]** from *none* to the newly added comparison metric.

1. Set [Differential Tracking][Threshold]=0.2,

    0.1 means 10% increase or decrease, 0.2 means 20%. 

2. Set [Tracking Parameters][Min Length (mm)]=30

    Lower value like 20 mm is more sensitive, whereas 40 mm is more specific. 
    
3. Click [Step T3d][Fiber Tracking] to map the differential stratigraphy. 

4. Test different [Differential Tracking][Threshold] (e.g. 0.05, 0.10, ... 0.25) and [Tracking Parameters][Min Length (mm)] (20, 25, 30, 35, 40, 45)

    The goal is to maximize sensitivity while retaining specificity. The following example suggest [Min Length (mm)]=40 has the best trade-off.

    ![image](https://user-images.githubusercontent.com/275569/147860680-74abdce8-81a3-47a6-9d01-3d93be355b0d.png)


**TIPS**

- You can use [Edit][Pruning (TIP)] to eliminate noisy results. I will apply it for 5~10 times.

- Add ROA or ROI to limit findings. 

    For example, you can map the affected pathways that pass through the internal capsule by assigning the internal capsule as the ROI. The number and length of tracks can be compared between patients if other tracking parameters are fixed (be sure to fix the seed count).

- Avoid lower cerebellum due to different slice coverage.

- Use [Tracts][Miscellaneous][Recognize Track] to know the name of the findings.

- If tracking results change a lot in repeated analyses, it is likely that the image acquisition is not optimal (e.g. too noisy, has very thick slices), and thus registration errors are boosted. To minimize this variance, export both baseline and follow-up NQA images and smooth them using [Tool][O41 View image][Signals][Smoothing] (make sure to update DSI Studio to use this function). Save the smoothed images as new files to run differential tracking.

After smoothing, add the smoothed image back using [Slices][Add Other images] and continue with further analysis.

## 4. False discovery rate and statistical testing

One key question for differential tractography is the significance of the findings. For example, if we observe a lot of tracks showing up in differential tractography, how many of them are false positive? A way to quantifying this reliability is by calculating the false discovery rate from a group of patients and a group of control subjects. The following steps illustrate how this can be carried out in DSI Studio.

**Example 1: calculate the false discovery rate using control subjects**

1. Apply **identical** steps and parameters for N patients and N matched controls, respectively. 

2. Calculate false discovery rate (FDR) 

    if you can get a total of 1000 tracks from 5 patients and 10 tracks from 5 controls, then the false discovery rate of the findings in patients is 10/100 = 10%. An FDR lower than 0.05 can be considered as significant.

**Example 2: calculate the false discovery rate without control subjects** 

This is the alternative sham approach described in the original work in Yeh, Neuroimage, 2019.

1. Apply **identical** steps to all subjects. 

2. Apply **identical** steps to all subjects but with an opposite comparison metrics (e.g. for `follow_up_qa-qa`, the opposite is `qa-follow_up_qa` )

3. Calculate false discovery rate (FDR) 

    if you can get a total of 1000 tracks from 1. patients and 10 tracks from 2., then the false discovery rate of the findings is 10/100 = 10%. An FDR lower than 0.05 can be considered as significant.

