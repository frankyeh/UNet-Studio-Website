## Current Trend in Diffusion MRI Acquisitions

There is still no consensus on the "optimal" b-table setting to acquire diffusion MRI for "beyond-DTI" analysis.
10 years ago, the mainstream beyond-DTI acquisition was "high angular resolution diffusion imaging" (HARDI),
which acquires hundreds of sampling at one b-value (typically 3000 or more), but then HARDI was gradually replaced by multishell acquisition, which acquired diffusion MRI using at least two different b-values. This trend was motivated by studies confirming the benefit of combining data from multiple b-values.

Recently, the multishell acquisition has been used in the HCP protocol to get robust results, but the protocol has the following issues:

1. The 90 sampling directions at the low b-value shell are over-sampled because any of its DWI signals can be readily interpolated by other similar DWIs. In comparison, the high b-value samples do not have a lot of redundancy. An optimal setting should have similar redundancy for each shell, and this means high b-value shells should have more sampling directions.
2. In addition to the efficiency problem, the sampling density is largely inhomogeneous within each shell. Some directions have a higher sampling density, whereas others have a lower. Consequently, the scheme has a lot of "rotation variation". This inhomogeneity may reduce reproducibility if the subject head is positioned at different angles.
3. The multi-shell acquires only 3 b-values, and it would be ideal to sample at more b-values to better differentiate restricted diffusion.

## My recommendation: 23 b-values with b-max=4,000 at 258 directions

My personal recommendation is a 12-minute "grid-258" sampling with a maximum b-value of 4000, which acquires, not just two or three b-values,
but 23 different b-values ranging from b=0 to b=4000 at a total of 258 directions.
The low b-value range has fewer sampling compared to HCP multi-shell,
making the entire acquisition much more efficient.
Moreover, the scheme reaches a higher b-value to 4,000 so that it captures restricted diffusion much better.
This scheme addresses the above-mentioned 3 issues in multi-shell acquisitions.

> **Using a multi-band sequence (e.g. CMRR) with an MB factor of 4, this 2-mm 258-direction dMRI acquisition can be done in 12 minutes.**  

*The grid sampling has several benefits:*
- It has uniformly distributed density in the diffusion encoding space (i.e. q-space). This avoids over-sampling at low b-values or under-sampling at high b-values. It does not have the sampling homogeneity problem in the shell acquisitions.
- It can be reconstructed by DTI, ball-and-sticks model, NODDI, GQI...etc.
- It captures a continuous range of diffusion patterns from non-restricted diffusion to restricted diffusion. For clinical studies, the grid scheme can capture all possible diffusion changes due to edematous tissue or cell infiltration. in comparison, multi-shell only acquires 2 or 3 b-values and may miss diffusion patterns that are only sensitive to values in between.

*There are limitations with the grid sampling scheme:*
- It's Eddy current artifact cannot be corrected using FSL eddy, and the bipolar pulse is needed to handle eddy current at the sequence level
- Methods using spherical harmonics cannot use grid schemes because there is no shell structure for estimating spherical harmonics.
- Another b0 with an opposite phase encoding direction will also be acquired to correct for the phase distortion artifact.

