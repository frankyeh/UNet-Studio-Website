# Packages

[![Build Release](https://github.com/frankyeh/DSI-Studio/actions/workflows/build_release.yml/badge.svg)](https://github.com/frankyeh/DSI-Studio/actions/workflows/build_release.yml)<a href="https://github.com/frankyeh/DSI-Studio/commits/master"><img src="https://img.shields.io/github/last-commit/frankyeh/DSI-Studio"></a>

<a href="https://github.com/frankyeh/DSI-Studio/releases"><img src="https://img.shields.io/github/v/release/frankyeh/DSI-Studio"></a><a href="https://github.com/frankyeh/DSI-Studio/releases"><img src="https://img.shields.io/github/downloads/frankyeh/DSI-STUDIO/total?style=social"></a>


Download and unzip to run the executive. No installation needed

| OS      | File     | Note      |
|------|----------|-------|
|  Windows   |  [dsi_studio_win.zip(github)](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win.zip)<br />[dsi_studio_win.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_win.zip) |  Unzip the file and click on the DSI Studio program to run it. If missing DLL files, install the package [here](https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package). |
|  Mac       |  [dsi_studio_mac.zip(github)](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_macos-10.15.zip)<br />[dsi_studio_mac.zip(中國镜像)](https://github.com.cnpmjs.org/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_macos-10.15.zip)  | You may need to [enable permission to run a 3-party app](http://mac-how-to.wonderhowto.com/how-to/open-third-party-apps-from-unidentified-developers-mac-os-x-0158095/).   |
|  Ubuntu    |  [dsi_studio_ubuntu_1604.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_ubuntu_1604.zip)<br />[dsi_studio_ubuntu_1804.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_ubuntu_1804.zip)<br />[dsi_studio_ubuntu_2004.zip](https://github.com/frankyeh/DSI-Studio/releases/download/2021.12.03/dsi_studio_ubuntu_2004.zip) | |



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

**Academic Use**
 
     DSI Studio is free for research purposes under the Attribution-NonCommercial-ShareAlike 2.0 Generic (CC BY-NC-SA 2.0) license.
     Please mention the usage of DSI Studio in your academic publications.

**Clinical Use**

     DSI Studio is NOT FDA-approved/cleared and provided "AS-IS."
     Using it on clinical research requires your institution's IRB approval. 
     Users should be attentive to issues reported on the user support forum and be responsible for timely software updates. 

# Optional Package

[Neonate/Infant1yr/Infant2yr template](https://pitt-my.sharepoint.com/:u:/g/personal/yehfc_pitt_edu/ERCWcDXswqJOgFj8xUqyPwYBBhHquH-JsdWHBIcRlcOi6g?e=SkwWd4) 
To install, unzip the files and move them to the /atlas folder (Windows). For Mac users, right-click on dsi_studio.app to [Show Content] and move the files under Content/MacOS/atlas

DSI Studio has a very high turning rate, and occasionally the computation outcome may be different between versions. I would recommend users keep a local copy of DSI Studio for each research project and only update DSI Studio if a new project is initiated.

# Hardware recommendation:

To achieve the best performance, I would recommend a computer with a multi-core CPU (e.g. http://store.hp.com/us/en/mdp/business-solutions/z840-workstation). Minimum memory of 2GB is needed. To handle a large number of tracks or image volumes, DSI Studio will need 32GB of memory or more. 

GPU computation is not yet supported in DSI Studio. 
