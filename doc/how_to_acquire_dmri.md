## Issues in HCP-Style Diffusion MRI Acquisitions

Multi-shell acquisition, especially the HCP-style 3-shell acquisition, is currently the most popular choice for "beyond-DTI" acquisition. The HCP-style multishell acquisition samples three b-values with 90-90-90 directions. However, the HCP acquisition has two issues:

- Suboptimal sampling scheme:

The 90 directions at the low b-value shell are over-sampled because most of the 90 DWI signals are redundant and can be readily interpolated by neighboring DWIs in the same shell. On the other hand, the high b-value shell does not have enough sampling directions. The correlation between the neighboring DWI is much lower, and more directions can be added. **An optimal setting should have the same redundancy for each shell**, which means high b-value shells should have more sampling directions, whereas the low b-value should have fewer directions.

- Orientation bias: 

The 90 directions of each shell is not equally distributed on the sphere. Consequently, the acquisition has a substantial orientational bias, and the reproducibility will be lower if head orientation is different. The problem is that the original HCP directions tried to avoid the same direction at different shells, but it is unnecessary because each shell can be viewed as different "bandwidth" for differentiating fast and slow diffusion. A sampling direction with good rotation invariance is essential for achieving good reproducibility and low rotation variance. 

## My recommendation: 23 b-values with b-max=4,000 at 258 directions

My recommendation is a 12-minute "grid-258" sampling with a maximum b-value of 4000, which acquires not just two or three b-values,
but 23 different b-values ranging from b=0 to b=4000 at a total of 258 directions. The low b-value range has fewer sampling compared to HCP multishell,
making the entire acquisition much more efficient. Moreover, the scheme reaches a higher b-value to 4,000 so that it captures restricted diffusion much better. 

This grid scheme addresses the issues of the HCP-style acquisition mentioned above.

> **Using a multiband sequence (e.g., CMRR) with an MB factor of 4, this 2-mm 258-direction dMRI acquisition can be completed in 12 minutes.**  

*The grid sampling has several benefits:*
- It has uniformly distributed density in the diffusion encoding space (i.e., q-space) and does not have the sampling homogeneity problem in the shell acquisitions. 
- The sampling is more efficient by avoiding over-sampling at low b-values or under-sampling at high b-values. 
- It can be reconstructed by DTI, ball-and-sticks model, NODDI, GQI...etc.
- It captures a continuous range of diffusion patterns from non-restricted diffusion to restricted diffusion. The grid scheme can capture all possible diffusion changes due to edematous tissue or cell infiltration for clinical studies. In comparison, multishell only acquire 2 or 3 b-values. Its ability to differentiate complex restricted diffusion is not as good as 23 b-value acquisition.

*There are limitations with the grid sampling scheme:*
- A bipolar-encoding pulse is needed to handle eddy current at the sequence level. 

FSL's *eddy* need enough redundancy at each shell to "interpolate" or correct DWI singals. The grid-258 turns out does not have this redundancy. Each of the acquired signals is much more unique and cannot be interpolated by the neighboring DWI signals. The eddy current distortion needs sequence-level correction.

- Methods using spherical harmonics cannot use grid scheme data.


## Steps to install the 12-min q-space scheme on Siemens scanners

The following steps will help set up the grid-258 sampling scheme on an MRI scanner. They were tested on Siemens Prisma scanners, and a similar protocol can be implemented in other manufacturers. If scanning time is an issue, consider 5-minute grid-101 ([b-table here](https://pitt-my.sharepoint.com/:t:/g/personal/yehfc_pitt_edu/EUFLViycNvFJjitO0pM2pg4BRHdXc9LSjICBtuAgiBk_4A?e=ztSaxy))

For a Siemens Prisma or Skyra scanner, a C2P agreement is needed (get it from Siemens representative) to install the CMRR multiband sequence:
http://www.cmrr.umn.edu/multiband/. Additional licenses include Siemens SMS EPI license (for MB imaging), Siemens DTI package license (for diffusion table), High-performance gradient (HCP) that is installed in Prisma (for high bandwidth readout).

Then setup the sequence using the exar file:

- [exar](/files/QSI258.exar1)
- [exar-journal](/files/QSI258.exar1-journal)
- [QSI_258dir.pdf](/files/QSI258.pdf)

Please use the "dMRI_dir258_1" sequence and add its opposite phase encoding b0 acquisition "dMRI_dir258_2" (take only a few seconds).

In the diffusion tab of the sequence, switch "MDDW" to "Free" mode and load the [grid-258 b-table](https://pitt-my.sharepoint.com/:t:/g/personal/yehfc_pitt_edu/ER8JurqNeGhAnn6k11tKAkEBZoGwPtuPCTnJK3ateCeAjg?e=yqUuIf).
The grid-258 text file should be placed under C:\MedCom\MriCustomer\seq\. You may need to rename the current DiffusionVectors.txt file to another name first and then copy the grid-258 table to DiffusionVectors.txt.
Then set b-value1=0 and b-value2=4000

For other scanners, please follow the following instruction.

## Steps to install the 12-min q-space scheme on Other scanners

Convert the [grid-258 b-table](https://pitt-my.sharepoint.com/:t:/g/personal/yehfc_pitt_edu/ER8JurqNeGhAnn6k11tKAkEBZoGwPtuPCTnJK3ateCeAjg?e=yqUuIf)
to its compatible format.

The following are acquisition parameters:

1. In-plane resolution: 2.0 mm, slice thickness: 2.0 mm (if your SNR is not good enough, increase them to 2.4 mm.)
2. Matrix size: 104x104
3. Slice number: 72 (can be reduced if ignoring the cerebellum), no gap
4. Multiband acceleration factor: 3 or 4
5. "Bipolar" diffusion scheme (for eliminating eddy current). Some may prefer "Monopolar" and correct Eddy current using FSL's eddy. This only works on shell acquisition and is not recommended for the grid scheme.
6. Minimum TE and TR
7. Pixel bandwidth: ~1700
8. Phase encoding direction: A to P
9. Make a copy of the sequence and invert its phase encoding direction (P to A). Only b0 is needed here for phase distortion correction.

## Quality Check for Preliminary Results

1. Make sure that the brain contour in the DWI with b=4000 is still visible. If not, consider lowering the b-value to 3000.
2. Create SRC files from the diffusion MRI data. Run DSI Studio and use [Diffusion MRI Analysis][Step T1a: Quality Control](/doc/gui_t1.html#step-t1a-quality-control-optional) to select a folder that contains the SRC file. It will compute "Neighboring DWI correlation". The one with a low correlation value may indicate a problem in data acquisition.

*Please feel free to send me your pilot grid258 data for a quality check. I will compare the results with the data I have to ensure that you have achieved the same quality.*

## What if I only have the default DTI protocol?

The good news is that you can use the scanner's built-in DTI protocol to acquire "multishell" and still enjoy the benefit of "beyond-DTI" methods such as GQI, QSDR, RDI...etc.

Here is a working parameter on a SIEMENS 3T Scanner:

1. acquire one 32-direction DTI at b=1500 and another 60-direction DTI at b=3000 (built-in ep2d_mddw protocol)
2. In-plane resolution: 2mm, slice thickness: 2mm (isotropic resolution is essential)
    If scanning time is an issue, use 2.5 mm isotropic.
3. Matrix size: 104x104
4. Slice number: 72 (can be reduced if ignoring the cerebellum), no gap
5. Minimum TE and TR, but the TE for the b=1500 DTI should be the same as the TE of the b=3000 DTI.
6. Make a copy of the sequence and invert its phase encoding direction (acquire AP and PA for phase distortion correction)
