# Rename DICOM Files

> use --action=`ren` to initiate automatic fiber tracking

## Examples


*Rename DICOM files under the raw_data directory*
```
dsi_studio --action=ren --source=d:/draw_data
```

*Rename DICOM files under the dicom directory and create SRC and NIFTI files
```
dsi_studio --action=ren --source=d:/dicom --to_src_nii=1
```


*For each directory, rename DICOM*
```
for /f "delims=" %%x in ('dir * /b') do (
    call dsi_studio.exe --action=ren --source="D:\MRI\CA\%%x" > %%x.log.txt 
)
```

## Core Functions

| Parameters            | Default | Description                                                                 |
|:-----------------|:--------|:------------------------------------------------------------------------------|
| source |  | specify the path to the directory containing the DICOM files. The subdir will be searched. |
| output |  | specify the directory to output the renamed DICOM files |
| to_src_nii | `0` | specify whether to convert DICOMs to SRC and NIFTI files |



