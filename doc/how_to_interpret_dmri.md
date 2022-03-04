# Introduction

Diffusion MRI (dMRI) acquires **diffusion-sensitive** MRI data to reveal the microscopic change of biological tissues structure. The dMRI data are processed to provide diffusion metrics, such as diffusivities and anisotropy to summarize the diffusion pattern. Studies have shown that diffusion metrics could reveal neuronal change, cellularity, tissue edema.

The diffusion metrics can be categorized into model-based metrics and model-free metrics. The model-based metrics are calculated by fitting dMRI signals with a *model*, such as a tensor model, NODDI model, and the model's parameters will provide the metrics. The model-free metrics are directly calculated from the PDF of diffusion distribution (i.e., histogram of diffusion distribution) without assuming a model. 

There are pros and cons concerning each approach. Model-based metrics need fewer diffusion sampling, and the metrics are usually associated with physical or biological references. The downside is the violation of models, which is common in biological studies. Model-free metrics need more diffusion samplings, and the association between metrics and biological findings requires tissue validation. The advantage is that it does not have a model assumption.

The following is a summary of how to interpret results from diffusion metrics.

# Model-based metrics

The most commonly used model-based metrics are calculated from the diffusion tensor model:

- **FA**: fractional anisotropy
- **AD**: axial diffusivity
- **RD**: radial diffusivity (the average of two radial eigenvalues) `
- **MD**: mean diffusivity (the average of all eigen values). The diffusivity (either RD, MD, or AD) calculated in DSI Studio has a unit of 10^-3 mm^2/s.
- **txx, txy, txz, tyy, tyz, tzz**: the 6 entries of the tensor matrix.

A diffusion tensor can provide fractional anisotropy (FA), axial diffusivity (AD), radial diffusivity (RD), and mean diffusivity (MD).

**AD**, denoted by λ parallel, quantifies how fast water diffuses along the axonal fibers. It is estimated by λ1, the first eigenvalue of the tensor. RD, denoted by λ perpendicular, quantified how fast water diffuses across the axonal bundles. It is estimated by (λ2+λ3)/2, the average of the second and third eigenvalues of the tensor. MD is the diffusivity average from the three eigenvalues of the tensor. It is often regarded as an approximation of the overall diffusivities. FA is a non-unit fraction derived from the ratio between λ1, λ2, and λ3. It has a value ranging from 0 (isotropic) to 1(totally anisotropic). Myelinated fibers have high FA and low RD (Chang 2017).

Numerous studies have investigated the relation between diffusivity and pathological conditions:

- Axonal injury: AD ↓(Budde et al., 2007; Song et al., 2003)
- Demyelination: RD ↑ (Budde et al., 2007; Song et al., 2002; Song et al., 2005)
- Myelination: FA (Chang, 2017), RD (partly, Chang, 2017).
- Tumor: ADC↓(Gauvain et al., 2001; Kono et al., 2001; Sugahara et al., 1999)
- Immune cell infiltration: ADC↓
- Vasogenic edema: ADC↑
- Cytotoxic edema: ADC↓
- Hemorrhage: ADC↓

When there is demyelination, RD changes dramatically (Song, 2002). If there is axonal loss, the AD drops (Song 2003). Many studies have used RD specifically for myelination, citing the demyelination studies. However, the fact that demyelination has RD change does not mean that good myelination is also reflected by RD (Change 2017). The interpretation of RD requires additional caution.

## References
1. Budde MD, Xie M, Cross AH, Song SK. Axial diffusivity is the primary correlate of axonal injury in the experimental autoimmune encephalomyelitis spinal cord: a quantitative pixelwise analysis. J Neurosci. 2009;29(9):2805-13.
2. Budde MD, Kim JH, Liang HF, Schmidt RE, Russell JH, Cross AH, et al. Toward accurate diagnosis of white matter pathology using diffusion tensor imaging. Magn Reson Med. 2007;57(4):688-95.
3. Sun SW, Liang HF, Trinkaus K, Cross AH, Armstrong RC, Song SK. Noninvasive detection of cuprizone induced axonal damage and demyelination in the mouse corpus callosum. Magn Reson Med. 2006;55(2):302-8.
4. Song SK, Yoshino J, Le TQ, Lin SJ, Sun SW, Cross AH, et al. Demyelination increases radial diffusivity in corpus callosum of mouse brain. Neuroimage. 2005;26(1):132-40.
5. Song SK, Sun SW, Ju WK, Lin SJ, Cross AH, Neufeld AH. Diffusion tensor imaging detects and differentiates axon and myelin degeneration in mouse optic nerve after retinal ischemia. Neuroimage. 2003;20(3):1714-22.
6. Song SK, Sun SW, Ramsbottom MJ, Chang C, Russell J, Cross AH. Dysmyelination revealed through MRI as increased radial (but unchanged axial) diffusion of water. Neuroimage. 2002;17(3):1429-36.
7.  Kono K, Inoue Y, Nakayama K, Shakudo M, Morino M, Ohata K, et al. The role of diffusion-weighted imaging in patients with brain tumors. AJNR Am J Neuroradiol. 2001;22(6):1081-8.
8.  Gauvain KM, McKinstry RC, Mukherjee P, Perry A, Neil JJ, Kaufman BA, et al. Evaluating pediatric brain tumor cellularity with diffusion-tensor imaging. AJR Am J Roentgenol. 2001;177(2):449-54.
9. Sugahara T, Korogi Y, Kochi M, Ikushima I, Shigematu Y, Hirai T, et al. Usefulness of diffusion-weighted MRI with echo-planar technique in the evaluation of cellularity in gliomas. J Magn Reson Imaging. 1999;9(1):53-60.
10. Chang EH, Argyelan M, Aggarwal M, Chandon TS, Karlsgodt KH, Mori S, et al. The role of myelination in measures of white matter integrity: Combination of diffusion tensor imaging and two-photon microscopy of CLARITY intact brains. Neuroimage. 2017;147:253-61.



## Model-free metrics

The model-free metrics calculated in DSI Studio include the following:

- **QA**: quantitative anisotropy (QA) is calculated from generalized q-sampling imaging (GQI)(Yeh, 2010).
- **NQA**: normalized QA, scaled from QA so that the maximum nqa of a subject is one.
- **ISO**: isotropic diffusion component derives from GQI analysis
- **RDI, NRDI**: an index quantifying the density of restricted diffusion given a displacement distance (L). nRDI quantifies non-restricted diffusion. (Yeh, et al. Magnetic resonance in medicine 77.2 (2017): 603-612).

QA is the density of *anisotropic* diffusing water calculated from GQI (Yeh, 2010). Each voxel may have more than one principal diffusion directions (when two white matter tracts intersect), and each principal direction will have its QA value. It is noteworthy that there is only one FA for each voxel, regardless of the number of principal diffusion directions. 

QA scales with spin density and receiver gain, and it has an "arbitrary unit."  QA is often calibrated by scaling the largest isotropic component in the entire image volume to a unit (i.e., max(iso)=1). The normalized QA (NQA) further scales the largest QA in the scan to one. 

ISO is the density of *isotropic diffusing water calculated from GQI (Yeh, 2010). It represents background isotropic diffusion contributed from CSF or edema, including restricted and non-restricted isotropic diffusion. ISO will be affected by the diffusion MRI sampling schemes. Higher b-value "diffusion sensitization" will provide more sensitivity to restricted diffusion, whereas lower b-value will be more sensitive to free water diffusion. 

RDI and NRDI further separate restricted ISO and non-restricted ISO. The calculation needs multiple b-values, ideally the grid scheme that acquires 20+ b-values.

Numerous studies have investigated the relation between model-free metrics and pathological conditions:

- Demyelination, Neuronal injury or degeneration: QA↓ (Yeh 2019)(Shen 2015) ISO↑(Shen 2015)
- Axonal density↑: RDI↑ (Garic 2021)
- Cell infiltration: RDI↑(Yeh 2017)(Yeh 2021)
- Edema: NRDI↑(Yeh 2017) 

# References:
1. Yeh FC, Irimia A, Bastos DCA, Golby AJ. Tractography methods and findings in brain tumors and traumatic brain injury. Neuroimage. 2021;245:118651.
2. Yeh FC, Zaydan IM, Suski VR, Lacomis D, Richardson RM, Maroon JC, et al. Differential tractography as a track-based biomarker for neuronal injury. Neuroimage. 2019;202:116131.
3. Garic D, Yeh FC, Graziano P, Dick AS. In vivo restricted diffusion imaging (RDI) is sensitive to differences in axonal density in typical children and adults. Brain Struct Funct. 2021;226(8):2689-705.
4. Yeh FC, Liu L, Hitchens TK, Wu YL. Mapping immune cell infiltration using restricted diffusion MRI. Magn Reson Med. 2017;77(2):603-12.
5. Shen CY, Tyan YS, Kuo LW, Wu CW, Weng JC. Quantitative Evaluation of Rabbit Brain Injury after Cerebral Hemisphere Radiation Exposure Using Generalized q-Sampling Imaging. PLoS One. 2015;10(7):e0133001.


# Difference between model-based and model-free

Here we focus on the differences between DTI and GQI, although other model-based and model-free methods exist.

## Partial volume effect due to fiber and free water

![image](https://user-images.githubusercontent.com/275569/156826203-e8c4ece1-1b45-4193-8257-aa8e64dfe57c.png)


The DTI model does not specify restricted diffusion contributed by axonal myelination. The consequence is that FA, AD, MD will reflect a portfolio of biological changes including edema, inflammation, or just a superimposing crossing fiber (see  Yeh F-C et al. PLoS ONE 8(11): e80713.2013). Using DTI metrics will result in a considerable variation due to the complexity of the real-world biological changes, and often time a large sample size is needed to find statistical significance.

GQI separates isotropic diffusion and anisotropic diffusion, thus minimizing the partial volume of free water. The anisotropic diffusion is further quantified per each principal diffusion direction, thus minimizing the partial volume of crossing fibers. A neurosurgery study has shown that QA is robust against peritumoral edema and contributes to more reliable tractography (Zhang, et al. Neurosurgery, 73(6), 1044-1053. 2013). A phantom study has shown that QA is more robust to the free water effect and partial volume of crossing fibers. (Yeh, PloS one 8.11, 2013). 

## Biophysical meaning

![image](https://user-images.githubusercontent.com/275569/156826048-40933f38-339d-442e-ab5d-2fa5d4fbb999.png)

The metrics derived from DTI (e.g., FA, AD, RD, MD) cannot differentiate non-restricted and restricted diffusion. The diffusivity measures the overall "rate" of diffusion, and the metrics are an ensemble measure from both non-restricted (due to edema or free water) and restricted diffusion (myelination). The calculation also cannot address the condition of fibers. The biological association between DTI-based metrics is often affected by multiple counteracting factors, making the interpretation much more difficult.

In comparison, the anisotropy and isotropic measures from GQI measure the "density" of diffusing water, not the "rate" of diffusion. The measures could separate restricted diffusion from non-restricted diffusion. The anisotropy component considers the possibility of more than one principal diffusion direction (e.g., crossing fibers). The isotropic components further consider restricted and non-restricted diffusion.

