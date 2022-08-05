DSI Studio has a high version turning rate, and occasionally the computation outcome may be different between versions. I would recommend  keepping a local copy of DSI Studio for each research project and update DSI Studio every time if a new project is initiated.

# Packages

[![Build Release](https://github.com/frankyeh/DSI-Studio/actions/workflows/build_dsistudio.yml/badge.svg)](https://github.com/frankyeh/DSI-Studio/actions/workflows/build_release.yml)<a href="https://github.com/frankyeh/DSI-Studio/commits/master"><img src="https://img.shields.io/github/last-commit/frankyeh/DSI-Studio"></a>

<a href="https://github.com/frankyeh/DSI-Studio/releases"><img src="https://img.shields.io/github/v/release/frankyeh/DSI-Studio"></a><a href="https://github.com/frankyeh/DSI-Studio/releases"><img src="https://img.shields.io/github/downloads/frankyeh/DSI-STUDIO/total?style=social"></a>

## DSI Studio

***[NOTICE (2020/08/02): Major revision on QA after August 2nd, 2022](https://groups.google.com/g/dsi-studio/c/t-kSFxXrGFU)***

***Download and unzip to run the executive. No installation needed***

| OS      | File     | Note      |
|---------|----------|-----------|
|  Windows (7+)  |  [dsi_studio_win.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_win.zip)<br />[dsi_studio_win.zip(中國镜像)](https://hub.fastgit.xyz/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_win.zip) |  Unzip the file and click on the DSI Studio program to run it. If missing DLL files, install the package [here](https://aka.ms/vs/17/release/vc_redist.x64.exe).<br>Install [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_network) and update your Graphic driver to use GPU |
|  Mac (10.15+)      |  [dsi_studio_mac-10.15.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_macos-10.15.zip)<br />[dsi_studio_mac-10.15.zip(中國镜像)](https://hub.fastgit.xyz/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_macos-10.15.zip)<br/>[dsi_studio_mac-11.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_macos-11.zip)<br />[dsi_studio_mac-11.zip(中國镜像)](https://hub.fastgit.xyz/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_macos-11.zip)<br/>[dsi_studio_mac-12.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_macos-12.zip)<br />[dsi_studio_mac-12.zip(中國镜像)](https://hub.fastgit.xyz/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_macos-12.zip)  | You may need to [enable permission to run a 3-party app](http://mac-how-to.wonderhowto.com/how-to/open-third-party-apps-from-unidentified-developers-mac-os-x-0158095/). <br> For MacOS < 10.15, consider [manually upgrading to 10.15](http://dosdude1.com/catalina)  |
|  Ubuntu (16.04+)   |  [dsi_studio_ubuntu_1604.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_ubuntu_1604.zip)<br />[dsi_studio_ubuntu_1804.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_ubuntu_1804.zip)<br />[dsi_studio_ubuntu_2004.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_ubuntu_2004.zip)<br />[dsi_studio_ubuntu_2204.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2022.08.03/dsi_studio_ubuntu_2204.zip) | |

*[previous versions](https://www.dropbox.com/sh/ectib64vhctkl8b/AADBRYp_aPLEuAOdNw393tO-a?dl=0)*

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

