---
layout: home
title: U-Net Studio
---
<section class="section">
  <div>
    <h2 id="output">Output</h2>
    <p>U-Net Studio can output 3D labels or 4D probabilistic maps for quantifying tissue characteristics. The tissue segmentation includes white matter, gray matter (excluding basal ganglion), basal ganglion, and others.</p>
  </div>
  <div>
    <img src="/images/examples3.png" alt="U-Net Studio segmentation and tissue probability maps" style="max-width:340px;display:block;margin:0 auto">
  </div>
</section>

<section class="section">
  <div>
    <h2 id="about">About</h2>
    <p>U-Net Studio is a tissue segmentation tool for human and animal brain images. It devises a unique data augmentation method that allows for using only <strong>one template image</strong> to train a 3D U-Net from scratch.</p>
    <p>U-Net Studio provides segmentation models for mice, rats, marmosets, rhesus monkeys, and humans. These models are easily adaptable and retrainable for various imaging modalities, streamlining the segmentation process and reducing the need for manual annotation.</p>
  </div>
  <div>
    <p>The current version only provides skull-stripping and segmentation of white matter, gray matter, cerebellum cortex, and basal ganglia. More detailed segmentation is under planning.</p>
    <p>U-Net Studio is developed with its sister tool <a href="https://dsi-studio.labsolver.org">DSI Studio</a>. Many of the libraries are shared between them.</p>
  </div>
</section>

<p style="color:var(--muted);margin:8px 0 0">All models and training templates: <a href="/models.html">models</a>.</p>
