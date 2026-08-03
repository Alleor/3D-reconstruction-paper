# Awesome 3D Reconstruction Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Auto Update](https://github.com/Alleor/3D-reconstruction-paper/actions/workflows/update-papers.yml/badge.svg)](https://github.com/Alleor/3D-reconstruction-paper/actions/workflows/update-papers.yml)
![Papers](https://img.shields.io/badge/papers-131-blue)

A curated, automatically updated list of recent papers on 3D reconstruction.
收录 2021 年至今的三维重建论文，并自动发现新论文及其开源代码。

> Coverage: 2021–Present · Last content update: 2026-08-03 · Maintainer: [@Alleor](https://github.com/Alleor)

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
| [Feed-Forward Geometry & Foundation Models](#feed-forward-geometry--foundation-models) | General-purpose visual geometry, camera/point prediction, SfM, and feed-forward reconstruction foundation models. | 43 |
| [Dense Depth, Surface & Mesh Reconstruction](#dense-depth-surface--mesh-reconstruction) | Methods whose primary output is dense depth, a mesh, TSDF/SDF, planes, or multi-view-stereo surface geometry. | 8 |
| [NeRF & Novel View Synthesis](#nerf--novel-view-synthesis) | Neural radiance fields and non-Gaussian novel/free-view synthesis. | 17 |
| [Gaussian Splatting](#gaussian-splatting) | Static-scene or generalizable reconstruction whose primary representation is Gaussian splatting. | 18 |
| [Dynamic & 4D Reconstruction](#dynamic--4d-reconstruction) | Time-varying scenes, motion-aware geometry, scene flow, and 4D rendering. | 13 |
| [Object, Human & 3D Generation](#object-human--3d-generation) | Object-centric reconstruction, humans/avatars, and explicit 3D or scene generation. | 12 |
| [Semantic 3D Reconstruction](#semantic-3d-reconstruction) | Joint geometry with semantic, instance, or panoptic understanding. | 6 |
| [SLAM, Robotics & Mapping](#slam-robotics--mapping) | SLAM, odometry, robotic reconstruction, and local or large-scale mapping. | 14 |

## Venue coverage

| Venue | Papers |
|:--|--:|
| CVPR | 51 |
| ICCV | 7 |
| ECCV | 4 |
| TPAMI | 3 |
| IROS | 1 |
| ICRA | 2 |
| TRO | 2 |
| RA-L | 2 |
| ICLR | 15 |
| 3DV | 4 |
| arXiv | 34 |
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

- **AMB3R: Accurate Feed-forward Metric-scale 3D Reconstruction with Backend** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2511.20343) · [Code](https://github.com/HengyiWang/amb3r)
- **DAGE: Dual-Stream Architecture for Efficient and Fine-Grained Geometry Estimation** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.03744) · [Code](https://github.com/ngoductuanlhp/DAGE)
- **Depth Anything 3: Recovering the Visual Space from Any Views** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2511.10647) · [Code](https://depth-anything-3.github.io/)
- **Déjà View: Looping Transformers for Multi-View 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2605.30215) · [Code](https://github.com/nv-tlabs/dvlt)
- **Faster VGGT with Block-Sparse Global Attention** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2509.07120) · [Code](https://github.com/brianwang00001/sparse-vggt)
- **FastVGGT: Training-Free Acceleration of Visual Geometry Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2509.02560) · [Code](https://github.com/mystorm16/FastVGGT)
- **FF3R: Feedforward Feature 3D Reconstruction from Unconstrained views** — *CVPRF 2026* · [Paper](https://arxiv.org/abs/2604.09862) · [Code](https://github.com/ChaoyiZh/ff3r)
- **From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.27455) · [Code](https://ranrhuang.github.io/nas3r/)
- **GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2605.23888) · [Code](https://kasothaphie.github.io/GenRecon/)
- **HD-VGGT: High-Resolution Visual Geometry Transformer** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.27222) · **Code pending** ([search](https://github.com/search?q=%22HD-VGGT%3A%20High-Resolution%20Visual%20Geometry%20Transformer%22&type=repositories))
- **LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.03269) · [Code](https://github.com/Junyi42/LoGeR)
- **MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos** — *arXiv 2026* · [Paper](https://arxiv.org/pdf/2607.15211) · **Code pending** ([search](https://github.com/search?q=%22MAGiSt3R%3A%20Multi-Agent%20Feed-forward%203D%20Reconstruction%20from%20Monocular%20RGB%20Videos%22&type=repositories))
- **MapAnything: Universal Feed-Forward Metric 3D Reconstruction** — *3DV 2026* · [Paper](https://arxiv.org/abs/2509.13414) · [Code](https://github.com/facebookresearch/map-anything)
- **MERG3R: A Divide-and-Conquer Approach to Large-Scale Neural Visual Geometry** — *CVPR 2026* · [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_MERG3R_A_Divide-and-Conquer_Approach_to_Large-Scale_Neural_Visual_Geometry_CVPR_2026_paper.pdf) · [Code](https://github.com/LeoChengKX/MERG3R)
- **NOVA3R: Non-pixel-aligned Visual Transformer for Amodal 3D Reconstruction** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2603.04179) · [Code](https://wrchen530.github.io/nova3r/)
- **Offline Feed-Forward 3D Reconstruction at Scale** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2602.23361) · **Code pending** ([search](https://github.com/search?q=%22Offline%20Feed-Forward%203D%20Reconstruction%20at%20Scale%22&type=repositories))
- **OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2511.10560) · [Code](https://livioni.github.io/OmniVGGT-official/)
- **PE3R: Perception-Efficient 3D Reconstruction** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2503.07507) · [Code](https://github.com/hujiecpp/pe3r)
- **Quantized Visual Geometry Grounded Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2509.21302) · [Code](https://github.com/wlfeng0509/QuantVGGT)
- **Reliev3R: Relieving Feed-forward 3D Reconstruction from Multi-View Geometric Annotations** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.00548) · **Code pending** ([search](https://github.com/search?q=%22Reliev3R%3A%20Relieving%20Feed-forward%203D%20Reconstruction%20from%20Multi-View%20Geometric%20Annotations%22&type=repositories))
- **S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models** — *ICME 2026* · [Paper](https://arxiv.org/abs/2603.17625) · [Code](https://github.com/Powertony102/S-VGGT)
- **SAIL-Recon: Large SfM by Augmenting Scene Regression with Localization** — *3DV 2026* · [Paper](https://arxiv.org/abs/2508.17972) · [Code](https://hkust-sail.github.io/sail-recon)
- **Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2604.08542) · [Code](https://zju3dv.github.io/scal3r/)
- **STream3R: Scalable Sequential 3D Reconstruction with Causal Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2508.10893) · [Code](https://github.com/NIRVANALAN/STream3R)
- **Surflo: Consistent 3D Surface Flow Model with Global State** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2606.13644) · [Code](https://anttwo.github.io/surflo/)
- **TTT3R: 3D Reconstruction as Test-Time Training** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2509.26645) · [Code](https://rover-xingyu.github.io/TTT3R/)
- **UniQueR: Unified Query-based Feedforward 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.22851) · **Code pending** ([search](https://github.com/search?q=%22UniQueR%3A%20Unified%20Query-based%20Feedforward%203D%20Reconstruction%22&type=repositories))
- **Unlocking the Power of Critical Factors for 3D Visual Geometry Estimation** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2604.21713) · [Code](https://github.com/aim-uofa/CARVE)
- **VGGT-Ω** — *CVPR 2026* · [Paper](https://vggt-omega.github.io/assets/paper/preview_v3.pdf) · [Code](https://github.com/facebookresearch/vggt-omega)
- **π³: Scalable Permutation-Equivariant Visual Geometry Learning** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2507.13347) · [Code](https://github.com/yyfz/Pi3)
- **🌐 Argus: Metric Panoramic 3D Reconstruction for Indoor Scenes** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2606.30047) · [Code](https://argus-paper.realsee.ai/)
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

- **MUSt3R: Multi-view Network for Stereo 3D Reconstruction** — *CVPR 2025* · [Paper](https://arxiv.org/abs/2503.01661) · [Code](https://github.com/naver/must3r)
- **MonoPlane: Exploiting Monocular Geometric Cues for Generalizable 3D Plane Reconstruction** — *IROS 2024* · [Paper](https://arxiv.org/abs/2411.01226) · [Code](https://github.com/thuzhaowang/MonoPlane)
- **FineRecon: Depth-aware Feed-forward Network for Detailed 3D Reconstruction** — *ICCV 2023* · [Paper](https://arxiv.org/abs/2304.01480) · [Code](https://github.com/apple/ml-finerecon)
- **Neuralangelo: High-Fidelity Neural Surface Reconstruction** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2306.03092) · [Code](https://github.com/NVlabs/neuralangelo)
- **NOPE-SAC: Neural One-Plane RANSAC for Sparse-View Planar 3D Reconstruction** — *TPAMI 2023* · [Paper](https://arxiv.org/abs/2211.16799) · [Code](https://github.com/IceTTTb/NopeSAC)
- **NeuralWarp: Time-Warping for Neural Surface Reconstruction** — *CVPR 2022* · [Paper](https://arxiv.org/abs/2202.03848) · [Code](https://github.com/fdarmon/NeuralWarp)
- **GigaMVS: A Benchmark for Ultra-Large-Scale Gigapixel-Level 3D Reconstruction** — *TPAMI 2021* · [Paper](https://doi.org/10.1109/TPAMI.2021.3115028) · **Code pending** ([search](https://github.com/search?q=%22GigaMVS%3A%20A%20Benchmark%20for%20Ultra-Large-Scale%20Gigapixel-Level%203D%20Reconstruction%22&type=repositories))
- **NeuralRecon: Real-Time Coherent 3D Reconstruction from Monocular Video** — *CVPR 2021* · [Paper](https://arxiv.org/abs/2104.00681) · [Code](https://github.com/zju3dv/NeuralRecon)

## NeRF & Novel View Synthesis

- **AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.19747) · [Code](https://github.com/OpenImagingLab/AnyRecon)
- **E-RayZer: Self-supervised 3D Reconstruction as Spatial Visual Pre-training** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.10950) · [Code](https://github.com/QitaoZhao/E-RayZer)
- **FreeScale: Scaling 3D scenes via Certainty-Aware Free-View Generation** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2604.10512) · [Code](https://github.com/mvp-ai-lab/FreeScale)
- **From Rays to Projections: Better Inputs for Feed-Forward View Synthesis** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2601.05116) · [Code](https://wuzirui.github.io/pvsm-web/)
- **LagerNVS: Latent Geometry for Fully Neural Real-Time Novel View Synthesis** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.20176) · [Code](https://github.com/facebookresearch/lagernvs)
- **One-Shot Refiner: Boosting Feed-forward Novel View Synthesis via One-Step Diffusion** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2601.14161) · [Code](https://github.com/YitongD/One_Shot_Refiner)
- **UniSHARP: Universal Sharp Monocular View Synthesis** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2606.07514) · [Code](https://github.com/Insta360-Research-Team/UniSHARP)
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

- **C3G: Learning Compact 3D Representations with 2K Gaussians** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.04021) · [Code](https://github.com/cvlab-kaist/C3G)
- **Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.01030) · [Code](https://liu115.github.io/diff3r)
- **EcoSplat: Efficiency-controllable Feed-forward 3D Gaussian Splatting from Multi-view Images** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.18692) · [Code](https://kaist-viclab.github.io/ecosplat-site/)
- **Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2603.25745) · [Code](https://yxlao.github.io/lgtm)
- **Leveling3D: Leveling Up 3D Reconstruction withFeed-Forward 3D Gaussian Splatting andGeometry-Aware Generation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.16211) · **Code pending** ([search](https://github.com/search?q=%22Leveling3D%3A%20Leveling%20Up%203D%20Reconstruction%20withFeed-Forward%203D%20Gaussian%20Splatting%20andGeometry-Aware%20Generation%22&type=repositories))
- **Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2512.15508) · [Code](https://arthurmoreau.github.io/OffTheGrid/)
- **PanoLess: Environment Reconstruction from Partial Reflective Views** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2607.25362) · **Code pending** ([search](https://github.com/search?q=%22PanoLess%3A%20Environment%20Reconstruction%20from%20Partial%20Reflective%20Views%22&type=repositories))
- **Pose-Free Omnidirectional Gaussian Splatting for 360-Degree Videos with Consistent Depth Priors** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2603.23324) · [Code](https://github.com/zcq15/PFGS360)
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

- **Efficiently Reconstructing Dynamic Scenes One D4RT at a Time** — *CVPR 2026* · 🏆 [CVPR 2026 Best Paper](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) · [Paper](https://arxiv.org/abs/2512.08924) · [Code](https://d4rt-paper.github.io/)
- **GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2607.21448) · **Code pending** ([search](https://github.com/search?q=%22GrainGS%3A%20Gradient-Decoupled%20Gaussian%20Splatting%20for%20Efficient%20Dynamic%20Novel%20View%20Synthesis%22&type=repositories))
- **StreamVGGT: Streaming 4D Visual Geometry Transformer** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2507.11539) · [Code](https://github.com/wzzheng/StreamVGGT)
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

- **ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2510.23306) · [Code](https://github.com/GAP-LAB-CUHK-SZ/ReconViaGen)
- **Repurposing Geometric Foundation Models for Multi-view Diffusion** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.22275) · [Code](https://github.com/cvlab-kaist/GLD)
- **S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image** — *arXiv 2026* · [Paper](https://doi.org/10.48550/arxiv.2607.28164) · **Code pending** ([search](https://github.com/search?q=%22S-Avatar%3A%20Diffusion-Guided%20Gaussian%20Head%20Avatars%20from%20a%20Single%20Image%22&type=repositories))
- **Stepper: Stepwise Immersive Scene Generation with Multiview Panorama** — *CVPRF 2026* · [Paper](https://arxiv.org/abs/2603.28980) · [Code](https://fwmb.github.io/stepper/)
- **VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2603.26599) · [Code](https://zhaochongan.github.io/projects/VGGRPO/)
- **Gamba: Marry Gaussian Splatting With Mamba for Single-View 3D Reconstruction** — *TPAMI 2025* · [Paper](https://arxiv.org/abs/2403.18795) · [Code](https://github.com/SkyworkAI/Gamba)
- **UniRecGen: Unifying Multi-View 3D Reconstruction and Generation** — *arXiv 2025* · [Paper](https://arxiv.org/abs/2604.01479) · [Code](https://github.com/zsh523/UniRecGen)
- **BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2303.14158) · [Code](https://github.com/NVlabs/BundleSDF)
- **ECON: Explicit Clothed Humans Optimized via Normal Integration** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2212.07422) · [Code](https://github.com/YuliangXiu/ECON)
- **Multiview Compressive Coding for 3D Reconstruction** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2301.08247) · [Code](https://github.com/facebookresearch/MCC)
- **SparseFusion: Distilling View-Conditioned Diffusion for 3D Reconstruction** — *CVPR 2023* · [Paper](https://arxiv.org/abs/2212.00792) · [Code](https://github.com/zhizdev/sparsefusion)
- **ICON: Implicit Clothed humans Obtained from Normals** — *CVPR 2022* · [Paper](https://arxiv.org/abs/2112.09127) · [Code](https://github.com/YuliangXiu/ICON)

## Semantic 3D Reconstruction

- **EPS3D : End-to-End Feed-Forward 3D Panoptic Segmentation** — *ICML 2026* · [Paper](https://arxiv.org/abs/2606.08980) · [Code](https://github.com/Runsong123/EPS3D)
- **IGGT: Instance-Grounded Geometry Transformer for Semantic 3D Reconstruction** — *ICLR 2026* · [Paper](https://arxiv.org/abs/2510.22706) · [Code](https://github.com/lifuguan/IGGT_official)
- **SegVGGT: Joint 3D Reconstruction and InstanceSegmentation from Multi-View Images** — *ECCV 2026* · [Paper](https://arxiv.org/abs/2603.19926) · [Code](https://github.com/IDEA-Research/SegVGGT)
- **Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images** — *CVPR 2026* · [Paper](https://arxiv.org/abs/2508.03643) · [Code](https://github.com/HorizonRobotics/Uni3R)
- **VGGT-Segmentor: Geometry-Enhanced Cross-View Segmentation** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.13596) · **Code pending** ([search](https://github.com/search?q=%22VGGT-Segmentor%3A%20Geometry-Enhanced%20Cross-View%20Segmentation%22&type=repositories))
- **PanSt3R: Multi-view Consistent Panoptic Segmentation** — *ICCV 2025* · [Paper](https://arxiv.org/abs/2506.21348) · [Code](https://github.com/naver/panst3r)

## SLAM, Robotics & Mapping

- **LingBot-Map: Geometric Context Transformer for Streaming 3D Reconstruction** — *arXiv 2026* · [Paper](https://arxiv.org/abs/2604.14141) · [Code](https://github.com/robbyant/lingbot-map)
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

A scheduled GitHub Action runs every Monday. It first synchronizes the reference repository, then queries OpenAlex for additional papers published since 2021, deduplicates records, searches GitHub for likely official implementations, applies the taxonomy, preserves curated honors, and regenerates this README and the visual timeline. The workflow can also be run manually from the Actions tab.

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

This repository mirrors 90 entries and their original categories from [End-to-End-3D-Reconstruction-Paper-List](https://github.com/chicleee/End-to-End-3D-Reconstruction-Paper-List). Metadata discovery for additional papers uses [OpenAlex](https://openalex.org/).

## License

MIT
