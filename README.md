# Awesome 3D Reconstruction Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Auto Update](https://github.com/Alleor/Awesome-3D-Reconstruction-Papers/actions/workflows/update-papers.yml/badge.svg)](https://github.com/Alleor/Awesome-3D-Reconstruction-Papers/actions/workflows/update-papers.yml)
![Papers](https://img.shields.io/badge/papers-49-blue)

A curated, automatically updated list of recent papers on 3D reconstruction.
收录近五年三维重建论文，并自动发现新论文及其开源代码。

> Coverage: 2021–2026 · Last content update: 2026-08-03 · Maintainer: [@Alleor](https://github.com/Alleor)

## Scope

Target venues: CVPR, ICCV, ECCV, TPAMI, IROS, ICRA, TRO, RA-L, ICLR, 3DV, arXiv. The rolling five-year window is based on publication date. Papers without a confidently matched official implementation are marked **Code pending**.

## Contents

- [Feed-forward and General Reconstruction](#feed-forward-and-general-reconstruction)
- [Neural Implicit Surfaces](#neural-implicit-surfaces)
- [Neural Rendering and Novel View Synthesis](#neural-rendering-and-novel-view-synthesis)
- [Gaussian Splatting](#gaussian-splatting)
- [Dynamic and 4D Reconstruction](#dynamic-and-4d-reconstruction)
- [Object and Human Reconstruction](#object-and-human-reconstruction)
- [Robotic Mapping and Large-scale Reconstruction](#robotic-mapping-and-large-scale-reconstruction)

## Venue coverage

| Venue | Papers |
|:--|--:|
| CVPR | 23 |
| ICCV | 3 |
| ECCV | 3 |
| TPAMI | 3 |
| IROS | 1 |
| ICRA | 2 |
| TRO | 2 |
| RA-L | 2 |
| ICLR | 3 |
| 3DV | 2 |
| arXiv | 5 |

## Feed-forward and General Reconstruction

- **MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos** — *arXiv 2026* [Paper](https://arxiv.org/pdf/2607.15211) · **Code pending** ([search](https://github.com/search?q=%22MAGiSt3R%3A%20Multi-Agent%20Feed-forward%203D%20Reconstruction%20from%20Monocular%20RGB%20Videos%22&type=repositories))
- **3D Reconstruction with Spatial Memory** — *3DV 2025* [Paper](https://arxiv.org/abs/2408.16061) · [Code](https://github.com/HengyiWang/spann3r)
- **Fast3R: Towards 3D Reconstruction of 1000+ Images in One Forward Pass** — *CVPR 2025* [Paper](https://arxiv.org/abs/2501.13928) · [Code](https://github.com/facebookresearch/fast3r)
- **SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos** — *CVPR 2025* [Paper](https://arxiv.org/abs/2412.09401) · [Code](https://github.com/PKU-VCL-3DV/SLAM3R)
- **VGGT: Visual Geometry Grounded Transformer** — *CVPR 2025* [Paper](https://arxiv.org/abs/2503.11651) · [Code](https://github.com/facebookresearch/vggt)
- **DUSt3R: Geometric 3D Vision Made Easy** — *CVPR 2024* [Paper](https://arxiv.org/abs/2312.14132) · [Code](https://github.com/naver/dust3r)
- **Grounding Image Matching in 3D with MASt3R** — *ECCV 2024* [Paper](https://arxiv.org/abs/2406.09756) · [Code](https://github.com/naver/mast3r)
- **MonoPlane: Exploiting Monocular Geometric Cues for Generalizable 3D Plane Reconstruction** — *IROS 2024* [Paper](https://arxiv.org/abs/2411.01226) · [Code](https://github.com/thuzhaowang/MonoPlane)
- **FineRecon: Depth-aware Feed-forward Network for Detailed 3D Reconstruction** — *ICCV 2023* [Paper](https://arxiv.org/abs/2304.01480) · [Code](https://github.com/apple/ml-finerecon)
- **NOPE-SAC: Neural One-Plane RANSAC for Sparse-View Planar 3D Reconstruction** — *TPAMI 2023* [Paper](https://arxiv.org/abs/2211.16799) · [Code](https://github.com/IceTTTb/NopeSAC)
- **NeuralRecon: Real-Time Coherent 3D Reconstruction from Monocular Video** — *CVPR 2021* [Paper](https://arxiv.org/abs/2104.00681) · [Code](https://github.com/zju3dv/NeuralRecon)

## Neural Implicit Surfaces

- **Neuralangelo: High-Fidelity Neural Surface Reconstruction** — *CVPR 2023* [Paper](https://arxiv.org/abs/2306.03092) · [Code](https://github.com/NVlabs/neuralangelo)
- **NeuralWarp: Time-Warping for Neural Surface Reconstruction** — *CVPR 2022* [Paper](https://arxiv.org/abs/2202.03848) · [Code](https://github.com/fdarmon/NeuralWarp)

## Neural Rendering and Novel View Synthesis

- **LVSM: A Large View Synthesis Model with Minimal 3D Inductive Bias** — *ICLR 2025* [Paper](https://arxiv.org/abs/2410.17242) · [Code](https://github.com/haian-jin/LVSM)
- **Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields** — *CVPR 2022* [Paper](https://arxiv.org/abs/2111.12077) · [Code](https://github.com/google-research/multinerf)
- **TensoRF: Tensorial Radiance Fields** — *ECCV 2022* [Paper](https://arxiv.org/abs/2203.09517) · [Code](https://github.com/apchenstu/TensoRF)
- **IBRNet: Learning Multi-View Image-Based Rendering** — *CVPR 2021* [Paper](https://arxiv.org/abs/2102.13090) · [Code](https://github.com/googleinterns/IBRNet)
- **MVSNeRF: Fast Generalizable Radiance Field Reconstruction from Multi-View Stereo** — *ICCV 2021* [Paper](https://arxiv.org/abs/2103.15595) · [Code](https://github.com/apchenstu/mvsnerf)
- **pixelNeRF: Neural Radiance Fields from One or Few Images** — *CVPR 2021* [Paper](https://arxiv.org/abs/2012.02190) · [Code](https://github.com/sxyu/pixel-nerf)

## Gaussian Splatting

- **PanoLess: Environment Reconstruction from Partial Reflective Views** — *arXiv 2026* [Paper](https://doi.org/10.48550/arxiv.2607.25362) · **Code pending** ([search](https://github.com/search?q=%22PanoLess%3A%20Environment%20Reconstruction%20from%20Partial%20Reflective%20Views%22&type=repositories))
- **No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images** — *ICLR 2025* [Paper](https://arxiv.org/abs/2410.24207) · [Code](https://github.com/cvg/NoPoSplat)
- **Gaussian-SLAM: Photo-realistic Dense SLAM with Gaussian Splatting** — *CVPR 2024* [Paper](https://arxiv.org/abs/2312.10070) · [Code](https://github.com/VladimirYugay/Gaussian-SLAM)
- **MonoGS: Gaussian Splatting SLAM from Monocular Videos** — *CVPR 2024* [Paper](https://arxiv.org/abs/2312.06741) · [Code](https://github.com/muskie82/MonoGS)
- **MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images** — *ECCV 2024* [Paper](https://arxiv.org/abs/2403.14627) · [Code](https://github.com/donydchen/mvsplat)
- **pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction** — *CVPR 2024* [Paper](https://arxiv.org/abs/2312.12337) · [Code](https://github.com/dcharatan/pixelsplat)
- **SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM** — *CVPR 2024* [Paper](https://arxiv.org/abs/2312.02126) · [Code](https://github.com/spla-tam/SplaTAM)
- **3D Gaussian Splatting for Real-Time Radiance Field Rendering** — *arXiv 2023* [Paper](https://arxiv.org/abs/2308.04079) · [Code](https://github.com/graphdeco-inria/gaussian-splatting)

## Dynamic and 4D Reconstruction

- **GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis** — *arXiv 2026* [Paper](https://doi.org/10.48550/arxiv.2607.21448) · **Code pending** ([search](https://github.com/search?q=%22GrainGS%3A%20Gradient-Decoupled%20Gaussian%20Splatting%20for%20Efficient%20Dynamic%20Novel%20View%20Synthesis%22&type=repositories))
- **S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image** — *arXiv 2026* [Paper](https://doi.org/10.48550/arxiv.2607.28164) · **Code pending** ([search](https://github.com/search?q=%22S-Avatar%3A%20Diffusion-Guided%20Gaussian%20Head%20Avatars%20from%20a%20Single%20Image%22&type=repositories))
- **MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion** — *ICLR 2025* [Paper](https://arxiv.org/abs/2410.03825) · [Code](https://github.com/Junyi42/monst3r)
- **4D Gaussian Splatting for Real-Time Dynamic Scene Rendering** — *CVPR 2024* [Paper](https://arxiv.org/abs/2310.08528) · [Code](https://github.com/hustvl/4DGaussians)
- **K-Planes: Explicit Radiance Fields in Space, Time, and Appearance** — *CVPR 2023* [Paper](https://arxiv.org/abs/2301.10241) · [Code](https://github.com/sarafridov/K-Planes)
- **D-NeRF: Neural Radiance Fields for Dynamic Scenes** — *CVPR 2021* [Paper](https://arxiv.org/abs/2011.13961) · [Code](https://github.com/albertpumarola/D-NeRF)
- **Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes** — *CVPR 2021* [Paper](https://arxiv.org/abs/2011.13084) · [Code](https://github.com/zhengqili/Neural-Scene-Flow-Fields)

## Object and Human Reconstruction

- **Gamba: Marry Gaussian Splatting With Mamba for Single-View 3D Reconstruction** — *TPAMI 2025* [Paper](https://arxiv.org/abs/2403.18795) · [Code](https://github.com/SkyworkAI/Gamba)
- **BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects** — *CVPR 2023* [Paper](https://arxiv.org/abs/2303.14158) · [Code](https://github.com/NVlabs/BundleSDF)
- **ECON: Explicit Clothed Humans Optimized via Normal Integration** — *CVPR 2023* [Paper](https://arxiv.org/abs/2212.07422) · [Code](https://github.com/YuliangXiu/ECON)
- **Multiview Compressive Coding for 3D Reconstruction** — *CVPR 2023* [Paper](https://arxiv.org/abs/2301.08247) · [Code](https://github.com/facebookresearch/MCC)
- **SparseFusion: Distilling View-Conditioned Diffusion for 3D Reconstruction** — *CVPR 2023* [Paper](https://arxiv.org/abs/2212.00792) · [Code](https://github.com/zhizdev/sparsefusion)
- **ICON: Implicit Clothed humans Obtained from Normals** — *CVPR 2022* [Paper](https://arxiv.org/abs/2112.09127) · [Code](https://github.com/YuliangXiu/ICON)

## Robotic Mapping and Large-scale Reconstruction

- **MoD-SLAM: Monocular Dense Mapping for Unbounded 3D Scene Reconstruction** — *RA-L 2024* [Paper](https://arxiv.org/abs/2402.03762) · **Code pending** ([search](https://github.com/search?q=%22MoD-SLAM%3A%20Monocular%20Dense%20Mapping%20for%20Unbounded%203D%20Scene%20Reconstruction%22&type=repositories))
- **NICER-SLAM: Neural Implicit Scene Encoding for RGB SLAM** — *3DV 2024* [Paper](https://arxiv.org/abs/2302.03594) · [Code](https://github.com/cvg/nicer-slam)
- **A Multirobot System for 3-D Surface Reconstruction With Centralized and Distributed Architectures** — *TRO 2023* [Paper](https://doi.org/10.1109/TRO.2023.3258641) · **Code pending** ([search](https://github.com/search?q=%22A%20Multirobot%20System%20for%203-D%20Surface%20Reconstruction%20With%20Centralized%20and%20Distributed%20Architectures%22&type=repositories))
- **GO-SLAM: Global Optimization for Consistent 3D Instant Reconstruction** — *ICCV 2023* [Paper](https://arxiv.org/abs/2309.02436) · [Code](https://github.com/youmi-zym/GO-SLAM)
- **NeurAR: Neural Uncertainty for Autonomous 3D Reconstruction With Implicit Neural Representations** — *RA-L 2023* [Paper](https://doi.org/10.1109/LRA.2023.3235686) · **Code pending** ([search](https://github.com/search?q=%22NeurAR%3A%20Neural%20Uncertainty%20for%20Autonomous%203D%20Reconstruction%20With%20Implicit%20Neural%20Representations%22&type=repositories))
- **SHINE-Mapping: Large-Scale 3D Mapping Using Sparse Hierarchical Implicit Neural Representations** — *ICRA 2023* [Paper](https://arxiv.org/abs/2210.02299) · [Code](https://github.com/PRBonn/SHINE_mapping)
- **Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems** — *TRO 2022* [Paper](https://arxiv.org/abs/2106.14386) · [Code](https://github.com/MIT-SPARK/Kimera-Multi)
- **GigaMVS: A Benchmark for Ultra-Large-Scale Gigapixel-Level 3D Reconstruction** — *TPAMI 2021* [Paper](https://doi.org/10.1109/TPAMI.2021.3115028) · **Code pending** ([search](https://github.com/search?q=%22GigaMVS%3A%20A%20Benchmark%20for%20Ultra-Large-Scale%20Gigapixel-Level%203D%20Reconstruction%22&type=repositories))
- **Poisson Surface Reconstruction for LiDAR Odometry and Mapping** — *ICRA 2021* [Paper](https://doi.org/10.1109/ICRA48506.2021.9562069) · **Code pending** ([search](https://github.com/search?q=%22Poisson%20Surface%20Reconstruction%20for%20LiDAR%20Odometry%20and%20Mapping%22&type=repositories))

## Automatic updates

A scheduled GitHub Action runs every Monday. It queries OpenAlex, keeps only relevant computer-vision/robotics papers from the target venues and rolling five-year window, deduplicates records, searches GitHub for likely official implementations, and regenerates this README. The workflow can also be run manually from the Actions tab.

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

The presentation is inspired by [End-to-End-3D-Reconstruction-Paper-List](https://github.com/chicleee/End-to-End-3D-Reconstruction-Paper-List). Metadata discovery uses [OpenAlex](https://openalex.org/).

## License

MIT
