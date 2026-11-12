---
layout: home
title: U-Net Studio
---
<section class="output" id="output-sec">
  <div>
    <h2 id="output">Output</h2>
    <p>U-Net Studio can output 3D labels or 4D probabilistic maps for quantifying tissue characteristics. The tissue segmentation includes white matter, gray matter (excluding basal ganglion), basal ganglion, and others.</p>
  </div>
  <figure><img src="/images/examples3.png" alt="U-Net Studio segmentation and tissue probability maps"></figure>
</section>

<section class="about">
  <div>
    <h2 id="about">About</h2>
    <p>U-Net Studio is a tissue segmentation tool for human and animal brain images. It devises a unique data augmentation method that allows for using only <strong style="color:#16181d">one template image</strong> to train a 3D U-Net from scratch.</p>
    <p>U-Net Studio provides segmentation models for mice, rats, marmosets, rhesus monkeys, and humans. These models are easily adaptable and retrainable for various imaging modalities, streamlining the segmentation process and reducing the need for manual annotation.</p>
    <p>The current version only provides skull-stripping and segmentation of white matter, gray matter, cerebellum cortex, and basal ganglia. More detailed segmentation is under planning.</p>
    <p>U-Net Studio is developed with its sister tool <a href="https://dsi-studio.labsolver.org">DSI Studio</a>. Many of the libraries are shared between them.</p>
  </div>
  <div class="cite-card">
    <small>arXiv · 2023</small>
    <span>FC Yeh, "Brain MRI Segmentation using Template-Based Training and Visual Perception Augmentation", arXiv:2308.02363.</span>
    <a href="https://arxiv.org/abs/2308.02363">arxiv.org/abs/2308.02363</a> · <a href="/download.html#citation">How to cite</a>
    <span class="lic">Free for academic or research purposes under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode">CC BY-NC-SA 4.0</a>.</span>
  </div>
</section>

<section class="start">
  <div>
    <h2>Get started</h2>
    <p>Download, unzip and run. All models and training templates are on the <a href="/models.html" style="color:#9ab8ff">models</a> page.</p>
  </div>
  <div class="opts">
    <a href="/download.html">Download<small>Pre-release 2023.04.17</small></a>
    <a href="/models.html">Models<small>training templates</small></a>
    <a href="/evaluate.html">Segment images<small>step by step</small></a>
    <a href="https://groups.google.com/g/unet-studio">Forum<small>questions</small></a>
  </div>
</section>
