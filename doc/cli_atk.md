# [Step B4] Automatic Fiber Tracking

> use --action=`atk` to initiate automatic fiber tracking

## Examples

*Run fiber tracking on all fib.gz files to map the left and arcuate fasciculus
```
dsi_studio --action=atk --source=*.fib.gz --track_id=Arcuate
```

*Run fiber tracking on all fib.gz files and output tracts to the template space
```
dsi_studio --action=atk --source=*.fib.gz --export_template_trk=1
```


## Core Functions

| Parameters            | Default | Description                                                                 |
|:-----------------|:--------|:------------------------------------------------------------------------------|
| source |  | specify the src.gz or fib.gz file for automatic bundle tracking.  |
| track_id | `Fasciculus,Cingulum,Aslant,Corticos,Thalamic_R,Reticular,Optic,Fornix,Corpus` | specify the id number or the name of the bundle. The id can be found in /atlas/ICBM152/HCP1065.tt.gz.txt . <p> This text file is included in DSI Studio package (For Mac, right-click on dsi_studio_64.app to find content). You can specify partial name of the bundle: <p>           example:<p>   for tracking left and right arcuate fasciculus, assign --track_id=0,1  or --track_id=arcuate    (DSI Studio will find bundles with names containing 'arcuate', case insensitive) <p>           example:<p>   for tracking left and right arcuate and cingulum, assign --track_id=0,1,2,3 or --track_id=arcuate,cingulum|

## Optional
  
| Parameters            | Default | Description                                                                 |
|:-----------------|:--------|:------------------------------------------------------------------------------|
| length_ratio | `1.25` | the diffusion sampling length ratio for GQI reconstruction. This is only used if the source file is an SRC file. |
| tolerance | `16,18,20` | the tolerance for the bundle recognition. The unit is in mm. Multiple values can be assigned using comma separator. A larger value may include larger track variation but also subject to more false results. |
| track_voxel_ratio | `2` | the track-voxel ratio for the total number of streamline count. A larger value gives better mapping with the expense of computation time. For small bundles (e.g. right arcuate), a larger value may cause a large computation burden. |
| tip | `16` | iterations of topology-informed pruning. A higher value will apply more pruning that removes noisy tracks |
| export_stat | `1` | Specify whether to output track statistics. |
| export_trk | `1` | Specify whether to output tractography file. |
| export_template_trk | `0` | Specify whether to output tractography in the template space. |
| overwrite | `0` | Specify whether to overwrite existing files. |
| default_mask | `0` | Specify whether default mask is used. |
| thread_count | hardware max | Specify number of CPU cores used in computation |
