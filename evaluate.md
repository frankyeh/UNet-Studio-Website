Segment Brain Images using Built-in Models
------------------------------------------

![Examples of segmented brain images](https://chat.openai.com/images/examples2.png)

This documentation describes the steps to segment brain images using the built-in models in the program. Follow the instructions below to segment your animal data.

### Step 1: Specify Input

![Select NIFTI files of the animal data](https://user-images.githubusercontent.com/275569/234067989-b087a252-8197-4756-95b4-5d363becf043.png)

Select the NIFTI files (.nii, .nii.gz) of the animal data as the input for the program. Make sure the images are axial images of the brain, as shown in the example images below for rhesus and rodent brains.

![Example axial images for rhesus and rodent brains](https://github.com/frankyeh/UNet-Studio-Website/blob/main/images/t2_default_template.png)

Ensure that the orientation is correct, or the segmentation may fail.

### Step 2: Configure Network

![Select a built-in model or load a model file](https://user-images.githubusercontent.com/275569/234068134-0c5adfa7-6766-4bdf-bef8-032471e410f3.png)

Choose a built-in model from the droplist or load a model file using the folder button. The built-in models are stored as .net.gz files in the *network* folder of the program.

### Step 3: Evaluate

![Choose pre and post processing options](https://user-images.githubusercontent.com/275569/234068755-d976e1bd-4e20-410a-8854-c365b9b33e13.png)

After configuring the network, specify the pre-processing and post-processing options:

-   Pre Processing: The input image will be regridded or padded using different strategies. Choose "match voxel size" to regrid the image volume so that it matches the training data, "match image size" to scale the image so that the image width/height/depth will be similar to that of the training data, or "original size" to use the original size of the image.

-   Post Processing: The output image can be a "3d label", which uses softmax to get voxel-based labels from the output, "4d prob maps", which outputs a 4D probabilistic volume, or "direct output", which is the direct output from the model.

-   Prob Threshold: The threshold used in thresholding the probability when creating the 3D labels.

-   Device: Specify whether CPU or GPU is used.

### Step 4: Output

Click on the disk button to save the output.

You may check out the results for each input data 

If you experience errors or issues, please feel free to upload data using the private upload link on the website. We will modify the software to fix the problems.
