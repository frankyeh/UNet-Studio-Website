# Automatic Fiber Tracking (AutoTrack)

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hzeb_q6ux-Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Automatic fiber tracking aims to map a target pathway (e.g. optic radiation, arcuate fasciculus) and is most suitable for pre-surgical planning or tract-of-interest analysis. The function uses a pathway recognition based on the a tractography atlas (Yeh et al. 2018) to filter out false tracks and unrelated tracks. The detail of how it works is the following:

1. non-linear registration of subject data to MNI space
2. seeds placed within the atlas tract volume (i.e. in any voxel corresponding to any tract
3. each of the generated streamlines is compared to the streamlines associated with each fiber tract from the HCP tractography atlas (Yeh 2018) using Hausdorff distances
4. determine which of the generated streamlines are the best match to the streamlines from the target structures in the HCP tractography atlas
5. streamlines matching to the target track in the HCP tractography atlas are retained and all other streamlines are discarded.

To use this function, click on [**Step T3: Fiber Tracking**] to select a FIB file generated from Step T1-T2, and DSI Studio will bring up the tracking window.

Follows the steps below to run automatic fiber tracking.

***Before using auto track, make sure you [run a whole-brain tracking](/doc/t3_whole_brain.html) as a visual quality check.***

## 1. Click on the [Step T3d:Tracts][Enable auto track...]

DSI Studio will normalize the subject's QA/ISO map to the template QA/ISO map and allow track recognition based on the bring tractography atlas.

## 2. Select Tract of Interest and Run [Fiber Tracking]

After normalization, select the target tracks and click fiber tracking to get the results.

You may change parameters at [Step T3c: Options] such as setting [Terminate if] = 10,000 [Tracts] or 1,000,000 [Seeds] to get satisfactory results.

[Min Length] helps remove fragments.

[Topology-Informed Pruning] will help remove singular fiber.

[Autotrack Tolerance (mm)] controls the tolerance to spurious fibers.

For detailed about tracking parameters, please refer to [whole brain tracking](/doc/t3_whole_brain.html)

## Troubleshooting AutoTrack

Automatic fiber tracking may fail to generate tracks if the data are not optimally reconstructed, or if the data has a quality problem. If "no result" happens very often (e.g. > 50%), then likely there is a post-processing problems.

Here is the checking list:

1. run [quality control for SRC files](/doc/gui_t1.html#batch-quality-control) and remove problematic dataset.

2. Check if the b-table is flipped, or if the image volume is flipped:


<iframe width="560" height="315" src="https://www.youtube.com/embed/stL4GMeTC1I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



   For b-table problems, uncheck the "check b-table" function at [Step T2b(2)], and manually flip the b-table in y-direction if you use bval and bvec from FSL.


The above issues will affect all pathways. If "no result" happens more often in small pathways (e.g. right AF, SLF I, corticopontine tract...etc) or in only some subjects (see examples reported in [1](https://groups.google.com/g/dsi-studio/c/wfXcuxk1I3g),[2](https://groups.google.com/g/dsi-studio/c/oOVyL9MN7PQ)), then likely your data acquisition is not perfect enough to map all small tracts in all individuals. 

The following is a list of common acquisition issues that may lead to poor results, and unfortunately, **there is not much you can do**.

1. nonisotropic spatial resolution (e.g., slice thickness much larger than in-plane resolution)
2. b-value not enough (e.g., b-value less than 1,500)
3. insufficient diffusion sampling directions (e.g., less than 100 directions)

If you still have concerns or unexpected issues, please upload the problematic SRC file(s) using the upload link provided on the left navigation bar and notify me at the Discussion forum.


# Manual Track Editing

<iframe width="560" height="315" src="https://www.youtube.com/embed/1xfhaFQhCtY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

DSI Studio provides "Select", "Delete", and "Cut" functions to refine the fiber tracking result.

- ***Tract Selection***

    ![image](https://user-images.githubusercontent.com/275569/147838366-a6adb599-2b04-4a17-9914-214c4af2fa9f.png)

    The steps are as follows:

    1. [Edit][Select] or press Ctrl + S

    2. Move the cursor to the starting point of the selection plane on the screen.

    3. Press the left button of the mouse and move the cursor to the ending point of the selection plane.

        **Use the right button to further select tracts perpendicular to the selection plane within an incoming angle (about 60degress).**

    4. Release the button and the selection will be performed immediately.


    The select function selects the tracks that pass through the *selection plane* determined by the location of the mouse click position on the screen. 
   

- ***Track Deletion***

    Tract deletion is carried out in the same manner except that the selected tracks will be deleted. The deletion can be undone by Ctrl+Z.

- ***Track Cutting***

    Tract cutting is to cut the selected tracts into two parts. This function is useful in a condition like the users want to analyze only the right corpus callosum. The corpus callosum can be cut into two parts by a sagittally placed selection plane.  The right corpus callosum is then selected to perform further analysis.

    Another condition to apply tract cutting is that only a section of the fiber bundle is to be analyzed, or the users want to align the fiber bundle. In such a case, an interested portion of the fiber bundle can be extracted by track cutting.

- ***Track Painting***

    Track painting offers a way to paint tracks by assigned color. To perform this task, press Ctrl+P. Assign the painting color and select the tracks.

- ***Cut by Slices***

    Cut tracts based on slice position. The function is at [Edit][Cut by slices]


***Shortcuts***

  - Ctrl+S: select tracts in the 3D window 

  - Ctrl+D: delete tracts in the 3D window

  - Ctrl+P: delete tracts in the 3D window

  - Ctrl+X: cut tracts in the 3D window (click-drag-release)(cannot undo)

  - Ctrl+T: trim tracts  (a.k.a. topology-informed pruning)

  - Ctrl+Z: undo select and delete

  - Ctrl+Y: redo select and delete


## 3. Save Tractography

The fiber trajectories can be saved using [Tracts][Save Tracts As]. One should note that [Tracts][Save Tracts As] saves only the current selected fiber bundles. To save tracts of different clusters at one, use [Tracts][Save All Tracts As...].


DSI Studio saves tracks in the native diffusion voxel space rotated to "LPS". The coordinates are voxel coordinates started from (0,0,0) at the most left/anterior/bottom point of the image volume. The orientation is (+right,+posterior, +top). For example, (1,2,3) = [the left most 1st voxel, the most anterior second voxel, the bottom 3rd voxel].


# Tractometry

[Tracts][Statistics] provides values extracted from shape analysis and diffusion metrics.

[Shape analysis](https://www.sciencedirect.com/science/article/pii/S1053811920308156) uses the topology information from tractography streamlines to derive length, area, volume, and shape descriptors. The analysis quantifies macroscopic structural features of fiber pathways.

The details of the diffusion metrics are documented at [Diffusion MRI Metrics](https://sites.google.com/a/labsolver.org/dsi-studio/Manual/diffusion-mri-indices)

***Shape Metrics***

| Metrics | Description |
|:--------|:------------|
| mean length  | multiplying number of coordinates in the streamlines with the distance between the coordinates |
| span(mm) | distance between two end regions |
| curl | length divided by span |
| elongation |    |
| diameter(mm) |  |
| volume (mm^3) | multiplying number of voxels passed by all streamlines with the voxel size (in mm cubic) |
| trunk volume(mm^3) |  |
| branch volume(mm^3) |  |
| total surface area(mm^2) |  |
| total radius of end regions(mm) | |
| total area of end regions(mm^2) |  |
| irregularity 12.0779  | |
| area of end region 1(mm^2) |  |
| radius of end region 1(mm) |  |
| irregularity of end region 1 |  |
| area of end region 2(mm^2) |  |
| radius of end region 2(mm) |  |
| irregularity of end region 2 |  |

***Diffusion Metrics***

| Metrics | Description |
|:--------|:------------|
| qa | quantitative anisotropy |
| nqa  | normalized QA (maximum QA of a scan=1) |
| dti_fa | fractional anisotropy|
| md | mean diffusivity |
| ad | axial diffusivity |
| rd | radial diffusivity |
| iso | isotropic diffusion |
| rdi | restricted diffusion |
| nrdi02L | non-restricted diffusion at 0.2 diffusion sampling length ratio |
| nrdi04L | non-restricted diffusion at 0.4 diffusion sampling length ratio |

You can insert an external volume (e.g., T1W, T2W, PET...etc.) using [Slices][Insert T1W/T2W...] and use track statistics to sample them along the fiber pathways.

## Tractography file formats

The supported tractography format in DSI Studio include the TT format (DSI Studio default), Text format, TRK format (TracVis), TCK format (Mrtrix), and MAT format (MATLAB):

***TT format***

The Tiny-Tract (TT) format stores tractography with a resolution limit of 1/32 voxel spacing. It is a gz compressed mat file. To load it in MATLAB, ungzip it and rename it as .mat. There will be matrices including dimension, parameter_id, report, track, voxel_size.

The tract matrix can be parsed using the following code:

```mat
function track = parse_tt(track)
buf1 = uint8(track);
buf2 = int8(track);
pos = [];
i = 1;
while(i <= length(track))
    pos = [pos i];
    i = i + typecast(buf1(i:i+3),'uint32')+13;
end

track = cell(1,length(pos));
parfor i = 1:length(pos)
    p = pos(i);
    size = typecast(buf1(p:p+3),'uint32')/3;
    x = typecast(buf1(p+4:p+7),'int32');
    y = typecast(buf1(p+8:p+11),'int32');
    z = typecast(buf1(p+12:p+15),'int32');
    tt = zeros(size,3);
    tt(1,:) = [x y z];
    p = p+16;
    for j = 2:size
        x = x+int32(buf2(p));
        y = y+int32(buf2(p+1));
        z = z+int32(buf2(p+2));
        p = p+3;
        tt(j,:) = [x y z];
    end
    track{i} = single(tt)/32;
end
end
```


***Text format***

The output format can be a text file that stores the coordinates of each fiber track. The coordinates of each fiber trajectory are stored in one line. The x y z coordinates are listed sequentially:

```
x1 y1 z1 x2 y2 z2 ... xn yn zn               <---first tract
x1 y1 z1 x2 y2 z2 ... xn yn zn               <---second tract
```

***Along-tract metrics format***

The fiber trajectories are sequences of 3D coordinates. DSI Studio uses these coordinates to sample the index like FA and ADC. The along-track sampling samples one value for each coordinate in a trajectory. The data arrangement is similar to that of the tract coordinate TXT file.
   
For each coordinate on a trajectory, DSI Studio calculates the index using trilinear interpolation. The calculated values of a trajectory are exported as a sequence of numbers in a line. The values are separated by space. The first value is the first coordinate of the first trajectory, as shown in the following.
     

```
v11 v12 v13 v14...
v21 v22 v23 v24...
```

Here v11 is the value corresponding to the coordinate (x1,y1,z1) of the first trajectory line (show above). v12 corresponds to (x2,y2,z2)...etc.

***MAT Format***

The trajectories can be saved in a Matlab MAT version 4 format. The coordinates of all tracts are stored in a matrix named "tracts". The numbers of coordinates for each fiber are stored in a matrix named "length". The coordinates of the first trajectory are stored in tracts(:,1:length(1)), and the second in tracts(:,length(1)+1,length(1)+length(2)).

To save the tracts data in MAT version 4 format. Use the command save tract.mat -v4


# Tract Profile

![image](https://user-images.githubusercontent.com/275569/147835769-2d0eb159-2c26-4820-8037-410e95226eac.png)

The tract profile is similar to [Automated Fiber Quantification (AFQ)](https://github.com/yeatmanlab/AFQ). The function is located at [Tracts][Tract Profile]. DSI Studio provides a reporting interface that visualizes the quantitative index of a generated tractography. The generated plot and data can be exported as image or text value data.

## X direction, Y direction, and Z direction

![image](https://user-images.githubusercontent.com/275569/147835776-b20e26dd-ab69-4e23-829e-41df14133c22.png)

**An example of corticospinal tract viewed from the anterior**

![image](https://user-images.githubusercontent.com/275569/147835782-ba03fd19-b335-405d-9ccf-58f644471cb9.png)

**Result obtained from X-direction sampling**

For X-direction, the coordinates of all tracks are projected to x-axis simultaneously, and the averaged values along the x-direction are estimated using kernel density estimator with the bandwidth specified in the interface. The unit of the bandwidth is at the scale of voxel size. The sampling strategies for y-direction and z-direction are conducted similarly.

## Fiber orientation

All fiber tracts are stretched to the same length, and the sampling starts from one end to another. The sampled values are regressed using a kernel density estimator with the bandwidth specified in the interface.

![image](https://user-images.githubusercontent.com/275569/147835790-a16c9d8a-0c91-4131-9b0d-8ca1954e6673.png)

**Illustration of the fiber stretch strategy for index sampling.**

## Mean of each fiber

the mean value of the index is calculated for each fiber tract first, and all the values are plotted.

# Tract Density Imaging

Track density imaging (TDI) was introduced by Calamante et al. [1]. TDI was shown to achieve higher resolution and facilitate the visualization of smaller structures. 

DSI Studio offers the function under [Tracts][Save Track Density] to export tract density imaging after tractography is generated. To generate TDI, smaller step size is required to produce a good result. The default setting of step size used in DSI Studio is half of the voxel size. This setting has to be changed to 1/8 voxel size in order to achieve a subvoxel resolution of 1/4 voxel size. A Larger amount of fiber tracts (e.g. 10,000 for human study) tends to generate better TDI. 

Another way to include more fiber is to generate multiple TDI and average them together. This may offer the same effect of generating a huge equivalent amount of fiber tracts. You may want to export TDI in MATLAB's mat format and use Matlab to perform the average.


Use [Tracts][Save Track Density] to save TDI. There are three options under this submenu

- **TDI in diffusion space**

The first option is exporting the TDI in the diffusion space, which does not use the subvoxel resolution.

- **TDI in subvoxel diffusion space**

The second one exports TDI in a 4-times higher spatial resolution than the current diffusion space.

- **TDI in current slice space**

You may load a T1w image in DSI Studio and export the TDI in the T1 space.

