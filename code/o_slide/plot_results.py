#!/usr/bin/env python3
"""Plot cached projector diagnostic JSON, no model inference."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--metrics", required=True, type=Path)
    p.add_argument("--output", type=Path, default=Path("results/o_slide_projection.svg"))
    a = p.parse_args()
    m = json.loads(a.metrics.read_text())
    values = [m["preserve_relative_norm"], m["personal_relative_norm"]]
    fig, ax = plt.subplots(figsize=(8.5, 3.1))
    ax.barh(["Original X0", "Personal Xpers"], values, color=["#91C9BE", "#B8A9ED"])
    ax.invert_yaxis()
    ax.set_xlim(0, 1.1)
    ax.set_xlabel("Relative projected Frobenius norm")
    for i, val in enumerate(values):
        ax.text(val + 0.02, i, f"{val:.2%}", va="center")
    fig.tight_layout()
    a.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(a.output)
if __name__ == "__main__":
    main()
