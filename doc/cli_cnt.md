# Connectometry analysis

> use --action=`cnt` to initiate [Step C3 Connectometry]


## Examples

*Use a multiple regression model with three variables (0:SEX, 1:BMI, 2:AGE) to study how BMI (the second variable) affects the brain connection in the CMU 60 connectometry database.*

```
dsi_studio --action=cnt --source=CMU60.db.fib.gz --demo=CMU60.txt --variable_list=0,1,2 --voi=1 --roi=FreeSurferDKT:left_precentral --output=CMU60
```

*Use ROI and ROA to limit connectometry analysis on subjects with demographics of scanner=1 and group not equal to 3

```
dsi_studio --action=cnt --source=study.db.fib.gz --demo=demo.csv --roi=ROI.nii.gz --roa=ROA.nii.gz --select="scanner=1,group/3" --variable_list=2,4,5 --voi=5
```

*Windows batch for testing each of the variable from 5 to 37, with variable 2 and 3 included as covariates

```
for /l %%G in (5,1,37) do (
dsi_studio --action=cnt --source=connectometry.sdf.db.fib.gz --demo=PANSS.csv --variable_list=2,3,%%G --voi=%%G > log%%G.txt
)
```


## Core Functions

| Parameters   | Description                                                                 |
|:-------------|:------------------------------------------------------------------------------|
| source |  specify the db.fib.gz file  |
| demo |  assign the path to the demographic CSV or Text file. |
| variable_list | assign the study variables to be included in the regression model. use comma to include multiple variables. <br> For example, use --variable_list=0,1,2 to include the first, second, and third variable.|
| voi | specify variable of interest (used only in multiple regression). <br> --foi=0 will analyze the "first" variable listed in the demographic file, <br> --foi=1 will analyze the second one. To test the longitudinal change, specify --foi=longitudinal |

## Parameters 

| Parameters | Default  | Description                                                                 |
|:-----------|:------|:------------------------------------------------------------------------------|
|t_threshold | `2.5`   | assign the t threshold for correlational tracking.  |
|length_threshold | `20` voxel distance | assign the length threshold for correlational tracking. |
|fdr_threshold | `0`  | assign a nonzero FDR threshold (e.g. 0.05) to enable FDR control. |
|permutation | `2000`   | assign the number of permutation used in the connectometry analysis. |
|thread_count | hardware max  | assign the number of threads used in the computation. |
|tip_iteration | `16`   | assign the number of pruning applied to remove noisy results. |
|exclude_cb | `1`  | assign --exclude_cb=1 to exclude cerebellum. |
|no_tractogram |  `1`  | specify 1 to signal DSI Studio NOT to output 3D tractogram pictures. The analysis will still output tractography files, which can be used later to generate tractogram separately. |
| output | path to the demographics file name | the file prefix for output all analysis results. The default will be the path to demographics file adding the name of the studying variable. | 

## Optional Functions

| Parameters | Description                                                                 |
|:-----------|:------------------------------------------------------------------------------|
| select |  select subjects for analysis. <br> For example, --selection=Gender=1,Age>20 select subjects with Gender field equal to 1 and Age older than 20 in the demographics.|
| seed, roi, roi2, roa... | assign regions to limit the tracking region. (see --action=trk for details) |


