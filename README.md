# Awesome 3D Reconstruction Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Auto Update](https://github.com/Alleor/3D-reconstruction-paper/actions/workflows/update-papers.yml/badge.svg)](https://github.com/Alleor/3D-reconstruction-paper/actions/workflows/update-papers.yml)
![Papers](https://img.shields.io/badge/papers-364-blue)

A curated, automatically updated list of recent papers on 3D reconstruction.
收录 2021 年至今的三维重建论文，并自动发现新论文及其开源代码。

> Coverage: 2021–Present · Last content update: 2026-10-19 · Maintainer: [@Alleor](https://github.com/Alleor)

## About / 项目简介

这是一个面向三维视觉研究者和开发者的开源论文库，持续整理 2021 年至今三维重建领域的重要工作。仓库覆盖主流会议、期刊与 arXiv，提供论文、官方代码和荣誉链接，并通过 GitHub Actions 每周自动发现、筛选、去重、分类和更新最新文献。

An open-source paper collection for 3D vision researchers and developers, continuously tracking important 3D reconstruction work published since 2021. It covers major conferences, journals, and arXiv, provides paper, official-code, and honor links, and uses GitHub Actions to discover, filter, deduplicate, classify, and update the collection every week.

### Highlights / 项目亮点

- 📚 Mutually exclusive task categories / 清晰且互不重叠的任务分类
- 📄 Paper and official-code links / 论文与官方代码链接
- 🏆 Verified paper awards and distinctions / 经官方来源核实的论文奖项与荣誉
- 📈 Visual development timeline / 可视化三维重建发展时间线
- 🔄 Automatic weekly updates / 每周自动更新
- 🔍 Automatic discovery, filtering, and deduplication / 自动发现、筛选与去重
- 📅 Coverage since 2021 / 持续覆盖 2021 年至今的研究成果

### Research Areas / 研究分类

| # | 中文分类 | English Category |
|--:|:--|:--|
| 1 | 前馈几何与基础模型 | Feed-Forward Geometry & Foundation Models |
| 2 | 稠密深度、表面与网格重建 | Dense Depth, Surface & Mesh Reconstruction |
| 3 | NeRF 与新视角合成 | NeRF & Novel View Synthesis |
| 4 | Gaussian Splatting | Gaussian Splatting |
| 5 | 动态与 4D 重建 | Dynamic & 4D Reconstruction |
| 6 | 对象、人体与 3D 生成 | Object, Human & 3D Generation |
| 7 | 语义三维重建 | Semantic 3D Reconstruction |
| 8 | SLAM、机器人与建图 | SLAM, Robotics & Mapping |

If this repository helps your research, literature review, or project development, please consider giving it a ⭐ **Star**. Issues and pull requests are always welcome!

如果这个仓库对你的科研、文献调研或项目开发有所帮助，欢迎点一个 ⭐ **Star**，也欢迎通过 Issue 或 Pull Request 推荐论文、补充代码和修正信息！

## Scope

Primary discovery venues: CVPR, ICCV, ECCV, TPAMI, IROS, ICRA, TRO, RA-L, ICLR, 3DV, arXiv. Coverage starts on January 1, 2021 and continues to the present. The complete reference list is also mirrored, so its additional venues are preserved. Papers without a confidently matched official implementation are marked **Code pending**. Honors are manually verified against official conference, journal, or author sources.

## Development Timeline / 发展时间线

Follow every paper along a central 2021–Present timeline, with papers alternating on both sides and colors showing the evolution of each research direction.

沿一条 2021 年至今的主线浏览全部论文；论文交替排列在两侧，并通过分类颜色观察不同研究方向的发展趋势。

### [Explore the full visual timeline → / 查看完整可视化时间线 →](TIMELINE.md)

## Contents

- [Feed-Forward Geometry & Foundation Models](#feed-forward-geometry--foundation-models)
- [Dense Depth, Surface & Mesh Reconstruction](#dense-depth-surface--mesh-reconstruction)
- [NeRF & Novel View Synthesis](#nerf--novel-view-synthesis)
- [Gaussian Splatting](#gaussian-splatting)
- [Dynamic & 4D Reconstruction](#dynamic--4d-reconstruction)
- [Object, Human & 3D Generation](#object-human--3d-generation)
- [Semantic 3D Reconstruction](#semantic-3d-reconstruction)
- [SLAM, Robotics & Mapping](#slam-robotics--mapping)

## Taxonomy

Categories are mutually exclusive and follow each paper's primary task. Method properties such as self-supervision, efficiency, or scalability do not create duplicate categories.

| Category | Scope | Papers |
|:--|:--|--:|
| [Feed-Forward Geometry & Foundation Models](#feed-forward-geometry--foundation-models) | General-purpose visual geometry, camera/point prediction, SfM, and feed-forward reconstruction foundation models. | 97 |
| [Dense Depth, Surface & Mesh Reconstruction](#dense-depth-surface--mesh-reconstruction) | Methods whose primary output is dense depth, a mesh, TSDF/SDF, planes, or multi-view-stereo surface geometry. | 16 |
| [NeRF & Novel View Synthesis](#nerf--novel-view-synthesis) | Neural radiance fields and non-Gaussian novel/free-view synthesis. | 31 |
| [Gaussian Splatting](#gaussian-splatting) | Static-scene or generalizable reconstruction whose primary representation is Gaussian splatting. | 104 |
| [Dynamic & 4D Reconstruction](#dynamic--4d-reconstruction) | Time-varying scenes, motion-aware geometry, scene flow, and 4D rendering. | 37 |
| [Object, Human & 3D Generation](#object-human--3d-generation) | Object-centric reconstruction, humans/avatars, and explicit 3D or scene generation. | 32 |
| [Semantic 3D Reconstruction](#semantic-3d-reconstruction) | Joint geometry with semantic, instance, or panoptic understanding. | 15 |
| [SLAM, Robotics & Mapping](#slam-robotics--mapping) | SLAM, odometry, robotic reconstruction, and local or large-scale mapping. | 32 |

## Venue coverage

| Venue | Papers |
|:--|--:|
| CVPR | 51 |
| ICCV | 8 |
| ECCV | 6 |
| TPAMI | 3 |
| IROS | 1 |
| ICRA | 2 |
| TRO | 2 |
| RA-L | 3 |
| ICLR | 15 |
| 3DV | 4 |
| arXiv | 263 |
| CVPRF | 2 |
| ICME | 1 |
| ICML | 1 |
| NeurIPS | 1 |
| SIGGRAPH Asia | 1 |

## Honors / 论文荣誉

Verified paper awards and official highlight selections. Click an honor to open its source.

| Paper | Honor |
|:--|:--|
| Efficiently Reconstructing Dynamic Scenes One D4RT at a Time | 🏆 [CVPR 2026 Best Paper](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) |
| FlowR: Flowing from Sparse to Dense 3D Reconstructions | 🏆 [ICCV 2025 Highlight](https://iccv.thecvf.com/virtual/2025/poster/759) |
| Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction | 🏆 [ICCV 2025 Highlight](https://iccv.thecvf.com/virtual/2025/poster/2494) |
| MegaSaM: Accurate, Fast, and Robust Structure and Motion from Casual Dynamic Videos | 🏆 [CVPR 2025 Best Paper Honorable Mention](https://cvpr.thecvf.com/Conferences/2025/News/Awards_Press) |
| VGGT: Visual Geometry Grounded Transformer | 🏆 [CVPR 2025 Best Paper](https://cvpr.thecvf.com/Conferences/2025/News/Awards_Press) |
| NICER-SLAM: Neural Implicit Scene Encoding for RGB SLAM | 🏆 [3DV 2024 Best Paper Honorable Mention](https://nicer-slam.github.io/) |
| pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction | 🏆 [CVPR 2024 Best Paper Honorable Mention](https://tc.computer.org/tcpami/awards/cvpr-paper-awards/) |
| 3D Gaussian Splatting for Real-Time Radiance Field Rendering | 🏆 [SIGGRAPH 2023 Best Paper](https://blog.siggraph.org/2025/03/a-path-to-smarter-more-effective-designs.html/) |
| Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems | 🏆 [IEEE T-RO King-Sun Fu Memorial Best Paper Award](https://www.ieee-ras.org/awards-recognition/publications-awards/ieee-transactions-on-robotics-king-sun-fu-memorial-best-paper-award/) |

## Feed-Forward Geometry & Foundation Models

- **3D-USE: From Image-Level to Scene-Level Underwater Enhancement** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.28020) · **Code pending** ([search](https://github.com/search?q=%223D-USE%3A%20From%20Image-Level%20to%20Scene-Level%20Underwater%20Enhancement%22&type=repositories))
- **3D-VITAL: Visibility-aware Identity Training from Artificial Liftings of 3D Reconstruction model for Cross-View Object Re-Identification** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.16692) · [Code](https://github.com/TurtleSmoke/3D-VITAL)
- **AMB3R: Accurate Feed-forward Metric-scale 3D Reconstruction with Backend** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2511.20343) · [Code](https://github.com/HengyiWang/amb3r)
- **Argos: Adapt Rich Geometric Priors for Generalizable Online Scene-Change-Detection** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.10181) · **Code pending** ([search](https://github.com/search?q=%22Argos%3A%20Adapt%20Rich%20Geometric%20Priors%20for%20Generalizable%20Online%20Scene-Change-Detection%22&type=repositories))
- **Automated Maize Ear Phenotyping Using 3D Reconstructions** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.01921) · **Code pending** ([search](https://github.com/search?q=%22Automated%20Maize%20Ear%20Phenotyping%20Using%203D%20Reconstructions%22&type=repositories))
- **BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.16330) · **Code pending** ([search](https://github.com/search?q=%22BAT3R%3A%20Robust%20Online%203D%20Reconstruction%20with%20Bayesian%20Adaptive%20State%20Updates%22&type=repositories))
- **CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.26656) · **Code pending** ([search](https://github.com/search?q=%22CoGeo-GS%3A%20Concept-Driven%20and%20Geometry-Aware%20Multi-Object%20Removal%20in%203D%20Scenes%22&type=repositories))
- **Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.27301) · **Code pending** ([search](https://github.com/search?q=%22Comparative%20Evaluation%20of%203D%20Reconstruction%20Methods%20for%20Immersive%20Visualization%20of%20Laboratory%20Objects%22&type=repositories))
- **CoTL: Compact Token Learning for 3D Scene Representation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.18446) · **Code pending** ([search](https://github.com/search?q=%22CoTL%3A%20Compact%20Token%20Learning%20for%203D%20Scene%20Representation%22&type=repositories))
- **Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.26383) · **Code pending** ([search](https://github.com/search?q=%22Cross-Platform%20Benchmark%20of%20Neural%203D%20Reconstruction%20for%20Autonomous%20Laboratory%20Robots%22&type=repositories))
- **DA-NBV: A Direction-Aware Next-Best-View Planner for Efficient 3D Reconstruction of Ships at Sea** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.08025) · [Code](https://github.com/Fo-OLLL/DA-NBV)
- **DAGE: Dual-Stream Architecture for Efficient and Fine-Grained Geometry Estimation** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.03744) · [Code](https://github.com/ngoductuanlhp/DAGE)
- **DecomVoxel: Harnessing 3D-Native Priors with Guided In-situ Denoising Optimization for Decompositional Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01914) · [Code](https://github.com/DecomVoxel/DecomVoxel)
- **Denoising-Aware Temporal Point Cloud Completion for 3D Crop Architecture Recovery and Phenotypic Trait Extraction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.28343) · **Code pending** ([search](https://github.com/search?q=%22Denoising-Aware%20Temporal%20Point%20Cloud%20Completion%20for%203D%20Crop%20Architecture%20Recovery%20and%20Phenotypic%20Trait%20Extraction%22&type=repositories))
- **Depth Anything 3: Recovering the Visual Space from Any Views** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2511.10647) · [Code](https://depth-anything-3.github.io/)
- **DICAROS: Diffeomorphic Ancestral Shape Reconstruction on Phylogenies** — *arXiv 2026* · [Paper](https://doi.org/10.64898/2026.08.21.746152) · **Code pending** ([search](https://github.com/search?q=%22DICAROS%3A%20Diffeomorphic%20Ancestral%20Shape%20Reconstruction%20on%20Phylogenies%22&type=repositories))
- **Digital Holography with Deep Learning for 3D Reconstruction** — *arXiv 2026* · [Paper](https://doi.org/10.5281/zenodo.22136495) · **Code pending** ([search](https://github.com/search?q=%22Digital%20Holography%20with%20Deep%20Learning%20for%203D%20Reconstruction%22&type=repositories))
- **Diversity-aware View Partitioning for Scalable VGGT** — *ECCV 2026* · [Paper](https://arxiv.org/abs/2607.01885) · [Code](https://github.com/jspark1213/DA-VGGT)
- **Domain Adaptation of SAM 2.1 for Building-Component Segmentation in Image-Based 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.12786) · **Code pending** ([search](https://github.com/search?q=%22Domain%20Adaptation%20of%20SAM%202.1%20for%20Building-Component%20Segmentation%20in%20Image-Based%203D%20Reconstruction%22&type=repositories))
- **Déjà View: Looping Transformers for Multi-View 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2605.30215) · [Code](https://github.com/nv-tlabs/dvlt)
- **ExMesh++: From Multi-View Images to Relightable UV-PBR Mesh Assets via Topology-Adaptive Reconstruction and Decomposition** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.24109) · **Code pending** ([search](https://github.com/search?q=%22ExMesh%2B%2B%3A%20From%20Multi-View%20Images%20to%20Relightable%20UV-PBR%20Mesh%20Assets%20via%20Topology-Adaptive%20Reconstruction%20and%20Decomposition%22&type=repositories))
- **Faster VGGT with Block-Sparse Global Attention** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2509.07120) · [Code](https://github.com/brianwang00001/sparse-vggt)
- **FastVGGT: Training-Free Acceleration of Visual Geometry Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2509.02560) · [Code](https://github.com/mystorm16/FastVGGT)
- **FF3R: Feedforward Feature 3D Reconstruction from Unconstrained views** — *CVPRF 2026* · [Paper](https://arxiv.org/abs/2604.09862) · [Code](https://github.com/ChaoyiZh/ff3r)
- **From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.27455) · [Code](https://ranrhuang.github.io/nas3r/)
- **Generating Multi-view Adversarial Examples for Visual Geometry Grounded Transformer** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.20748) · [Code](https://github.com/qsong2001/mvap-g)
- **GenRec: Knowing Where to Reconstruct and Where to Generate** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17832) · [Code](https://github.com/atcelen/GenRec)
- **GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2605.23888) · [Code](https://kasothaphie.github.io/GenRecon/)
- **GeoPano: Towards Geometrically Accurate 3D Reconstruction from a Single Panorama** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.21297) · **Code pending** ([search](https://github.com/search?q=%22GeoPano%3A%20Towards%20Geometrically%20Accurate%203D%20Reconstruction%20from%20a%20Single%20Panorama%22&type=repositories))
- **GeoWeaver: Accurate Long-Sequence 3D Reconstruction via Hierarchical Geometric Assembly** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17389) · **Code pending** ([search](https://github.com/search?q=%22GeoWeaver%3A%20Accurate%20Long-Sequence%203D%20Reconstruction%20via%20Hierarchical%20Geometric%20Assembly%22&type=repositories))
- **Glass Surface Detection Grounded in 3D Visual Geometry** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.26752) · **Code pending** ([search](https://github.com/search?q=%22Glass%20Surface%20Detection%20Grounded%20in%203D%20Visual%20Geometry%22&type=repositories))
- **HD-VGGT: High-Resolution Visual Geometry Transformer** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.27222) · **Code pending** ([search](https://github.com/search?q=%22HD-VGGT%3A%20High-Resolution%20Visual%20Geometry%20Transformer%22&type=repositories))
- **HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2605.23889) · [Code](https://github.com/3DAgentWorld/HorizonStream/)
- **Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.38177) · [Code](https://github.com/cvlab-kaist/Imagine3D-LLM)
- **Latent Riemannian Flow Matching for Geometry-Grounded 3D Foundation Models** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2607.19120) · [Code](https://lisaweijler.github.io/geometry-grounded-rfm/)
- **LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01863) · [Code](https://github.com/LiteReality/LiteReality-Agent/)
- **LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.03269) · [Code](https://github.com/Junyi42/LoGeR)
- **MagicGarment: Benchmarking Single-Image Standalone 3D Garment Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.19623) · [Code](https://1019538157.github.io/MagicGarment/)
- **MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos** — *arXiv 2026* · [Paper](https://arxiv.org/pdf/2607.15211) · **Code pending** ([search](https://github.com/search?q=%22MAGiSt3R%3A%20Multi-Agent%20Feed-forward%203D%20Reconstruction%20from%20Monocular%20RGB%20Videos%22&type=repositories))
- **MapAnything: Universal Feed-Forward Metric 3D Reconstruction** — *3DV 2026* · [Paper](https://arxiv.org/abs/2509.13414) · [Code](https://github.com/facebookresearch/map-anything)
- **Matisse: Evidence-Space Reasoning for Active 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.38746) · **Code pending** ([search](https://github.com/search?q=%22Matisse%3A%20Evidence-Space%20Reasoning%20for%20Active%203D%20Reconstruction%22&type=repositories))
- **MERG3R: A Divide-and-Conquer Approach to Large-Scale Neural Visual Geometry** — *CVPR 2026* · [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_MERG3R_A_Divide-and-Conquer_Approach_to_Large-Scale_Neural_Visual_Geometry_CVPR_2026_paper.pdf) · [Code](https://github.com/LeoChengKX/MERG3R)
- **Monocular Panoramic Imaging for High-Precision 3D Shape Reconstruction** — *arXiv 2026* · [Paper](https://www.researchsquare.com/article/rs-8363056/latest.pdf) · **Code pending** ([search](https://github.com/search?q=%22Monocular%20Panoramic%20Imaging%20for%20High-Precision%203D%20Shape%20Reconstruction%22&type=repositories))
- **MRIo3DS-Net: a mutually reinforcing images to 3D surface RNN-like framework for model-adaptation indoor 3D reconstruction** — *arXiv 2026* · [Paper](https://doi.org/10.1016/j.isprsjprs.2026.08.035) · **Code pending** ([search](https://github.com/search?q=%22MRIo3DS-Net%3A%20a%20mutually%20reinforcing%20images%20to%203D%20surface%20RNN-like%20framework%20for%20model-adaptation%20indoor%203D%20reconstruction%22&type=repositories))
- **MVDG: Efficient Multi-view 3D Disambiguation on Unconstrained Real-World Images** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01098) · **Code pending** ([search](https://github.com/search?q=%22MVDG%3A%20Efficient%20Multi-view%203D%20Disambiguation%20on%20Unconstrained%20Real-World%20Images%22&type=repositories))
- **NOVA3R: Non-pixel-aligned Visual Transformer for Amodal 3D Reconstruction** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2603.04179) · [Code](https://wrchen530.github.io/nova3r/)
- **Offline Feed-Forward 3D Reconstruction at Scale** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2602.23361) · **Code pending** ([search](https://github.com/search?q=%22Offline%20Feed-Forward%203D%20Reconstruction%20at%20Scale%22&type=repositories))
- **OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2511.10560) · [Code](https://livioni.github.io/OmniVGGT-official/)
- **On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.00923) · [Code](https://github.com/Sh1nZzz/On_the_Fly3R)
- **OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.12461) · [Code](https://ouroworld.userwei.com)
- **PE3R: Perception-Efficient 3D Reconstruction** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2503.07507) · [Code](https://github.com/hujiecpp/pe3r)
- **PhysForge: Material-Controllable 3D Reconstruction with Separable Components** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.13681) · [Code](https://masterwanna.github.io/PhysForge.html)
- **Point-Based 3D Reconstruction from Sparse Views under Known Illumination** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.20000) · **Code pending** ([search](https://github.com/search?q=%22Point-Based%203D%20Reconstruction%20from%20Sparse%20Views%20under%20Known%20Illumination%22&type=repositories))
- **PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03341) · [Code](https://github.com/zvict/pointgt)
- **PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.11612) · [Code](https://github.com/Jiang-HB/PointVGGT)
- **Pose-Free Feed-Forward 3D Inpainting via Learnable Mask Attention and Support Token Refinement** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.11857) · [Code](https://rorisis.github.io/FreeInpaint/)
- **Quantized Visual Geometry Grounded Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2509.21302) · [Code](https://github.com/wlfeng0509/QuantVGGT)
- **Reliev3R: Relieving Feed-forward 3D Reconstruction from Multi-View Geometric Annotations** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.00548) · **Code pending** ([search](https://github.com/search?q=%22Reliev3R%3A%20Relieving%20Feed-forward%203D%20Reconstruction%20from%20Multi-View%20Geometric%20Annotations%22&type=repositories))
- **Remember, Revisit, Revise: Scaffold Memory for Long-Horizon 3D Geometry** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.19674) · **Code pending** ([search](https://github.com/search?q=%22Remember%2C%20Revisit%2C%20Revise%3A%20Scaffold%20Memory%20for%20Long-Horizon%203D%20Geometry%22&type=repositories))
- **Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03657) · **Code pending** ([search](https://github.com/search?q=%22Rethinking%203D%20Noise%3A%20Learning%203D-Aware%20Video%20Priors%20via%20Optimization-Free%20Morphological%20Perturbations%22&type=repositories))
- **Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.07883) · **Code pending** ([search](https://github.com/search?q=%22Revar3r%3A%20gauge-aware%20perturbation%20uncertainty%20for%20feed-forward%203d%20reconstruction%22&type=repositories))
- **Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.27529) · [Code](https://github.com/amap-cvlab/ABot-Recon)
- **S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models** — *ICME 2026* · [Paper](https://arxiv.org/abs/2603.17625) · [Code](https://github.com/Powertony102/S-VGGT)
- **SAIL-Recon: Large SfM by Augmenting Scene Regression with Localization** — *3DV 2026* · [Paper](https://arxiv.org/abs/2508.17972) · [Code](https://hkust-sail.github.io/sail-recon)
- **Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.04201) · [Code](https://linjohnss.github.io/scal3r/)
- **Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2604.08542) · [Code](https://zju3dv.github.io/scal3r/)
- **ScaleVid: Geometry-Aware Video Object Scaling with Mesh-Free Inference** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.12232) · **Code pending** ([search](https://github.com/search?q=%22ScaleVid%3A%20Geometry-Aware%20Video%20Object%20Scaling%20with%20Mesh-Free%20Inference%22&type=repositories))
- **SCION: Scene Composition with Instanced Neural Primitives** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.02322) · [Code](https://light.princeton.edu/SCION)
- **Self-Supervised Learning for 3D Shape Reconstruction from Point Clouds** — *arXiv 2026* · [Paper](https://doi.org/10.5281/zenodo.22153652) · **Code pending** ([search](https://github.com/search?q=%22Self-Supervised%20Learning%20for%203D%20Shape%20Reconstruction%20from%20Point%20Clouds%22&type=repositories))
- **Slot3R: Set-Associative Spatial Memory for Streaming 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.12282) · **Code pending** ([search](https://github.com/search?q=%22Slot3R%3A%20Set-Associative%20Spatial%20Memory%20for%20Streaming%203D%20Reconstruction%22&type=repositories))
- **STream3R: Scalable Sequential 3D Reconstruction with Causal Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2508.10893) · [Code](https://github.com/NIRVANALAN/STream3R)
- **Surflo: Consistent 3D Surface Flow Model with Global State** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2606.13644) · [Code](https://anttwo.github.io/surflo/)
- **TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.02304) · **Code pending** ([search](https://github.com/search?q=%22TRACE%3A%20Ergodic%20Trajectory%20Optimization%20for%20Active%20Scene%20Reconstruction%22&type=repositories))
- **TTT3R: 3D Reconstruction as Test-Time Training** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2509.26645) · [Code](https://rover-xingyu.github.io/TTT3R/)
- **UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.06404) · [Code](https://github.com/Link-dev/UAV3DCrop)
- **UniQueR: Unified Query-based Feedforward 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.22851) · **Code pending** ([search](https://github.com/search?q=%22UniQueR%3A%20Unified%20Query-based%20Feedforward%203D%20Reconstruction%22&type=repositories))
- **Unlocking the Power of Critical Factors for 3D Visual Geometry Estimation** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2604.21713) · [Code](https://github.com/aim-uofa/CARVE)
- **VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01013) · [Code](https://github.com/kosakayamahoo-design/VASC)
- **VGGT-Ω** — *CVPR 2026* · [Paper](https://vggt-omega.github.io/assets/paper/preview_v3.pdf) · [Code](https://github.com/facebookresearch/vggt-omega)
- **Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.04381) · **Code pending** ([search](https://github.com/search?q=%22Where%20Appearance%20Fails%2C%20Geometry%20Recognizes%3A%20A%20CAD-Free%203D%20Shape%20Prior%20That%20Complements%20Vision%20Foundation%20Models%22&type=repositories))
- **Why 3D Reconstruction Breaks Down on Under-Ice AUV Video, and How to Predict It** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.19993) · **Code pending** ([search](https://github.com/search?q=%22Why%203D%20Reconstruction%20Breaks%20Down%20on%20Under-Ice%20AUV%20Video%2C%20and%20How%20to%20Predict%20It%22&type=repositories))
- **Zebra3D: Efficient Hybrid Foundation Models For Scalable 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.12727) · **Code pending** ([search](https://github.com/search?q=%22Zebra3D%3A%20Efficient%20Hybrid%20Foundation%20Models%20For%20Scalable%203D%20Reconstruction%22&type=repositories))
- **Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.04174) · **Code pending** ([search](https://github.com/search?q=%22Zero-Shot%20Novel%20Depth%20Synthesis%20Using%203D%20Foundation%20Models%20Scene%20Representations%22&type=repositories))
- **π³: Scalable Permutation-Equivariant Visual Geometry Learning** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2507.13347) · [Code](https://github.com/yyfz/Pi3)
- **🌐 Argus: Metric Panoramic 3D Reconstruction for Indoor Scenes** — *ECCV 2026* · [Paper](https://arxiv.org/abs/2606.30047) · [Code](https://argus-paper.realsee.ai/)
- **3D Reconstruction with Spatial Memory** — *3DV 2025* · [Paper](https://arxiv.org/abs/2408.16061) · [Code](https://github.com/HengyiWang/spann3r)
- **Continuous 3D Perception Model with Persistent State** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2501.12387) · [Code](https://cut3r.github.io/)
- **DiffusionSfM: Predicting Structure and Motion via Ray Origin and Endpoint Diffusion** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2505.05473) · [Code](https://github.com/QitaoZhao/DiffusionSfM)
- **Fast3R: Towards 3D Reconstruction of 1000+ Images in One Forward Pass** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2501.13928) · [Code](https://fast3r-3d.github.io/)
- **Matrix3D: Large Photogrammetry Model All-in-One** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2502.07685) · [Code](https://github.com/apple/ml-matrix3d)
- **Point3R: Streaming 3D Reconstruction with Explicit Spatial Pointer Memory** — *NeurIPS 2025* · [Paper](https://arxiv.org/abs/2507.02863) · [Code](https://github.com/YkiWu/Point3R)
- **Pow3R: Empowering Unconstrained 3D Reconstruction with Camera and Scene Priors** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2503.17316) · **Code pending** ([search](https://github.com/search?q=%22Pow3R%3A%20Empowering%20Unconstrained%203D%20Reconstruction%20with%20Camera%20and%20Scene%20Priors%22&type=repositories))
- **VGGT: Visual Geometry Grounded Transformer** — *CVPR 2025* · 🏆 [CVPR 2025 Best Paper](https://cvpr.thecvf.com/Conferences/2025/News/Awards_Press) · [Paper](https://arxiv.org/abs/2503.11651) · [Code](https://github.com/facebookresearch/vggt)
- **WinT3R: Window-Based Streaming Reconstruction With Camera Token Pool** — *arXiv 2025* · [Paper](https://arxiv.org/abs/2509.05296) · [Code](https://github.com/LiZizun/WinT3R)
- **WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting** — *arXiv 2025* · [Paper](https://arxiv.org/abs/2510.10726) · [Code](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror)
- **DUSt3R: Geometric 3D Vision Made Easy** — *CVPR 2024* · [Paper](https://arxiv.org/abs/2312.14132) · [Code](https://github.com/naver/dust3r)
- **Grounding Image Matching in 3D with MASt3R** — *ECCV 2024* · [Paper](https://arxiv.org/abs/2406.09756) · [Code](https://github.com/naver/mast3r)

## Dense Depth, Surface & Mesh Reconstruction

- **Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.10602) · **Code pending** ([search](https://github.com/search?q=%22Gaussian%20Sculpting%3A%20End-to-End%20Controllable%20Surface%20Reconstruction%20via%20Field%20Optimization%22&type=repositories))
- **MicroSDF: Microfacet-Driven Hybrid Neural SDFs for Mixed-Reflectance Surface Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.19681) · **Code pending** ([search](https://github.com/search?q=%22MicroSDF%3A%20Microfacet-Driven%20Hybrid%20Neural%20SDFs%20for%20Mixed-Reflectance%20Surface%20Reconstruction%22&type=repositories))
- **Sensor-Informed Per-Point Covariance for Structured-Light 3D Imaging** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.10888) · **Code pending** ([search](https://github.com/search?q=%22Sensor-Informed%20Per-Point%20Covariance%20for%20Structured-Light%203D%20Imaging%22&type=repositories))
- **StyleFields: Multi-Scale AdaIN-Modulated Implicit SDFs for Coarse-to-Fine 3D Shape Reconstruction and Editing** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.09200) · **Code pending** ([search](https://github.com/search?q=%22StyleFields%3A%20Multi-Scale%20AdaIN-Modulated%20Implicit%20SDFs%20for%20Coarse-to-Fine%203D%20Shape%20Reconstruction%20and%20Editing%22&type=repositories))
- **Surface Reconstruction from Range Scans Under Visibility Constraints** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.18005) · **Code pending** ([search](https://github.com/search?q=%22Surface%20Reconstruction%20from%20Range%20Scans%20Under%20Visibility%20Constraints%22&type=repositories))
- **T3lescope: Arbitrary-Resolution High-Fidelity Generative Surface Reconstruction from Images** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.03308) · [Code](https://pfnet-research.github.io/t3lescope/)
- **VISION-BASED DRY-MATERIAL INVENTORY ESTIMATION IN AUTONOMOUS LABORATORIES: RGB SEGMENTATION VERSUS RGB-D SURFACE RECONSTRUCTION** — *arXiv 2026* · [Paper](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv.15010138/v1) · **Code pending** ([search](https://github.com/search?q=%22VISION-BASED%20DRY-MATERIAL%20INVENTORY%20ESTIMATION%20IN%20AUTONOMOUS%20LABORATORIES%3A%20RGB%20SEGMENTATION%20VERSUS%20RGB-D%20SURFACE%20RECONSTRUCTION%22&type=repositories))
- **ZipMVS: Multi-View Stereo with Compressed Cost Volumes** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.28033) · [Code](https://github.com/JihnGlyn/ZipMVS)
- **MUSt3R: Multi-view Network for Stereo 3D Reconstruction** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2503.01661) · [Code](https://github.com/naver/must3r)
- **MonoPlane: Exploiting Monocular Geometric Cues for Generalizable 3D Plane Reconstruction** — *IROS 2024* · [Paper](https://arxiv.org/abs/2411.01226) · [Code](https://github.com/thuzhaowang/MonoPlane)
- **FineRecon: Depth-aware Feed-forward Network for Detailed 3D Reconstruction** — *ICCV 2023* · [Paper](https://arxiv.org/abs/2304.01480) · [Code](https://github.com/apple/ml-finerecon)
- **Neuralangelo: High-Fidelity Neural Surface Reconstruction** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2306.03092) · [Code](https://github.com/NVlabs/neuralangelo)
- **NOPE-SAC: Neural One-Plane RANSAC for Sparse-View Planar 3D Reconstruction** — *TPAMI 2023* · [Paper](https://arxiv.org/abs/2211.16799) · [Code](https://github.com/IceTTTb/NopeSAC)
- **NeuralWarp: Time-Warping for Neural Surface Reconstruction** — *CVPR 2022* · [Paper](https://arxiv.org/abs/2202.03848) · [Code](https://github.com/fdarmon/NeuralWarp)
- **GigaMVS: A Benchmark for Ultra-Large-Scale Gigapixel-Level 3D Reconstruction** — *TPAMI 2021* · [Paper](https://doi.org/10.1109/TPAMI.2021.3115028) · **Code pending** ([search](https://github.com/search?q=%22GigaMVS%3A%20A%20Benchmark%20for%20Ultra-Large-Scale%20Gigapixel-Level%203D%20Reconstruction%22&type=repositories))
- **NeuralRecon: Real-Time Coherent 3D Reconstruction from Monocular Video** — *CVPR 2021* · [Paper](https://arxiv.org/abs/2104.00681) · [Code](https://github.com/zju3dv/NeuralRecon)

## NeRF & Novel View Synthesis

- **ABCD: Alpha-Composited Block Coordinate Descent: Constant-VRAM Training for Large Radiance Fields** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.27735) · [Code](https://github.com/shiukaheng/abcd)
- **AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.19747) · [Code](https://github.com/OpenImagingLab/AnyRecon)
- **E-RayZer: Self-supervised 3D Reconstruction as Spatial Visual Pre-training** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.10950) · [Code](https://github.com/QitaoZhao/E-RayZer)
- **ESC: Escaping 2D Diffusion Ambiguity with Geometric Constraints for Consistent Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.23732) · **Code pending** ([search](https://github.com/search?q=%22ESC%3A%20Escaping%202D%20Diffusion%20Ambiguity%20with%20Geometric%20Constraints%20for%20Consistent%20Novel%20View%20Synthesis%22&type=repositories))
- **Feedforward Novel View Synthesis for Heterogeneous Cameras** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.03522) · **Code pending** ([search](https://github.com/search?q=%22Feedforward%20Novel%20View%20Synthesis%20for%20Heterogeneous%20Cameras%22&type=repositories))
- **Floating Radiance Networks** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.05920) · [Code](https://github.com/KByrski/FlaRe)
- **FreeScale: Scaling 3D scenes via Certainty-Aware Free-View Generation** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2604.10512) · [Code](https://github.com/mvp-ai-lab/FreeScale)
- **From Rays to Projections: Better Inputs for Feed-Forward View Synthesis** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2601.05116) · [Code](https://wuzirui.github.io/pvsm-web/)
- **LagerNVS: Latent Geometry for Fully Neural Real-Time Novel View Synthesis** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.20176) · [Code](https://github.com/facebookresearch/lagernvs)
- **Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.03717) · [Code](https://snap-nvs.github.io)
- **LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.12127) · **Code pending** ([search](https://github.com/search?q=%22LVS%3A%20Local%20View%20Synthesis%20from%20Relative%20Camera%20Pose%20by%20Reusing%20Previous%20Views%22&type=repositories))
- **LVSPM: Long Sequence View Synthesis and Pose Estimation Model** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.10960) · [Code](https://burningdust21.github.io/Projects/LVSPM)
- **MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.12442) · [Code](https://mv2-dataset.github.io/)
- **One-Shot Refiner: Boosting Feed-forward Novel View Synthesis via One-Step Diffusion** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2601.14161) · [Code](https://github.com/YitongD/One_Shot_Refiner)
- **PIVOT: A Multi-Trajectory Dataset and Testbed for Pose, Intrinsics, and Novel Viewpoint Evaluation in Real-World 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.25401) · **Code pending** ([search](https://github.com/search?q=%22PIVOT%3A%20A%20Multi-Trajectory%20Dataset%20and%20Testbed%20for%20Pose%2C%20Intrinsics%2C%20and%20Novel%20Viewpoint%20Evaluation%20in%20Real-World%203D%20Reconstruction%22&type=repositories))
- **Quantum implicit neural representations for 3D scene reconstruction and novel view synthesis** — *arXiv 2026* · [Paper](https://doi.org/10.1007/s42484-026-00426-0) · **Code pending** ([search](https://github.com/search?q=%22Quantum%20implicit%20neural%20representations%20for%203D%20scene%20reconstruction%20and%20novel%20view%20synthesis%22&type=repositories))
- **Reflection-aware Generative Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.05382) · [Code](https://kim-geonu.github.io/Ref-GeNVS/)
- **Stabilizing Camera-Controlled Novel View Synthesis at Inference Time** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03639) · **Code pending** ([search](https://github.com/search?q=%22Stabilizing%20Camera-Controlled%20Novel%20View%20Synthesis%20at%20Inference%20Time%22&type=repositories))
- **UniSHARP: Universal Sharp Monocular View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2606.07514) · [Code](https://github.com/Insta360-Research-Team/UniSHARP)
- **UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.04701) · **Code pending** ([search](https://github.com/search?q=%22UniWorld-View%3A%20Large-Baseline%20View%20Synthesis%20via%20Video%20Diffusion%20Models%22&type=repositories))
- **VGGT-Diff: Visual Geometry Meets Diffusion for Sparse-View Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.33253) · [Code](https://chenkangjie1123.github.io/VGGT-Diff/)
- **FlowR: Flowing from Sparse to Dense 3D Reconstructions** — *ICCV 2025* · 🏆 [ICCV 2025 Highlight](https://iccv.thecvf.com/virtual/2025/poster/759) · [Paper](https://arxiv.org/abs/2504.01647) · [Code](https://github.com/tobiasfshr/flowr)
- **LVSM: A Large View Synthesis Model with Minimal 3D Inductive Bias** — *ICLR 2025* · [Paper](https://arxiv.org/abs/2410.17242) · [Code](https://github.com/haian-jin/LVSM)
- **RayZer: A Self-supervised Large View Synthesis Model** — *ICCV 2025* · [Paper](https://arxiv.org/abs/2505.00702) · [Code](https://github.com/hwjiang1510/RayZer)
- **Sharp Monocular View Synthesis in Less Than a Second** — *arXiv 2025* · [Paper](https://arxiv.org/abs/2512.10685) · [Code](https://github.com/apple/ml-sharp)
- **VGGT-X: When VGGT Meets Dense Novel View Synthesis** — *arXiv 2025* · [Paper](https://arxiv.org/abs/2509.25191) · [Code](https://github.com/Linketic/VGGT-X)
- **Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields** — *CVPR 2022* · [Paper](https://arxiv.org/abs/2111.12077) · [Code](https://github.com/google-research/multinerf)
- **TensoRF: Tensorial Radiance Fields** — *ECCV 2022* · [Paper](https://arxiv.org/abs/2203.09517) · [Code](https://github.com/apchenstu/TensoRF)
- **IBRNet: Learning Multi-View Image-Based Rendering** — *CVPR 2021* · [Paper](https://arxiv.org/abs/2102.13090) · [Code](https://github.com/googleinterns/IBRNet)
- **MVSNeRF: Fast Generalizable Radiance Field Reconstruction from Multi-View Stereo** — *ICCV 2021* · [Paper](https://arxiv.org/abs/2103.15595) · [Code](https://github.com/apchenstu/mvsnerf)
- **pixelNeRF: Neural Radiance Fields from One or Few Images** — *CVPR 2021* · [Paper](https://arxiv.org/abs/2012.02190) · [Code](https://github.com/sxyu/pixel-nerf)

## Gaussian Splatting

- **3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17298) · **Code pending** ([search](https://github.com/search?q=%223D%20Gaussian%20Accelerated%20Ray%20Tracing%3A%20Fast%20training%20through%20particle-based%20backward%20propagation%22&type=repositories))
- **Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01114) · **Code pending** ([search](https://github.com/search?q=%22Affine-Aligned%20Atlas%20for%20Canonical%20Gaussian%20Construction%20in%20Video%20Representation%22&type=repositories))
- **Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.21634) · **Code pending** ([search](https://github.com/search?q=%22Anchor3DGS%3A%20Feed-Forward%203D%20Gaussian%20Splatting%20with%20Compact%20Anchor-Based%20Representation%22&type=repositories))
- **AnyGS2Mesh: Feed-Forward Mesh Reconstruction from 3D Gaussian Splatting with Arbitrary-Resolution Views** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03304) · **Code pending** ([search](https://github.com/search?q=%22AnyGS2Mesh%3A%20Feed-Forward%20Mesh%20Reconstruction%20from%203D%20Gaussian%20Splatting%20with%20Arbitrary-Resolution%20Views%22&type=repositories))
- **ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.30184) · [Code](https://github.com/WuJH2001/ATGS)
- **BRF-GS: Hyperspectral Bidirectional Reflectance Factor Modeling and Image Generation Based on 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.31159) · **Code pending** ([search](https://github.com/search?q=%22BRF-GS%3A%20Hyperspectral%20Bidirectional%20Reflectance%20Factor%20Modeling%20and%20Image%20Generation%20Based%20on%203D%20Gaussian%20Splatting%22&type=repositories))
- **Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.03162) · **Code pending** ([search](https://github.com/search?q=%22Budgeted-GS%3A%20Real-Time%20Large-Scale%20Gaussian%20Splatting%20via%20Factoring%20LOD%22&type=repositories))
- **C3G: Learning Compact 3D Representations with 2K Gaussians** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.04021) · [Code](https://github.com/cvlab-kaist/C3G)
- **CapFrame: Text-Instructed Viewpoint Grounding in 3D Gaussian Scenes via Geometric Pseudo Labels** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.30342) · [Code](https://github.com/jirongli/CapFrame)
- **CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.10345) · **Code pending** ([search](https://github.com/search?q=%22CasDeblurGS%3A%20Cascaded%202D-to-3D%20Multi-View%20Consistency%20for%203D%20Gaussian%20Splatting%20from%20Two%20Blurry%20Images%22&type=repositories))
- **CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.02206) · **Code pending** ([search](https://github.com/search?q=%22CLEAR%3A%20Conflict-aware%20Learning%20via%20Evidence-guided%20Adaptive%20Routing%20for%20Unified%20Sparse-View%203D%20Gaussian%20Super-Resolution%22&type=repositories))
- **Compact Neural Appearance Models for Efficient Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.05255) · **Code pending** ([search](https://github.com/search?q=%22Compact%20Neural%20Appearance%20Models%20for%20Efficient%20Gaussian%20Splatting%22&type=repositories))
- **CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.13177) · **Code pending** ([search](https://github.com/search?q=%22CompactSplat%3A%20Spatially%20Adaptive%20Gaussian%20Distribution%20for%20Feedforward%20Scene%20Reconstruction%22&type=repositories))
- **CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.18413) · **Code pending** ([search](https://github.com/search?q=%22CoMVS-GS%3A%20Collaborative%20Multi-View%20Stereo%20and%203D%20Gaussian%20Splatting%20for%20Surface%20Reconstruction%22&type=repositories))
- **Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.06117) · **Code pending** ([search](https://github.com/search?q=%22Confidence%20matters%3A%20Leveraging%20Multi-view%20Geometric%20Priors%20for%20GS-based%20Reconstruction%22&type=repositories))
- **CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2607.25569) · **Code pending** ([search](https://github.com/search?q=%22CORF-GS%3A%20Real-Time%20Wireless%20Radiance%20Field%20Reconstruction%20via%20Coupled%20Optical-RF%20Gaussian%20Splatting%22&type=repositories))
- **DeltaSplat: Iterative Gaussian Refinement for Pose-Free Feed-Forward 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.09853) · **Code pending** ([search](https://github.com/search?q=%22DeltaSplat%3A%20Iterative%20Gaussian%20Refinement%20for%20Pose-Free%20Feed-Forward%203D%20Gaussian%20Splatting%22&type=repositories))
- **DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.02191) · **Code pending** ([search](https://github.com/search?q=%22DerainSplat%3A%20Feed-Forward%20Clean%203D%20Gaussian%20Splatting%20from%20Sparse%20Rainy%20Views%22&type=repositories))
- **Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.01030) · [Code](https://liu115.github.io/diff3r)
- **DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.01516) · [Code](https://github.com/Akaneqwq/DualDiff3D)
- **EcoSplat: Efficiency-controllable Feed-forward 3D Gaussian Splatting from Multi-view Images** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.18692) · [Code](https://kaist-viclab.github.io/ecosplat-site/)
- **EffGS: Efficient and High-Fidelity Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.39553) · [Code](https://github.com/CypressLi01/EffGS)
- **EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01876) · **Code pending** ([search](https://github.com/search?q=%22EvenSplat%3A%20Coupled%202D-3D%20Decomposition%20for%20Gaussian%20Splatting%20under%20Exposure%20and%20Illumination%20Variation%22&type=repositories))
- **EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.08585) · **Code pending** ([search](https://github.com/search?q=%22EvTrajGS%3A%20Accurate%20and%20Efficient%203D%20Gaussian%20Splatting%20from%20Unposed%20Event%20Streams%22&type=repositories))
- **FactorSplat: Appearance-Controllable Gaussian Proxies for Medical Volume Rendering** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.02382) · [Code](https://gaozhongpai.github.io/FactorSplat/)
- **Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.20590) · **Code pending** ([search](https://github.com/search?q=%22Feed-Forward%20Multi-View%20Feature%20Coding%20for%203D%20Gaussian%20Splatting%22&type=repositories))
- **FlexSplat: Flexible Feed-Forward 3D Gaussian Splatting without Point Cloud Correspondence** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.07937) · **Code pending** ([search](https://github.com/search?q=%22FlexSplat%3A%20Flexible%20Feed-Forward%203D%20Gaussian%20Splatting%20without%20Point%20Cloud%20Correspondence%22&type=repositories))
- **FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.11364) · **Code pending** ([search](https://github.com/search?q=%22FlyMark%3A%20Training-Free%20Invisible%20Watermarking%20of%203D%20Gaussian%20Splatting%20via%20a%20Fruit%20Fly%20Connectome%22&type=repositories))
- **Frame-Consistent Feed-Forward 3D Gaussian Splatting from Sparse Unposed Images** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.23039) · **Code pending** ([search](https://github.com/search?q=%22Frame-Consistent%20Feed-Forward%203D%20Gaussian%20Splatting%20from%20Sparse%20Unposed%20Images%22&type=repositories))
- **GaussCast: Dependency-Aware Shared Block Retrieval for Multi-User Layered 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://www.researchsquare.com/article/rs-10239330/latest.pdf) · **Code pending** ([search](https://github.com/search?q=%22GaussCast%3A%20Dependency-Aware%20Shared%20Block%20Retrieval%20for%20Multi-User%20Layered%203D%20Gaussian%20Splatting%22&type=repositories))
- **Gaussian Density Splatting Network** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.10396) · [Code](https://github.com/infinite0522/GDSNet-Gaussian-Density-Splatting-Network)
- **Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.17513) · **Code pending** ([search](https://github.com/search?q=%22Gaussian%20Splatting%20for%20Real-Time%20Scene%20Reconstruction%3A%20Methods%2C%20Systems%2C%20and%20Trade-offs%22&type=repositories))
- **Gaussian Splatting Underwater: A Controlled Cross-Regime Study** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.25483) · [Code](https://github.com/olayasturias/uw3dgs)
- **Gaussian Splatting with Reflections Guided by What is Seen** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.13757) · **Code pending** ([search](https://github.com/search?q=%22Gaussian%20Splatting%20with%20Reflections%20Guided%20by%20What%20is%20Seen%22&type=repositories))
- **Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.15651) · [Code](https://amazingren.github.io/Gaussian-JEPA/)
- **GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17535) · **Code pending** ([search](https://github.com/search?q=%22GroupForward%3A%20Building%20Referable%203D%20Scenes%20via%20Instance-Grouped%20Feed-Forward%20Gaussian%20Splatting%22&type=repositories))
- **GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.13502) · **Code pending** ([search](https://github.com/search?q=%22GS%24%5E%7B2%7D%24CI%3A%20Robust%20Gaussian%20Splatting%20For%20Snapshot%20Compressive%20Imaging%20via%20Large%20Vision%20Model%20Priors%22&type=repositories))
- **GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.19066) · **Code pending** ([search](https://github.com/search?q=%22GS-VLA%3A%20Plug-and-Play%20Viewpoint%20Canonicalization%20for%20Frozen%20VLA%20Policies%20via%20Gaussian%20Splatting%22&type=repositories))
- **HandSplatter: Automated Digital Goniometry from Neural Rendering** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.09735) · **Code pending** ([search](https://github.com/search?q=%22HandSplatter%3A%20Automated%20Digital%20Goniometry%20from%20Neural%20Rendering%22&type=repositories))
- **HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.14136) · [Code](https://github.com/WZ-CS/HiCo-GS)
- **HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01056) · **Code pending** ([search](https://github.com/search?q=%22HierGF%3A%20Hierarchical%20Gaussian%20Fields%20via%20Geometry-perception%20Message%20Passing%20for%20Sparse-view%203D%20Reconstruction%22&type=repositories))
- **High-quality underwater 3D Gaussian splatting reconstruction with multiview consistency constraints** — *ICCV 2026* · [Paper](https://doi.org/10.1117/12.3120435) · **Code pending** ([search](https://github.com/search?q=%22High-quality%20underwater%203D%20Gaussian%20splatting%20reconstruction%20with%20multiview%20consistency%20constraints%22&type=repositories))
- **InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.02747) · **Code pending** ([search](https://github.com/search?q=%22InceptionGS%3A%20Generative%20Bootstrapping%20for%20Large-Scale%20Gaussian%20Splatting%20under%20Unstructured%20View%20Sampling%22&type=repositories))
- **JSGS: JPEG State-Guided Supervision for 3D Gaussian Splatting from Mixed-Quality Views** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.08659) · [Code](https://github.com/Jayden-Cui/JSGS)
- **LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.16324) · **Code pending** ([search](https://github.com/search?q=%22LaGSplat%3A%20Inferring%20Physics-Governed%20Interactive%20Simulation%20from%20Monocular%20Video%20Using%20Latent%20Lagrangian%20Gaussian%20Splatting%22&type=repositories))
- **Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03334) · **Code pending** ([search](https://github.com/search?q=%22Laplacian%20Frequency%20Hierarchies%20for%20Efficient%203D%20Gaussian%20Splatting%20Training%22&type=repositories))
- **LEGS: Laplacian-Enhanced Gaussian Splatting with a Nonlinear Weighted Loss** — *arXiv 2026* · [Paper](https://doi.org/10.1145/3822516.3834868) · **Code pending** ([search](https://github.com/search?q=%22LEGS%3A%20Laplacian-Enhanced%20Gaussian%20Splatting%20with%20a%20Nonlinear%20Weighted%20Loss%22&type=repositories))
- **Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2603.25745) · [Code](https://yxlao.github.io/lgtm)
- **Leveling3D: Leveling Up 3D Reconstruction withFeed-Forward 3D Gaussian Splatting andGeometry-Aware Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.16211) · **Code pending** ([search](https://github.com/search?q=%22Leveling3D%3A%20Leveling%20Up%203D%20Reconstruction%20withFeed-Forward%203D%20Gaussian%20Splatting%20andGeometry-Aware%20Generation%22&type=repositories))
- **LL-3DGS Reconstruction: Degradation-Consistent Gaussian Splatting for Monocular Low-Light Scenes** — *arXiv 2026* · [Paper](https://doi.org/10.20944/preprints202608.1777.v1) · **Code pending** ([search](https://github.com/search?q=%22LL-3DGS%20Reconstruction%3A%20Degradation-Consistent%20Gaussian%20Splatting%20for%20Monocular%20Low-Light%20Scenes%22&type=repositories))
- **LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.12825) · [Code](https://leo-frank.github.io/LocusGS_viewer)
- **LonGaussian: Tracking Foundation Priors for Long-Context Feedforward Gaussian Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.23250) · **Code pending** ([search](https://github.com/search?q=%22LonGaussian%3A%20Tracking%20Foundation%20Priors%20for%20Long-Context%20Feedforward%20Gaussian%20Reconstruction%22&type=repositories))
- **Make It Flow: Animating Water in 3D Gaussian Splatting Scenes** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.13860) · **Code pending** ([search](https://github.com/search?q=%22Make%20It%20Flow%3A%20Animating%20Water%20in%203D%20Gaussian%20Splatting%20Scenes%22&type=repositories))
- **NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17447) · **Code pending** ([search](https://github.com/search?q=%22NGS-Marker%3A%20Robust%20Native%20Watermarking%20for%203D%20Gaussian%20Splatting%22&type=repositories))
- **NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.13309) · [Code](https://github.com/POSE-Lab/novasplat}{https://github.com/POSE-Lab/novasplat)
- **NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.37115) · **Code pending** ([search](https://github.com/search?q=%22NRF-GS%3A%20Neural%20Residual%20Fields%20for%20Expressive%20and%20Compact%20Gaussian%20Splatting%22&type=repositories))
- **ObjectSplat: Improving Mesh Fidelity and Interactivity for 3D Scenes via Object-Level Mesh Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.30423) · **Code pending** ([search](https://github.com/search?q=%22ObjectSplat%3A%20Improving%20Mesh%20Fidelity%20and%20Interactivity%20for%203D%20Scenes%20via%20Object-Level%20Mesh%20Splatting%22&type=repositories))
- **Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.15508) · [Code](https://arthurmoreau.github.io/OffTheGrid/)
- **One Setting, Any Scene: Tuning-Free Model-Size Control for 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://www.researchsquare.com/article/rs-10987108/latest.pdf) · **Code pending** ([search](https://github.com/search?q=%22One%20Setting%2C%20Any%20Scene%3A%20Tuning-Free%20Model-Size%20Control%20for%203D%20Gaussian%20Splatting%22&type=repositories))
- **PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.11572) · **Code pending** ([search](https://github.com/search?q=%22PAM-ToD%3A%20Plug-and-Play%20Appearance%20Modeling%20for%20Cross-Time-of-Day%203D%20Gaussian%20Splatting%22&type=repositories))
- **PanoLess: Environment Reconstruction from Partial Reflective Views** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2607.25362) · **Code pending** ([search](https://github.com/search?q=%22PanoLess%3A%20Environment%20Reconstruction%20from%20Partial%20Reflective%20Views%22&type=repositories))
- **PanoramicSplat: Scaling 3D Gaussian Splatting for Single-View Large-Scale Outdoor Reconstruction** — *arXiv 2026* · [Paper](https://www.researchsquare.com/article/rs-11014476/latest.pdf) · **Code pending** ([search](https://github.com/search?q=%22PanoramicSplat%3A%20Scaling%203D%20Gaussian%20Splatting%20for%20Single-View%20Large-Scale%20Outdoor%20Reconstruction%22&type=repositories))
- **PCAsplat: Gaussian Splatting with Local PCA Regularization** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.11011) · **Code pending** ([search](https://github.com/search?q=%22PCAsplat%3A%20Gaussian%20Splatting%20with%20Local%20PCA%20Regularization%22&type=repositories))
- **Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.26951) · **Code pending** ([search](https://github.com/search?q=%22Per-View%20Gaussian%20Predictions%20Enable%20Training-Free%20Distractor%20Filtering%20in%20Feed-Forward%203DGS%22&type=repositories))
- **Physics-Integrated Operator Learning via Gaussian Splatting Representations** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.24049) · **Code pending** ([search](https://github.com/search?q=%22Physics-Integrated%20Operator%20Learning%20via%20Gaussian%20Splatting%20Representations%22&type=repositories))
- **Pose-Free Omnidirectional Gaussian Splatting for 360-Degree Videos with Consistent Depth Priors** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.23324) · [Code](https://github.com/zcq15/PFGS360)
- **Prior-Driven Enhancements in 3D Gaussian Splatting: Normals and Depths Regularization** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.36969) · **Code pending** ([search](https://github.com/search?q=%22Prior-Driven%20Enhancements%20in%203D%20Gaussian%20Splatting%3A%20Normals%20and%20Depths%20Regularization%22&type=repositories))
- **ProbSplat: Efficient Probabilistic Hardware for Gaussian Splatting in 3D Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.13143) · **Code pending** ([search](https://github.com/search?q=%22ProbSplat%3A%20Efficient%20Probabilistic%20Hardware%20for%20Gaussian%20Splatting%20in%203D%20Scene%20Reconstruction%22&type=repositories))
- **PSCD-GS: Role-Aware Perception-Structure Collaborative Densification for 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://www.researchsquare.com/article/rs-10466466/latest.pdf) · **Code pending** ([search](https://github.com/search?q=%22PSCD-GS%3A%20Role-Aware%20Perception-Structure%20Collaborative%20Densification%20for%203D%20Gaussian%20Splatting%22&type=repositories))
- **QuantumGS: Quantum Encoding Framework for Gaussian Splatting** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2602.05047) · **Code pending** ([search](https://github.com/search?q=%22QuantumGS%3A%20Quantum%20Encoding%20Framework%20for%20Gaussian%20Splatting%22&type=repositories))
- **QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.01186) · [Code](https://github.com/inspatio/querysplat)
- **RDGSplat: Render-Dedicated Geometry for Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.09173) · **Code pending** ([search](https://github.com/search?q=%22RDGSplat%3A%20Render-Dedicated%20Geometry%20for%20Novel%20View%20Synthesis%22&type=repositories))
- **ResStreamGS: Residual-Sensitive Dual-Stream Gaussian Splatting for Mobile Volumetric Video Streaming** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.21121) · **Code pending** ([search](https://github.com/search?q=%22ResStreamGS%3A%20Residual-Sensitive%20Dual-Stream%20Gaussian%20Splatting%20for%20Mobile%20Volumetric%20Video%20Streaming%22&type=repositories))
- **RoofGS: Roofline-Guided End-to-End Acceleration of 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.15785) · **Code pending** ([search](https://github.com/search?q=%22RoofGS%3A%20Roofline-Guided%20End-to-End%20Acceleration%20of%203D%20Gaussian%20Splatting%22&type=repositories))
- **S2Tok: Streaming 3D Gaussian Reconstruction with Persistent Spatial Tokens** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.08978) · [Code](https://github.com/Applied-Intuition-Open-Source/S2Tok)
- **Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.11928) · **Code pending** ([search](https://github.com/search?q=%22Seed2GS%3A%20Camera-Free%2C%20Training-Free%20Object%20Extraction%20from%203D%20Gaussian%20Scenes%20via%20a%20Single%20Reference-View%20Grounding%22&type=repositories))
- **SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.16863) · **Code pending** ([search](https://github.com/search?q=%22SplatGuide%3A%20Geometric%20Priors%20from%203D%20Gaussians%20for%20Pose-Free%20Novel%20View%20Synthesis%22&type=repositories))
- **SplatQ: Interaction-Aware Pruning of 3D Gaussian Splatting via Quadratic Selection** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.13503) · **Code pending** ([search](https://github.com/search?q=%22SplatQ%3A%20Interaction-Aware%20Pruning%20of%203D%20Gaussian%20Splatting%20via%20Quadratic%20Selection%22&type=repositories))
- **STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03447) · **Code pending** ([search](https://github.com/search?q=%22STARS-GS%3A%20Structure-Aware%20Regularized%20Gaussian%20Splatting%20for%20Large-Scale%20Aerial%20Surface%20Reconstruction%22&type=repositories))
- **StereoGaussians: Feed-Forward 3D Gaussian Splatting from Stereo Images** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.38592) · **Code pending** ([search](https://github.com/search?q=%22StereoGaussians%3A%20Feed-Forward%203D%20Gaussian%20Splatting%20from%20Stereo%20Images%22&type=repositories))
- **Stipple: Real-Time Incremental Gaussian Splatting with Visual-Inertial Tracking** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.00931) · **Code pending** ([search](https://github.com/search?q=%22Stipple%3A%20Real-Time%20Incremental%20Gaussian%20Splatting%20with%20Visual-Inertial%20Tracking%22&type=repositories))
- **Swimm3R: Splatting with Medium-aware SfM for Underwater 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.00950) · **Code pending** ([search](https://github.com/search?q=%22Swimm3R%3A%20Splatting%20with%20Medium-aware%20SfM%20for%20Underwater%203D%20Reconstruction%22&type=repositories))
- **TileSkipper: Region-Adaptive Tile Pruning for 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.09343) · **Code pending** ([search](https://github.com/search?q=%22TileSkipper%3A%20Region-Adaptive%20Tile%20Pruning%20for%203D%20Gaussian%20Splatting%22&type=repositories))
- **TopoSurfel: Closing the Loop between Gaussian Surfels and Meshes for Surface Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.20687) · [Code](https://github.com/Fan-Treasure/TopoSurfel)
- **TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03534) · [Code](https://github.com/DubiousCactus/trunc-grad-gs)
- **UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.39089) · **Code pending** ([search](https://github.com/search?q=%22UGOD%3A%20Uncertainty-Guided%20Opacity%20and%20Dropout%20for%20Sparse-View%203D%20Gaussian%20Splatting%22&type=repositories))
- **VisibilitySplat: Ray-Traced Occlusion for Relighting with 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.19847) · **Code pending** ([search](https://github.com/search?q=%22VisibilitySplat%3A%20Ray-Traced%20Occlusion%20for%20Relighting%20with%203D%20Gaussian%20Splatting%22&type=repositories))
- **Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.10682) · **Code pending** ([search](https://github.com/search?q=%22Visual%20Geometry%20Foundation-Aware%20Gaussians%20for%20Single-Frame%20Surround-View%20Driving%20Reconstruction%22&type=repositories))
- **What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.00749) · **Code pending** ([search](https://github.com/search?q=%22What%20Builds%20the%20Scene%3F%20Luminance%20Dominates%20Geometry%20Formation%20in%203D%20Gaussian%20Splatting%22&type=repositories))
- **When 3D Gaussian Splatting Recovers Real Surfaces** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.30054) · **Code pending** ([search](https://github.com/search?q=%22When%203D%20Gaussian%20Splatting%20Recovers%20Real%20Surfaces%22&type=repositories))
- **Where Should the Gaussians Go? Reusable Label-Aware Allocation for Budget-Constrained Gaussian Splatting of Cinematic CT** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.20397) · **Code pending** ([search](https://github.com/search?q=%22Where%20Should%20the%20Gaussians%20Go%3F%20Reusable%20Label-Aware%20Allocation%20for%20Budget-Constrained%20Gaussian%20Splatting%20of%20Cinematic%20CT%22&type=repositories))
- **WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.28240) · **Code pending** ([search](https://github.com/search?q=%22WilLaGS%3A%20Latent-Conditional%203D%20Appearance%20Fields%20for%20Robust%20Gaussian%20Splatting%20In-the-Wild%22&type=repositories))
- **WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.37816) · **Code pending** ([search](https://github.com/search?q=%22WINGS%3A%20Reference-Free%20Gaussian%20Splatting%20Inpainting%20with%203D-Native%20Generative%20Priors%22&type=repositories))
- **X-Splat: Unified Gaussian Splatting for Joint RGB and X-ray 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.23237) · **Code pending** ([search](https://github.com/search?q=%22X-Splat%3A%20Unified%20Gaussian%20Splatting%20for%20Joint%20RGB%20and%20X-ray%203D%20Reconstruction%22&type=repositories))
- **YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2511.07321) · [Code](https://botaoye.github.io/yonosplat/)
- **ZipSplat: Fewer Gaussians, Better Splats** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2606.05102) · [Code](https://github.com/cvg/ZipSplat)
- **AnySplat: Feed-forward 3D Gaussian Splatting from Unconstrained Views** — *SIGGRAPH Asia 2025* · [Paper](https://arxiv.org/abs/2505.23716) · [Code](https://github.com/InternRobotics/AnySplat)
- **No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images** — *ICLR 2025* · [Paper](https://arxiv.org/abs/2410.24207) · [Code](https://github.com/cvg/NoPoSplat)
- **SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2411.12592) · [Code](https://github.com/snldmt/SPARS3R)
- **MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images** — *ECCV 2024* · [Paper](https://arxiv.org/abs/2403.14627) · [Code](https://github.com/donydchen/mvsplat)
- **pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction** — *CVPR 2024* · 🏆 [CVPR 2024 Best Paper Honorable Mention](https://tc.computer.org/tcpami/awards/cvpr-paper-awards/) · [Paper](https://arxiv.org/abs/2312.12337) · [Code](https://github.com/dcharatan/pixelsplat)
- **PreF3R: Pose-Free Feed-Forward 3D Gaussian Splatting from Variable-length Image Sequence** — *arXiv 2024* · [Paper](https://arxiv.org/abs/2411.16877) · [Code](https://computationalrobotics.seas.harvard.edu/PreF3R)
- **Splatt3R: Zero-shot Gaussian Splatting from Uncalibrated Image Pairs** — *arXiv 2024* · [Paper](https://arxiv.org/abs/2408.13912) · [Code](https://github.com/btsmart/splatt3r)
- **3D Gaussian Splatting for Real-Time Radiance Field Rendering** — *arXiv 2023* · 🏆 [SIGGRAPH 2023 Best Paper](https://blog.siggraph.org/2025/03/a-path-to-smarter-more-effective-designs.html/) · [Paper](https://arxiv.org/abs/2308.04079) · [Code](https://github.com/graphdeco-inria/gaussian-splatting)

## Dynamic & 4D Reconstruction

- **4DAnyone: Create Anyone in 4D from a Casual Monocular Video** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.20335) · [Code](https://4danyone.github.io)
- **4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.25956) · **Code pending** ([search](https://github.com/search?q=%224DGS-WAM%3A%20Bridging%20Past%20and%20Future%20with%20an%20Object-Centric%20World%20Action%20Model%20based%20on%204D%20Gaussian%20Splatting%22&type=repositories))
- **4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.17625) · **Code pending** ([search](https://github.com/search?q=%224LC%3A%204D%20Latent%20Cache%20for%20Efficient%20Conditioning%20in%20Dynamic%20World%20Modeling%22&type=repositories))
- **ACA-GS: Adaptive-Capacity Anchored Gaussian Splatting for Compact Dynamic Radiance Fields** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.04581) · **Code pending** ([search](https://github.com/search?q=%22ACA-GS%3A%20Adaptive-Capacity%20Anchored%20Gaussian%20Splatting%20for%20Compact%20Dynamic%20Radiance%20Fields%22&type=repositories))
- **ARROW: Arbitrary Reconstruction and Tracking of 4D Observations in the Wild** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01314) · **Code pending** ([search](https://github.com/search?q=%22ARROW%3A%20Arbitrary%20Reconstruction%20and%20Tracking%20of%204D%20Observations%20in%20the%20Wild%22&type=repositories))
- **D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.01588) · **Code pending** ([search](https://github.com/search?q=%22D%5E2-4DGS%3A%20Dual-Depth%20Guided%20Sparse-Camera%204D%20Gaussian%20Splatting%22&type=repositories))
- **Depth Anything V4: Dynamic 4D Scene Reconstruction via Riemannian Flow Matching on 4D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.18388) · **Code pending** ([search](https://github.com/search?q=%22Depth%20Anything%20V4%3A%20Dynamic%204D%20Scene%20Reconstruction%20via%20Riemannian%20Flow%20Matching%20on%204D%20Gaussian%20Splatting%22&type=repositories))
- **DynActiveGS: Active Gaussian Splatting for Dynamic Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.01178) · **Code pending** ([search](https://github.com/search?q=%22DynActiveGS%3A%20Active%20Gaussian%20Splatting%20for%20Dynamic%20Scene%20Reconstruction%22&type=repositories))
- **DyRAD: Radar Novel View Synthesis for Dynamic Driving Scenes** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.39841) · [Code](https://github.com/Dyrad-NVS/DyRAD)
- **Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2605.14629) · **Code pending** ([search](https://github.com/search?q=%22Efficient%20Dense%20Matching%20for%20Enhanced%20Gaussian%20Splatting%20Using%20AV1%20Motion%20Vectors%22&type=repositories))
- **Efficiently Reconstructing Dynamic Scenes One D4RT at a Time** — *CVPR 2026* · 🏆 [CVPR 2026 Best Paper](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) · [Paper](https://arxiv.org/abs/2512.08924) · [Code](https://d4rt-paper.github.io/)
- **ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.08531) · [Code](https://github.com/andrewbxy/ERF-GS)
- **EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.00994) · **Code pending** ([search](https://github.com/search?q=%22EvoGS%3A%20Modeling%20Deformation%20Evolution%20for%20Dynamic%20Gaussian%20Splatting%22&type=repositories))
- **FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.01958) · **Code pending** ([search](https://github.com/search?q=%22FAST-GS%3A%20Frequency%20Aware%20Space-time%20Gaussian%20Splatting%20for%20Photorealistic%20Dynamic%20Novel%20View%20Synthesis%22&type=repositories))
- **GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2607.21448) · **Code pending** ([search](https://github.com/search?q=%22GrainGS%3A%20Gradient-Decoupled%20Gaussian%20Splatting%20for%20Efficient%20Dynamic%20Novel%20View%20Synthesis%22&type=repositories))
- **HiSfM: Disambiguating Structure-from-Motion via Scaffold-Anchored Hierarchical Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.04718) · [Code](https://github.com/3dv-casia/HiSfM)
- **LagrangeGS: Non-Conservative Lagrangian System on Dynamic 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.22773) · **Code pending** ([search](https://github.com/search?q=%22LagrangeGS%3A%20Non-Conservative%20Lagrangian%20System%20on%20Dynamic%203D%20Gaussian%20Splatting%22&type=repositories))
- **Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.09613) · **Code pending** ([search](https://github.com/search?q=%22Marrying%20Optimal%20Transport%20and%20ODEs%20for%20Unified%20Continuous-Time%204D%20Reconstruction%20and%20Tracking%22&type=repositories))
- **Motion- and Gravity-Aware Feedforward 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.22177) · **Code pending** ([search](https://github.com/search?q=%22Motion-%20and%20Gravity-Aware%20Feedforward%203D%20Reconstruction%22&type=repositories))
- **NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.22888) · [Code](https://nemosplat.hkustvgd.com)
- **PUGS: Physics-Guided Uncertainty Modeling for Underwater Dynamic 3D Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.17936) · **Code pending** ([search](https://github.com/search?q=%22PUGS%3A%20Physics-Guided%20Uncertainty%20Modeling%20for%20Underwater%20Dynamic%203D%20Gaussian%20Splatting%22&type=repositories))
- **QuARC-GS: Quantized Anchored Residual Coding for Compact Dynamic Scene Streaming with Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.18285) · **Code pending** ([search](https://github.com/search?q=%22QuARC-GS%3A%20Quantized%20Anchored%20Residual%20Coding%20for%20Compact%20Dynamic%20Scene%20Streaming%20with%20Gaussian%20Splatting%22&type=repositories))
- **Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.39960) · [Code](https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction)
- **Sparse Light Field Sampling Improves Casual 3D and 4D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.20602) · **Code pending** ([search](https://github.com/search?q=%22Sparse%20Light%20Field%20Sampling%20Improves%20Casual%203D%20and%204D%20Reconstruction%22&type=repositories))
- **Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.19556) · [Code](https://banyuanhao.github.io/Stream4D/)
- **StreamVGGT: Streaming 4D Visual Geometry Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2507.11539) · [Code](https://github.com/wzzheng/StreamVGGT)
- **VidMap: Exploiting Temporal Structure for Video-Based Structure-from-Motion** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2607.27194) · **Code pending** ([search](https://github.com/search?q=%22VidMap%3A%20Exploiting%20Temporal%20Structure%20for%20Video-Based%20Structure-from-Motion%22&type=repositories))
- **Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction** — *ICCV 2025* · 🏆 [ICCV 2025 Highlight](https://iccv.thecvf.com/virtual/2025/poster/2494) · [Paper](https://arxiv.org/abs/2504.07961) · [Code](https://github.com/jzr99/Geo4D)
- **MegaSaM: Accurate, Fast, and Robust Structure and Motion from Casual Dynamic Videos** — *CVPR 2025* · 🏆 [CVPR 2025 Best Paper Honorable Mention](https://cvpr.thecvf.com/Conferences/2025/News/Awards_Press) · [Paper](https://arxiv.org/abs/2412.04463) · [Code](https://mega-sam.github.io/)
- **MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion** — *ICLR 2025* · [Paper](https://arxiv.org/abs/2410.03825) · [Code](https://github.com/Junyi42/monst3r)
- **VGGT4D: Mining Motion Cues in Visual Geometry Transformers for 4D Scene Reconstruction** — *arXiv 2025* · [Paper](https://arxiv.org/abs/2511.19971) · [Code](https://3dagentworld.github.io/vggt4d)
- **ViPE: Video Pose Engine for Geometric 3D Perception** — *arXiv 2025* · [Paper](https://research.nvidia.com/labs/toronto-ai/vipe/assets/paper.pdf) · [Code](https://github.com/nv-tlabs/vipe)
- **4D Gaussian Splatting for Real-Time Dynamic Scene Rendering** — *CVPR 2024* · [Paper](https://arxiv.org/abs/2310.08528) · [Code](https://github.com/hustvl/4DGaussians)
- **Driv3R: Learning Dense 4D Reconstruction for Autonomous Driving** — *arXiv 2024* · [Paper](https://arxiv.org/abs/2412.06777) · [Code](https://github.com/Barrybarry-Smith/Driv3R)
- **K-Planes: Explicit Radiance Fields in Space, Time, and Appearance** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2301.10241) · [Code](https://github.com/sarafridov/K-Planes)
- **D-NeRF: Neural Radiance Fields for Dynamic Scenes** — *CVPR 2021* · [Paper](https://arxiv.org/abs/2011.13961) · [Code](https://github.com/albertpumarola/D-NeRF)
- **Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes** — *CVPR 2021* · [Paper](https://arxiv.org/abs/2011.13084) · [Code](https://github.com/zhengqili/Neural-Scene-Flow-Fields)

## Object, Human & 3D Generation

- **Cloth-HUGS: Cloth Aware Human Gaussian Splatting** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2604.15875) · **Code pending** ([search](https://github.com/search?q=%22Cloth-HUGS%3A%20Cloth%20Aware%20Human%20Gaussian%20Splatting%22&type=repositories))
- **DiGS-Avatar: Single-Image Animatable 3D Human Reconstruction via UV-Space Diffusion** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.20759) · [Code](https://github.com/KLMAV-CUC/DiGS-Avatar)
- **Edit4D: Editable 4D Scene Generation with Textual Control** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.21668) · [Code](https://chanwo0kim.github.io/Edit4D/)
- **EgoGVAE: Ego-body Mesh Reconstruction via Guided Variational Autoencoder** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2607.27755) · **Code pending** ([search](https://github.com/search?q=%22EgoGVAE%3A%20Ego-body%20Mesh%20Reconstruction%20via%20Guided%20Variational%20Autoencoder%22&type=repositories))
- **ElasticGS: Pose-Aware Dynamic Gaussian Adaptation for Geometry-Consistent Human Digital Twin Reconstruction from Monocular Video** — *arXiv 2026* · [Paper](https://doi.org/10.20944/preprints202608.1929.v1) · **Code pending** ([search](https://github.com/search?q=%22ElasticGS%3A%20Pose-Aware%20Dynamic%20Gaussian%20Adaptation%20for%20Geometry-Consistent%20Human%20Digital%20Twin%20Reconstruction%20from%20Monocular%20Video%22&type=repositories))
- **GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17988) · **Code pending** ([search](https://github.com/search?q=%22GS-Voxel%3A%20Fitting-Free%20Structured%20Latents%20for%20Large-Scale%203DGS%20Generation%22&type=repositories))
- **Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.23206) · **Code pending** ([search](https://github.com/search?q=%22Learning%20Spherical%20Occupancy%20Profiles%20for%20Multi-View%203D%20Reconstruction%20and%20Generation%22&type=repositories))
- **Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.22757) · **Code pending** ([search](https://github.com/search?q=%22Object-Uni%3A%20A%20Unified%20Model%20for%20Object-Centric%20Spatial%20Understanding%20and%20Controllable%20Generation%22&type=repositories))
- **OmniMech: All-in-one Multimodal Mechanical Benchmark for 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.05539) · **Code pending** ([search](https://github.com/search?q=%22OmniMech%3A%20All-in-one%20Multimodal%20Mechanical%20Benchmark%20for%203D%20Reconstruction%22&type=repositories))
- **Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.23410) · **Code pending** ([search](https://github.com/search?q=%22Photorealistic%20Novel%20View%20Synthesis%20of%20Human%20Faces%20using%20Next-Scale%20Transformers%22&type=repositories))
- **PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2607.05373) · [Code](https://github.com/SensenGao/PixWorld)
- **ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2510.23306) · [Code](https://github.com/GAP-LAB-CUHK-SZ/ReconViaGen)
- **Repurposing Geometric Foundation Models for Multi-view Diffusion** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.22275) · [Code](https://github.com/cvlab-kaist/GLD)
- **ReX-Shot: Single-Image Rephotography via Geometry- and Camera-Grounded Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.18593) · **Code pending** ([search](https://github.com/search?q=%22ReX-Shot%3A%20Single-Image%20Rephotography%20via%20Geometry-%20and%20Camera-Grounded%20Generation%22&type=repositories))
- **RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.02847) · [Code](https://jerry-locker.github.io/roge/)
- **S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2607.28164) · **Code pending** ([search](https://github.com/search?q=%22S-Avatar%3A%20Diffusion-Guided%20Gaussian%20Head%20Avatars%20from%20a%20Single%20Image%22&type=repositories))
- **Scanline-Aware Animatable Gaussian Avatars from Rolling-Shutter Videos** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17314) · **Code pending** ([search](https://github.com/search?q=%22Scanline-Aware%20Animatable%20Gaussian%20Avatars%20from%20Rolling-Shutter%20Videos%22&type=repositories))
- **Source-Face Authenticity Detection for 3D Gaussian Heads Reconstructed from a Single Portrait: A Benchmark and Dedicated Detector** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.23984) · **Code pending** ([search](https://github.com/search?q=%22Source-Face%20Authenticity%20Detection%20for%203D%20Gaussian%20Heads%20Reconstructed%20from%20a%20Single%20Portrait%3A%20A%20Benchmark%20and%20Dedicated%20Detector%22&type=repositories))
- **Sparse auto-regressive modeling for scene generation from multi-view images** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.03931) · **Code pending** ([search](https://github.com/search?q=%22Sparse%20auto-regressive%20modeling%20for%20scene%20generation%20from%20multi-view%20images%22&type=repositories))
- **Stepper: Stepwise Immersive Scene Generation with Multiview Panorama** — *CVPRF 2026* · [Paper](https://arxiv.org/abs/2603.28980) · [Code](https://fwmb.github.io/stepper/)
- **Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.00610) · **Code pending** ([search](https://github.com/search?q=%22Streaming4D%3A%20Accelerate%204D%20World%20Models%20via%20Block-wise%20Video%20Generation%20and%20Incremental%20Reconstruction%22&type=repositories))
- **VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.26599) · [Code](https://zhaochongan.github.io/projects/VGGRPO/)
- **View-Adaptive Renderer for View-Consistent 2D-to-3D Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.09110) · **Code pending** ([search](https://github.com/search?q=%22View-Adaptive%20Renderer%20for%20View-Consistent%202D-to-3D%20Generation%22&type=repositories))
- **VisTa3D: A Dataset and Benchmark for Thin Object Reconstruction from Vision, Tactile, and 3D Point Clouds** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.20740) · [Code](https://huggingface.co/datasets/shaniaguo/VisTa3D)
- **When Does An Extra View Help? Adapting Single-View 3D Reconstruction with Extra Imagery** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.08132) · [Code](https://github.com/YNhuHuynh/ASV3D/tree/main)
- **Gamba: Marry Gaussian Splatting With Mamba for Single-View 3D Reconstruction** — *TPAMI 2025* · [Paper](https://arxiv.org/abs/2403.18795) · [Code](https://github.com/SkyworkAI/Gamba)
- **UniRecGen: Unifying Multi-View 3D Reconstruction and Generation** — *arXiv 2025* · [Paper](https://arxiv.org/abs/2604.01479) · [Code](https://github.com/zsh523/UniRecGen)
- **BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2303.14158) · [Code](https://github.com/NVlabs/BundleSDF)
- **ECON: Explicit Clothed Humans Optimized via Normal Integration** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2212.07422) · [Code](https://github.com/YuliangXiu/ECON)
- **Multiview Compressive Coding for 3D Reconstruction** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2301.08247) · [Code](https://github.com/facebookresearch/MCC)
- **SparseFusion: Distilling View-Conditioned Diffusion for 3D Reconstruction** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2212.00792) · [Code](https://github.com/zhizdev/sparsefusion)
- **ICON: Implicit Clothed humans Obtained from Normals** — *CVPR 2022* · [Paper](https://arxiv.org/abs/2112.09127) · [Code](https://github.com/YuliangXiu/ICON)

## Semantic 3D Reconstruction

- **3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.16292) · **Code pending** ([search](https://github.com/search?q=%223D%20Gaussian%20Splatting%20for%20Fine-grained%20Urban%20Scene%20Reconstruction%20via%20Semantic-guided%20Density%20Control%20and%20Loss%20Design%22&type=repositories))
- **EPS3D : End-to-End Feed-Forward 3D Panoptic Segmentation** — *ICML 2026* · [Paper](https://arxiv.org/abs/2606.08980) · [Code](https://github.com/Runsong123/EPS3D)
- **IGGT: Instance-Grounded Geometry Transformer for Semantic 3D Reconstruction** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2510.22706) · [Code](https://github.com/lifuguan/IGGT_official)
- **InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene Understanding** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.07144) · [Code](https://github.com/JamChaos/InsSplat)
- **ManifoldSplat: Language-Guided Semantic Shape Editing of 3D Gaussian Head Avatars** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.03599) · [Code](https://a-canela.github.io/manifoldsplat/)
- **Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.13143) · **Code pending** ([search](https://github.com/search?q=%22Measurable%20Semantic%203D%20Gaussian%20Splatting%20with%20Joint%20Region%20and%20Depth%20Supervision%20for%20Interactive%20Building%20Inspection%22&type=repositories))
- **Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.22740) · **Code pending** ([search](https://github.com/search?q=%22Seeing%20the%20Unseen%3A%20Semantic-in-Gaussian%20for%20Sparse-View%203D%20Generalization%22&type=repositories))
- **SegVGGT: Joint 3D Reconstruction and InstanceSegmentation from Multi-View Images** — *ECCV 2026* · [Paper](https://arxiv.org/abs/2603.19926) · [Code](https://github.com/IDEA-Research/SegVGGT)
- **SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.31023) · [Code](https://smg-gaussian.github.io/)
- **SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.17420) · [Code](https://github.com/Li00147/SPVC)
- **Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2508.03643) · [Code](https://github.com/HorizonRobotics/Uni3R)
- **VGGT-Segmentor: Geometry-Enhanced Cross-View Segmentation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.13596) · **Code pending** ([search](https://github.com/search?q=%22VGGT-Segmentor%3A%20Geometry-Enhanced%20Cross-View%20Segmentation%22&type=repositories))
- **Vision3D: A Full-Stack Framework for Monocular Single-Image 3D Scene Reconstruction with Depth– Object Semantic Fusion** — *arXiv 2026* · [Paper](https://doi.org/10.5281/zenodo.22277718) · **Code pending** ([search](https://github.com/search?q=%22Vision3D%3A%20A%20Full-Stack%20Framework%20for%20Monocular%20Single-Image%203D%20Scene%20Reconstruction%20with%20Depth%E2%80%93%20Object%20Semantic%20Fusion%22&type=repositories))
- **WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.11100) · **Code pending** ([search](https://github.com/search?q=%22WildFireGS%3A%20Physics-Based%20Wildfire%20Simulation%20in%20Large-Scale%20Semantics-Enriched%20Gaussian%20Splatting%20Forest%20Scenes%22&type=repositories))
- **PanSt3R: Multi-view Consistent Panoptic Segmentation** — *ICCV 2025* · [Paper](https://arxiv.org/abs/2506.21348) · [Code](https://github.com/naver/panst3r)

## SLAM, Robotics & Mapping

- **2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.11752) · **Code pending** ([search](https://github.com/search?q=%222DGS-Planner%3A%20Rasterization-based%20Path%20Planning%20in%202D%20Gaussian%20Splatting%20Map%22&type=repositories))
- **Benchmarking 3D Reconstruction for Under-Ice Robotic Perception in Arctic Environments** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.19097) · **Code pending** ([search](https://github.com/search?q=%22Benchmarking%203D%20Reconstruction%20for%20Under-Ice%20Robotic%20Perception%20in%20Arctic%20Environments%22&type=repositories))
- **CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.26868) · **Code pending** ([search](https://github.com/search?q=%22CGS-SLAM%3A%20Collaborative%20Gaussian%20Splatting%20based%20SLAM%20for%20Multi-Agent%20Reconstruction%22&type=repositories))
- **EndoMD-SLAM: Endoscopic Gaussian Splatting SLAM under Optical Degradation with Memory and Static-Transient Decomposition** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.08949) · [Code](https://github.com/phai-lab/EndoMD-SLAM)
- **Gaussian-LIC2: LiDAR-Inertial-Camera Gaussian Splatting SLAM** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2507.04004) · [Code](https://github.com/APRIL-ZJU/Gaussian-LIC)
- **Geometry-Aware Online Mapping for 3D Gaussian Splatting SLAM** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.14902) · **Code pending** ([search](https://github.com/search?q=%22Geometry-Aware%20Online%20Mapping%20for%203D%20Gaussian%20Splatting%20SLAM%22&type=repositories))
- **HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.19742) · **Code pending** ([search](https://github.com/search?q=%22HyperLoop%3A%20Hyperspectral-Assisted%20Loop%20Closure%20Detection%20in%203D-SLAM%20for%20Planetary%20Exploration%22&type=repositories))
- **KFS$^4$LAM: Adaptive KeyFrame Selection with Structure-Aware Mapping for Endoscopic Gaussian Splatting SLAM** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.22505) · [Code](https://xinweiju.github.io/KFSLAM/)
- **LatentAM: Real-Time, Large-Scale Latent Gaussian Attention Mapping via Online Dictionary Learning** — *RA-L 2026* · [Paper](https://doi.org/10.48550/arxiv.2602.12314) · [Code](https://github.com/UMich-SSI-Lab/latentam)
- **LingBot-Map: Geometric Context Transformer for Streaming 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.14141) · [Code](https://github.com/robbyant/lingbot-map)
- **Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.12179) · [Code](https://royyang0714.github.io/Map-Det3D)
- **Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.00731) · **Code pending** ([search](https://github.com/search?q=%22Measuring%20Asset%20and%20Scene%20Reconstruction%20Effects%20in%20Real-to-Sim%20Robot%20Evaluation%22&type=repositories))
- **Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.09146) · **Code pending** ([search](https://github.com/search?q=%22Multi-Submap%20Implicit%20Neural%20SLAM%20with%20Local-to-Global%20Loop%20Closure%20for%20Large-Scale%20Scene%20Reconstruction%22&type=repositories))
- **Pow3R-SLAM: Real-Time RGB-D SLAM with 3D Reconstruction Priors** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2609.38054) · [Code](https://ChrisKolios.github.io/Pow3R-SLAM)
- **Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.01206) · **Code pending** ([search](https://github.com/search?q=%22Resolving%20Mixed%20Single-Photon%20LiDAR%20Returns%20for%20Foreground-View%20and%20Hidden%20Scene%20Reconstruction%22&type=repositories))
- **SLAMFormer-$\infty$: Infinite SLAM Transformer for Unbounded Frontend and Backend Processing** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.03429) · [Code](https://github.com/Tsinghua-MARS-Lab/SLAMFormer-Infinity)
- **SpotlessGS: Relightable 3D Gaussian Splatting under Dynamic Illumination for Robotic Perception** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2608.14713) · **Code pending** ([search](https://github.com/search?q=%22SpotlessGS%3A%20Relightable%203D%20Gaussian%20Splatting%20under%20Dynamic%20Illumination%20for%20Robotic%20Perception%22&type=repositories))
- **TCGSplat: Temporal Confidence Guided 3D Gaussian Splatting for RGB-D SLAM** — *arXiv 2026* · [Paper](https://doi.org/10.21203/rs.3.rs-10579135/v1) · **Code pending** ([search](https://github.com/search?q=%22TCGSplat%3A%20Temporal%20Confidence%20Guided%203D%20Gaussian%20Splatting%20for%20RGB-D%20SLAM%22&type=repositories))
- **Training-Free Target-Aware Refinement of 3D Gaussian Language Map** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2610.21619) · [Code](https://lab-of-ai-and-robotics.github.io/target-aware-langmap/)
- **ZipMap: Linear-Time Stateful 3D Reconstruction via Test-Time Training** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.04385) · [Code](https://github.com/Haian-Jin/ZipMap)
- **SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2412.09401) · [Code](https://github.com/PKU-VCL-3DV/SLAM3R)
- **Gaussian-SLAM: Photo-realistic Dense SLAM with Gaussian Splatting** — *CVPR 2024* · [Paper](https://arxiv.org/abs/2312.10070) · [Code](https://github.com/VladimirYugay/Gaussian-SLAM)
- **MoD-SLAM: Monocular Dense Mapping for Unbounded 3D Scene Reconstruction** — *RA-L 2024* · [Paper](https://arxiv.org/abs/2402.03762) · **Code pending** ([search](https://github.com/search?q=%22MoD-SLAM%3A%20Monocular%20Dense%20Mapping%20for%20Unbounded%203D%20Scene%20Reconstruction%22&type=repositories))
- **MonoGS: Gaussian Splatting SLAM from Monocular Videos** — *CVPR 2024* · [Paper](https://arxiv.org/abs/2312.06741) · [Code](https://github.com/muskie82/MonoGS)
- **NICER-SLAM: Neural Implicit Scene Encoding for RGB SLAM** — *3DV 2024* · 🏆 [3DV 2024 Best Paper Honorable Mention](https://nicer-slam.github.io/) · [Paper](https://arxiv.org/abs/2302.03594) · [Code](https://github.com/cvg/nicer-slam)
- **SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM** — *CVPR 2024* · [Paper](https://arxiv.org/abs/2312.02126) · [Code](https://github.com/spla-tam/SplaTAM)
- **A Multirobot System for 3-D Surface Reconstruction With Centralized and Distributed Architectures** — *TRO 2023* · [Paper](https://doi.org/10.1109/TRO.2023.3258641) · **Code pending** ([search](https://github.com/search?q=%22A%20Multirobot%20System%20for%203-D%20Surface%20Reconstruction%20With%20Centralized%20and%20Distributed%20Architectures%22&type=repositories))
- **GO-SLAM: Global Optimization for Consistent 3D Instant Reconstruction** — *ICCV 2023* · [Paper](https://arxiv.org/abs/2309.02436) · [Code](https://github.com/youmi-zym/GO-SLAM)
- **NeurAR: Neural Uncertainty for Autonomous 3D Reconstruction With Implicit Neural Representations** — *RA-L 2023* · [Paper](https://doi.org/10.1109/LRA.2023.3235686) · **Code pending** ([search](https://github.com/search?q=%22NeurAR%3A%20Neural%20Uncertainty%20for%20Autonomous%203D%20Reconstruction%20With%20Implicit%20Neural%20Representations%22&type=repositories))
- **SHINE-Mapping: Large-Scale 3D Mapping Using Sparse Hierarchical Implicit Neural Representations** — *ICRA 2023* · [Paper](https://arxiv.org/abs/2210.02299) · [Code](https://github.com/PRBonn/SHINE_mapping)
- **Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems** — *TRO 2022* · 🏆 [IEEE T-RO King-Sun Fu Memorial Best Paper Award](https://www.ieee-ras.org/awards-recognition/publications-awards/ieee-transactions-on-robotics-king-sun-fu-memorial-best-paper-award/) · [Paper](https://arxiv.org/abs/2106.14386) · [Code](https://github.com/MIT-SPARK/Kimera-Multi)
- **Poisson Surface Reconstruction for LiDAR Odometry and Mapping** — *ICRA 2021* · [Paper](https://doi.org/10.1109/ICRA48506.2021.9562069) · **Code pending** ([search](https://github.com/search?q=%22Poisson%20Surface%20Reconstruction%20for%20LiDAR%20Odometry%20and%20Mapping%22&type=repositories))

## Automatic updates

A scheduled GitHub Action runs every Monday. It first synchronizes the reference repository, checks the latest arXiv submissions directly, then queries OpenAlex for additional papers published since 2021, deduplicates records, searches GitHub for likely official implementations, applies the taxonomy, preserves curated honors, and regenerates this README and the visual timeline. The workflow can also be run manually from the Actions tab.

To run locally:

```bash
python scripts/update_papers.py --render-only
python scripts/update_papers.py --dry-run
python scripts/update_papers.py
```

Set `GITHUB_TOKEN` to enable code-repository discovery and optionally set `OPENALEX_EMAIL` for the OpenAlex polite pool.

## Contributing

Corrections and missing papers are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and open a pull request or issue.

## Acknowledgements

This repository mirrors 98 entries and their original categories from [End-to-End-3D-Reconstruction-Paper-List](https://github.com/chicleee/End-to-End-3D-Reconstruction-Paper-List). Metadata discovery for additional papers uses the [arXiv API](https://info.arxiv.org/help/api/) and [OpenAlex](https://openalex.org/).

## License

MIT
