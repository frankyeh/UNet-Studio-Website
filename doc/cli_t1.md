# Generating SRC files

> use --action=`src` to generate SRC file from NIFTI or DICOM files

## Examples

*Convert one 4d NIFTI file and generate an SRC file subject001.nii.gz.src.gz*

```
dsi_studio --action=src --source=c:\subject001.nii.gz
```

*Convert one 4d NIFTI file and specify the location of bval and bvec (only needed when DSI Studio cannot find them)*

```
dsi_studio --action=src --source=c:\subject001.nii.gz --bval=bval --bvec=bvec
```

*Combine two 4d NIFTI files and generate one SRC file*

```
dsi_studio --action=src --source=HCA9992517_V1_MR_dMRI_dir98_AP.nii.gz,HCA9992517_V1_MR_dMRI_dir99_AP.nii.gz
```

*Search all DICOM files under the assigned directory and output SRC file*

```
dsi_studio --action=src --source=C:\20081006_11_00814348_DWI_WIP_DSI_203 --output=c:\.src.gz
```

*Find all *98_AP.nii.gz file and combine its corresponding 99_AP.nii.gz file to generate one combined SRC file*

```bash
for sub in $(ls *98_AP.nii.gz)
do
    dsi_studio --action=rec --source=${sub},${sub:0:25}99_AP.nii.gz
done
```

*Parse all 4d NIFTI files in a folder (each of them has a bval and bvec file that shares a similar file name) and generate corresponding SRC files to a new folder*

```
dsi_studio --action=src --source=*.nii.gz --output=/src_folder
```

*Windows batch file for creating src files from HCP datasets*

```bat
path=C:\dsi_studio_64
cd F:\HCP\
dir ?????? /b > file_list.txt
for /f "delims=" %%x in (file_list.txt) do (
call dsi_studio.exe --action=src --source=F:\HCP\%%x\T1w\Diffusion\data.nii.gz --output=F:\%%x.src.gz > F:\%%x.txt
)
```

*Windows batch script for creating src from NIFTI data*

```bat
path=C:\dsi_studio_64
dir ????? /b > file_list.txt
for /f "delims=" %%x in (file_list.txt) do (
call dsi_studio.exe --action=src --source=%%x\%%x_dwi_QCed.nii --bval=%%x\%%x_QC.bval --bvec=%%x\%%x_QC.bvec --output=%%x.src.gz
)
```

## Core Functions

| Parameters            | Default | Description                                                                 |
|:-----------------|:--------|:------------------------------------------------------------------------------|
| source |  | specify a directory storing DICOM files or the file name for 4D nifti file. <br> specify one or more 4D NIFTI files separated by comma |


## Optional Functions

| Parameters            | Description                                                                 |
|:-----------------|:------------------------------------------------------------------------------|
| output | assign the output src file name (.src.gz) or the output folder |
| b_table | assign the text file to replace b-table |
| bval |specify the location of the FSL bval file<sup>a</sup> |
| bvec |specify the location of the FSL bvec file<sup>a</sup> |

<sup>a</sup>for most cases, DSI Studio can automatically associate bval and bvec with NIFTI automatically.

## Accessory Functions

| Parameters            | Default | Description                                                                 |
|:-----------------|:--------|:------------------------------------------------------------------------------|
| recursive | `0` | search all NIFTI or DICOM files under the directory specified in --source |
| up_sampling | `0` | upsampling the DWI, `0`:no resampling, `1`:upsample by2, `2`:downsample by2, `3`:upsample by 4, `4`:downsample by 4 |

    
