
# Packages

## UNet Studio Pre-release

U-Net Studio is a standard alone executive program written in C++. The only dependency is CUDA Toolkit and Libtorch DLLs. To use U-Net Studio, download the zip file from the link and uncompress it to any folder. There is a `install_win.bat` script to install CUDA Toolkit and Libtorch DLLs. After it finishes, just run the program.

| OS      | Install      |
|---------|-----------|
|  [Windows (7+)](https://github.com/frankyeh/UNet-Studio/releases/download/2023.04.17/unet_studio_win.zip) | (1) download the zip file and unzip it to a folder. <br> (2) run install_win.bat to install pytorch DLLs (~3GB) and CUDA toolkit (~2gb)|
|  [MacOS 13 (Intel)](https://github.com/frankyeh/UNet-Studio/releases/download/2023.04.17/unet_studio_macos-13.zip) <br> [MacOS 14 (AppleSilicon)](https://github.com/frankyeh/UNet-Studio/releases/download/2023.04.17/unet_studio_macos-14.zip) <br> [MacOS 15 (AppleSilicon)](https://github.com/frankyeh/UNet-Studio/releases/download/2023.04.17/unet_studio_macos-15.zip) | To run it, you need to [enable permission](http://mac-how-to.wonderhowto.com/how-to/open-third-party-apps-from-unidentified-developers-mac-os-x-0158095/). <br> On MacOS 15, the system may show the app is damaged because it is not notarized (requires $99 per year). To bypass Gatekeeper, run the line below in the terminal: <br>```xattr -rd com.apple.quarantine /path/to/dsi_studio.app.```|
|  [Ubuntu 22.04 cuda](https://github.com/frankyeh/UNet-Studio/releases/download/2023.04.17/unet_studio_ubuntu2204.zip) | Need CUDA 11.8 and Pytorch installed  |

To update U-Net Studio, just replace the .exe file and the models stored under the network folder.

# Citation

`FC Yeh, "Brain MRI Segmentation using Template-Based Training and Visual Perception Augmentation", arXiv:2308.02363, 2023.`

# License

U-Net Studio is free for academic or research purposes under the [Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). 

