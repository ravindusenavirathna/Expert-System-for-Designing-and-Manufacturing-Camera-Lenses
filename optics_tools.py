import numpy as np


def calculate_refractive_index(material):
    indices = {"BK7": 1.5168, "SF11": 1.7847}
    return indices.get(material.upper(), "Unknown material")


def ray_tracing(focal_length, aperture):
    # Placeholder for ray tracing simulation
    return f"Ray tracing completed for focal length: {focal_length}, aperture: {aperture}."
