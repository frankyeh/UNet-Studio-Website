DSI Studio has a high version turning rate, and occasionally the computation outcome may be different between versions. I would recommend  keepping a local copy of DSI Studio for each research project and update DSI Studio every time if a new project is initiated.

# Packages

[![Build Release](https://github.com/frankyeh/DSI-Studio/actions/workflows/build_release.yml/badge.svg)](https://github.com/frankyeh/DSI-Studio/actions/workflows/build_release.yml)<a href="https://github.com/frankyeh/DSI-Studio/commits/master"><img src="https://img.shields.io/github/last-commit/frankyeh/DSI-Studio"></a>

<a href="https://github.com/frankyeh/DSI-Studio/releases"><img src="https://img.shields.io/github/v/release/frankyeh/DSI-Studio"></a><a href="https://github.com/frankyeh/DSI-Studio/releases"><img src="https://img.shields.io/github/downloads/frankyeh/DSI-STUDIO/total?style=social"></a>

## DSI Studio

***Download and unzip to run the executive. No installation needed***

| OS      | File     | Note      |
|------|----------|-------|
|  Windows (7+)  |  [dsi_studio_win.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win.zip)<br />[dsi_studio_win.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win.zip) |  Unzip the file and click on the DSI Studio program to run it. If missing DLL files, install the package [here](https://aka.ms/vs/17/release/vc_redist.x64.exe). |
|  Mac (10.15+)      |  [dsi_studio_mac.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_macos-10.15.zip)<br />[dsi_studio_mac.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_macos-10.15.zip)  | You may need to [enable permission to run a 3-party app](http://mac-how-to.wonderhowto.com/how-to/open-third-party-apps-from-unidentified-developers-mac-os-x-0158095/). <br> If you have an old Mac that does not natively support 10.15, you may consider [manually upgrading to 10.15](http://dosdude1.com/catalina)  |
|  Ubuntu (16.04+)   |  [dsi_studio_ubuntu_1604.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_ubuntu_1604.zip)<br />[dsi_studio_ubuntu_1804.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_ubuntu_1804.zip)<br />[dsi_studio_ubuntu_2004.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_ubuntu_2004.zip) | |

*[previous versions](https://www.dropbox.com/sh/ectib64vhctkl8b/AADBRYp_aPLEuAOdNw393tO-a?dl=0)*



## DSI Studio with GPU support (Windows Version Only)

The FSL eddy correction and DSI Studio's atlas functions use GPU computation to achieve ~x5 to x10 accelerations.

***You may need to install [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_network)***

***If you are not sure which SM number to use, just download any of them to run. DSI Studio will check your graphic card and tell the correct one you should use.*** 

| File | NVidia Graphic Card|
|------|--------------------|
|  [dsi_studio_win_cuda_sm35.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm35.zip)<br />[dsi_studio_win_cuda_sm35.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm35.zip) | Tesla K40 |
|  [dsi_studio_win_cuda_sm37.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm37.zip)<br />[dsi_studio_win_cuda_sm37.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm37.zip) | Tesla K80 |
|  [dsi_studio_win_cuda_sm50.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm50.zip)<br />[dsi_studio_win_cuda_sm50.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm50.zip) | Tesla/Quadro M series |
|  [dsi_studio_win_cuda_sm52.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm52.zip)<br />[dsi_studio_win_cuda_sm52.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm52.zip) | Quadro M6000 , GeForce 900, GTX-970, GTX-980, GTX Titan X.  | 
|  [dsi_studio_win_cuda_sm53.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm53.zip)<br />[dsi_studio_win_cuda_sm53.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm53.zip) | Tegra (Jetson) TX1 / Tegra X1, Drive CX, Drive PX, Jetson Nano. |
|  [dsi_studio_win_cuda_sm60.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm60.zip)<br />[dsi_studio_win_cuda_sm60.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm60.zip) | Quadro GP100, Tesla P100, DGX-1 (Generic Pascal) |
|  [dsi_studio_win_cuda_sm61.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm61.zip)<br />[dsi_studio_win_cuda_sm61.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm61.zip) | GTX 1080, GTX 1070, GTX 1060, GTX 1050, GTX 1030 (GP108) <br> GT 1010 (GP108) Titan Xp, Tesla P40, Tesla P4, Discrete GPU on the NVIDIA Drive PX2 |
|  [dsi_studio_win_cuda_sm62.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm62.zip)<br />[dsi_studio_win_cuda_sm62.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm62.zip) | Integrated GPU on the NVIDIA Drive PX2, Tegra (Jetson) TX2 | 
|  [dsi_studio_win_cuda_sm70.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm70.zip)<br />[dsi_studio_win_cuda_sm70.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm70.zip) | DGX-1 with Volta, Tesla V100, GTX 1180 (GV104), Titan V, Quadro GV100 |
|  [dsi_studio_win_cuda_sm72.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm72.zip)<br />[dsi_studio_win_cuda_sm72.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm72.zip) | Jetson AGX Xavier, Drive AGX Pegasus, Xavier NX |
|  [dsi_studio_win_cuda_sm75.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm75.zip)<br />[dsi_studio_win_cuda_sm75.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm75.zip) | GTX/RTX Turing – GTX 1660 Ti, RTX 2060, RTX 2070, RTX 2080, Titan RTX, <br> Quadro RTX 4000, Quadro RTX 5000, Quadro RTX 6000, Quadro RTX 8000, Quadro T1000/T2000, Tesla T4 |
|  [dsi_studio_win_cuda_sm80.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm80.zip)<br />[dsi_studio_win_cuda_sm80.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm80.zip) | NVIDIA A100 (GA100), NVIDIA DGX-A100 |
|  [dsi_studio_win_cuda_sm86.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm86.zip)<br />[dsi_studio_win_cuda_sm86.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win_cuda_sm86.zip) | Tesla GA10x cards, RTX Ampere – RTX 3080, GA102 – RTX 3090,<br> RTX A2000, A3000, A4000, A5000, A6000, NVIDIA A40,<br> GA106 – RTX 3060, GA104 – RTX 3070, GA107 – RTX 3050, <br> Quadro A10, Quadro A16, Quadro A40, A2 Tensor Core GPU |

# Containers

<a href="https://hub.docker.com/repository/docker/dsistudio/dsistudio"><img src="https://img.shields.io/docker/cloud/build/dsistudio/dsistudio"></a>

**Docker**

```
docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD:/data dsistudio/dsistudio:latest
```

**Singularity**
     
```
$ singularity pull docker://dsistudio/dsistudio:latest     # This creates a singularity container *.sif file from the latest release of DSI Studio. Make sure you keep a copy of .sif file for your results
$ singularity exec -B /var,/run -B /home/server/folder dsistudio_latest.sif dsi_studio  # Some cluster does not allow users to access host drive, and you may need to mount folder into singularity container
$ singularity exec dsistudio_latest.sif dsi_studio   #  This invoke the graphic interface of DSI Studio 
$ singularity exec dsistudio_latest.sif dsi_studio --action=rec --source=my.src.gz # call DSI Studio command line interface in the singularity container  
```

# License

DSI Studio is free for research purposes (including research conducted within business entities). 

Unless required by applicable law or agreed to in writing, DSI Studio program and source code are distributed under [Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). Including any part of DSI Studio in a commercial product would require both copyright and patent licensing.

# Hardware recommendation:

To achieve the best performance, I would recommend a computer with a multi-core CPU (e.g. http://store.hp.com/us/en/mdp/business-solutions/z840-workstation). Minimum memory of 16GB is needed. To handle a large number of tracks or image volumes, DSI Studio will need 32GB of memory or more. 

