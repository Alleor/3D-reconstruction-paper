"""Mutually exclusive task taxonomy for the paper list."""

from __future__ import annotations

import re
import unicodedata
from typing import Any


CATEGORY_ORDER = [
    "Feed-Forward Geometry & Foundation Models",
    "Dense Depth, Surface & Mesh Reconstruction",
    "NeRF & Novel View Synthesis",
    "Gaussian Splatting",
    "Dynamic & 4D Reconstruction",
    "Object, Human & 3D Generation",
    "Semantic 3D Reconstruction",
    "SLAM, Robotics & Mapping",
]

CATEGORY_DESCRIPTIONS = {
    "Feed-Forward Geometry & Foundation Models": (
        "General-purpose visual geometry, camera/point prediction, SfM, and "
        "feed-forward reconstruction foundation models."
    ),
    "Dense Depth, Surface & Mesh Reconstruction": (
        "Methods whose primary output is dense depth, a mesh, TSDF/SDF, planes, "
        "or multi-view-stereo surface geometry."
    ),
    "NeRF & Novel View Synthesis": (
        "Neural radiance fields and non-Gaussian novel/free-view synthesis."
    ),
    "Gaussian Splatting": (
        "Static-scene or generalizable reconstruction whose primary "
        "representation is Gaussian splatting."
    ),
    "Dynamic & 4D Reconstruction": (
        "Time-varying scenes, motion-aware geometry, scene flow, and 4D rendering."
    ),
    "Object, Human & 3D Generation": (
        "Object-centric reconstruction, humans/avatars, and explicit 3D or scene generation."
    ),
    "Semantic 3D Reconstruction": (
        "Joint geometry with semantic, instance, or panoptic understanding."
    ),
    "SLAM, Robotics & Mapping": (
        "SLAM, odometry, robotic reconstruction, and local or large-scale mapping."
    ),
}

# Overrides are reserved for titles whose primary contribution cannot be
# inferred reliably from surface words alone.
TITLE_OVERRIDES = {
    "anyrecon arbitrary view 3d reconstruction with video diffusion model": "NeRF & Novel View Synthesis",
    "bundlesdf neural 6 dof tracking and 3d reconstruction of unknown objects": "Object, Human & 3D Generation",
    "diffusionsfm predicting structure and motion via ray origin and endpoint diffusion": "Feed-Forward Geometry & Foundation Models",
    "fast3r towards 3d reconstruction of 1000 images in one forward pass": "Feed-Forward Geometry & Foundation Models",
    "flowr flowing from sparse to dense 3d reconstructions": "NeRF & Novel View Synthesis",
    "from none to all self supervised 3d reconstruction via novel view synthesis": "Feed-Forward Geometry & Foundation Models",
    "gamba marry gaussian splatting with mamba for single view 3d reconstruction": "Object, Human & 3D Generation",
    "genrecon bridging generative priors for multi view 3d scene reconstruction": "Feed-Forward Geometry & Foundation Models",
    "gigamvs a benchmark for ultra large scale gigapixel level 3d reconstruction": "Dense Depth, Surface & Mesh Reconstruction",
    "kimera multi robust distributed dense metric semantic slam for multi robot systems": "SLAM, Robotics & Mapping",
    "multiview compressive coding for 3d reconstruction": "Object, Human & 3D Generation",
    "must3r multi view network for stereo 3d reconstruction": "Dense Depth, Surface & Mesh Reconstruction",
    "neuralrecon real time coherent 3d reconstruction from monocular video": "Dense Depth, Surface & Mesh Reconstruction",
    "neurar neural uncertainty for autonomous 3d reconstruction with implicit neural representations": "SLAM, Robotics & Mapping",
    "panoless environment reconstruction from partial reflective views": "Gaussian Splatting",
    "repurposing geometric foundation models for multi view diffusion": "Object, Human & 3D Generation",
    "sail recon large sfm by augmenting scene regression with localization": "Feed-Forward Geometry & Foundation Models",
    "sparsefusion distilling view conditioned diffusion for 3d reconstruction": "Object, Human & 3D Generation",
    "spars3r semantic prior alignment and regularization for sparse 3d reconstruction": "Gaussian Splatting",
    "slam3r real time dense scene reconstruction from monocular rgb videos": "SLAM, Robotics & Mapping",
    "splatam splat track map 3d gaussians for dense rgb d slam": "SLAM, Robotics & Mapping",
    "surflo consistent 3d surface flow model with global state": "Feed-Forward Geometry & Foundation Models",
    "unique r unified query based feedforward 3d reconstruction": "Feed-Forward Geometry & Foundation Models",
    "uniquer unified query based feedforward 3d reconstruction": "Feed-Forward Geometry & Foundation Models",
    "vggt x when vggt meets dense novel view synthesis": "NeRF & Novel View Synthesis",
    "vipe video pose engine for geometric 3d perception": "Dynamic & 4D Reconstruction",
    "zipmap linear time stateful 3d reconstruction via test time training": "SLAM, Robotics & Mapping",
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def has_any_phrase(text: str, terms: tuple[str, ...]) -> bool:
    padded = f" {text} "
    return any(f" {normalize(term)} " in padded for term in terms)


def classify_paper(title: str) -> str:
    text = normalize(title)
    if text in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[text]

    # Semantics is the output task even when the representation is Gaussian.
    if has_any(
        text,
        ("semantic", "panoptic", "instance segmentation", "instancesegmentation", "segmentor"),
    ):
        return "Semantic 3D Reconstruction"

    # Explicit generation and human/object reconstruction take precedence over
    # representation details such as diffusion or Gaussian splatting.
    if has_any_phrase(
        text,
        (
            "avatar", "avatars", "human", "humans", "clothed", "face", "faces",
            "hand", "hands", "object reconstruction",
            "3d generation", "scene generation", "video generation", "reconstruction and generation",
        ),
    ):
        return "Object, Human & 3D Generation"

    # Mapping is primary for Gaussian/NeRF SLAM and robotic systems. Generic
    # scalability, long context, or streaming are method properties, not tasks.
    if has_any_phrase(
        text,
        (
            "slam", "mapping", "map", "odometry", "multirobot", "multi robot",
            "robotic", "robot", "lidar",
        ),
    ):
        return "SLAM, Robotics & Mapping"

    if has_any(
        text,
        (
            "dynamic", "4d", "motion", "scene flow", "space time", "space-time",
            "d nerf", "d-nerf", "k planes", "k-planes",
        ),
    ):
        return "Dynamic & 4D Reconstruction"

    if has_any(text, ("gaussian", "splat", "gaussians")):
        return "Gaussian Splatting"

    if has_any(
        text,
        (
            "novel view", "view synthesis", "free view", "free-view", "radiance field",
            "nerf", "tensorf", "ibrnet", "rayzer", "sharp monocular",
        ),
    ):
        return "NeRF & Novel View Synthesis"

    if has_any(
        text,
        (
            "surface reconstruction", "neural surface", "signed distance", "sdf",
            "dense scene reconstruction", "detailed 3d reconstruction", "plane reconstruction",
            "planar 3d reconstruction", "multi view stereo", "multi-view stereo",
            "poisson surface", "depth aware", "depth-aware",
        ),
    ):
        return "Dense Depth, Surface & Mesh Reconstruction"

    if "generation" in text:
        return "Object, Human & 3D Generation"
    return "Feed-Forward Geometry & Foundation Models"


def reclassify_papers(papers: list[dict[str, Any]]) -> int:
    changed = 0
    for paper in papers:
        category = classify_paper(paper["title"])
        if paper.get("category") != category:
            paper["category"] = category
            changed += 1
    return changed