The following steps will help you set up the grid-258 sampling scheme on your MRI scanner. The following steps are verified on Siemens Prisma scanners, and a similar protocol can be implemented in other manufacturers. If scanning is an issue, you may also consider grid-101 ([b-table here](https://pitt-my.sharepoint.com/:t:/g/personal/yehfc_pitt_edu/EUFLViycNvFJjitO0pM2pg4BRHdXc9LSjICBtuAgiBk_4A?e=ztSaxy))


## Steps to install the 12-min q-space scheme on Siemens scanners

The following are strategies I used to optimize the DWI protocol

- Reduce scanning time using multiband (MD=3 or 4)
- shorten TE by partial Fourier PE
- shorten TE by high readout bandwidth (trade-off with SNR)
- Phase distortion correction by acquiring full-forward PE and one b0 at backward PE

If you are using a Siemens Prisma or Skyra scanner, you will need a C2P agreement (get it from your Siemens representative) to install the CMRR multi-band sequence:
http://www.cmrr.umn.edu/multiband/. You may also need a Siemens SMS EPI license (for MB imaging), Siemens DTI package license (for diffusion table), High-performance gradient (HCP) that is installed in Prisma (for high bandwidth readout).

Then setup the sequence using the exar file:

- [exar](/dsi-studio-document/files/QSI258.exar1)
- [exar-journal](/dsi-studio-document/files/QSI258.exar1-journal)
- [QSI_258dir.pdf](/dsi-studio-document/files/QSI258.pdf)

Please use the "dMRI_dir258_1" sequence and add its opposite phase encoding b0 acquisition "dMRI_dir258_2" (take only few seconds).

In the diffusion tab of the sequence, switch "MDDW" to "Free" mode and load the [grid-258 b-table](https://pitt-my.sharepoint.com/:t:/g/personal/yehfc_pitt_edu/ER8JurqNeGhAnn6k11tKAkEBZoGwPtuPCTnJK3ateCeAjg?e=yqUuIf).
The grid-258 text file should be placed under C:\MedCom\MriCustomer\seq\. You may need to rename the current DiffusionVectors.txt file to another name first and then copy the grid-258 table to DiffusionVectors.txt.
Then set b-value1=0 and b-value2=4000

> I would recommend NOT to use Siemens' SMS-DWI for DSI-258 because my collaborator has reported serious peripheral nerve stimulation.
> If this has been improved, please email me and I will revise this recommendation.

If you are using other scanners, please follow the following instruction.

## Steps to install the 12-min q-space scheme on Other scanners

If you are using other Scanners, you may need to convert the [grid-258 b-table](https://pitt-my.sharepoint.com/:t:/g/personal/yehfc_pitt_edu/ER8JurqNeGhAnn6k11tKAkEBZoGwPtuPCTnJK3ateCeAjg?e=yqUuIf)
to its compatible format.

The following are acquisition parameters:

1. In-plane resolution: 2.0 mm, slice thickness: 2.0 mm (if your SNR is not good enough, increase them to 2.4 mm.)
2. Matrix size: 104x104
3. Slice number: 72 (can be reduced if ignoring the cerebellum), no gap
4. Multi-band acceleration factor: 3 or 4
5. "Bipolar" diffusion scheme (for eliminating eddy current). Some may prefer "Monopolar" and correct Eddy current using FSL's eddy. This only works on shell acquisition, and I do not recommend this approach for the grid scheme.
6. Minimum TE and TR
7. Pixel bandwidth: ~1700
8. Phase encoding direction: A to P
9. Make a copy of the sequence, invert its phase encoding direction (P to A). Only b0 is needed here for phase distortion correction.

## Quality Check for Preliminary Results

1. Make sure that you can still see the brain contour in the DWI with b=4000. If not, consider lowering the b-value to 3000.
2. Create SRC files from the diffusion MRI data. Run DSI Studio and use [Diffusion MRI Analysis][Step T1a: Quality Control](/doc/gui_t1.html#step-t1a-quality-control-optional) to select a folder that contains the SRC file. It will compute "Neighboring DWI correlation". The one with a low correlation value may indicate a problem in data acquisition.

*Please feel free to send me your grid258 data for a quality check. I will compare the results with the data I have to make sure that you have achieved the same quality.*

## What if I only have the default DTI protocol?

The good news is that you can use the scanner's built-in DTI protocol to acquire "multishell" and still enjoy the benefit of "beyond-DTI" methods such as GQI, QSDR, RDI...etc.

Here's a working parameter on a SIEMENS 3T Scanner:

1. acquire one 32-direction DTI at b=1500 and another 60-direction DTI at b=3000 (built-in ep2d_mddw protocol)
2. In-plane resolution: 2mm, slice thickness: 2mm (isotropic resolution is important)
    If scanning time is an issue, use 2.5 mm isotropic.
3. Matrix size: 104x104
4. Slice number: 72 (can be reduced if ignoring the cerebellum), no gap
5. Minimum TE and TR, but the TE for the b=1500 DTI should be the same as the TE of the b=3000 DTI.
6. Make a copy of the sequence and invert its phase encoding direction (acquire AP and PA for phase distortion correction)
