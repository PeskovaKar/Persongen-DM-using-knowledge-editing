#!/usr/bin/env python3
"""Projector diagnostic: compute metrics only, no plotting."""
import argparse, json
from pathlib import Path
import torch

def load(path):
    t = torch.load(path, map_location="cpu", weights_only=True)
    if not isinstance(t, torch.Tensor) or t.ndim != 2:
        raise ValueError(f"Expected 2D tensor in {path}")
    return t.double()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--x0", type=Path, required=True)
    p.add_argument("--xpers", type=Path, required=True)
    p.add_argument("--projector", type=Path)
    p.add_argument("--preserve-rank", type=int, default=38)
    p.add_argument("--output", type=Path, default=Path("results/o_slide_metrics.json"))
    a = p.parse_args()
    x0, xp = load(a.x0), load(a.xpers)
    if x0.shape[1] != xp.shape[1]:
        raise ValueError("Embedding dimensions differ")
    if a.projector:
        proj = load(a.projector)
    else:
        if not 0 <= a.preserve_rank <= min(x0.shape):
            raise ValueError("Invalid preserve rank")
        _, _, vh = torch.linalg.svd(x0, full_matrices=False)
        v = vh[:a.preserve_rank]
        proj = torch.eye(x0.shape[1], dtype=x0.dtype) - v.T @ v
    if proj.shape != (x0.shape[1], x0.shape[1]):
        raise ValueError("Projector dimensions mismatch")
    rel = lambda x: (torch.linalg.matrix_norm(x @ proj) / torch.linalg.matrix_norm(x)).item()
    result = {
        "x0_shape": list(x0.shape),
        "xpers_shape": list(xp.shape),
        "projector_source": str(a.projector) if a.projector else "svd",
        "preserve_rank": a.preserve_rank if not a.projector else None,
        "preserve_relative_norm": rel(x0),
        "personal_relative_norm": rel(xp),
        "idempotence_relative_error": (torch.linalg.matrix_norm(proj @ proj - proj) / torch.linalg.matrix_norm(proj)).item(),
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
