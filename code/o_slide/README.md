# O-slide: projector reproducibility

The one-slide talk is in [o-slide.svg](../../slides/o-slide.svg). The edited matrices are the `to_k` and `to_v` cross-attention projections in Stable Diffusion v1.4.

The result is a **projector diagnostic**, not an image-quality score. The displayed reference values are from a previous small-`X0` run (118×768 text representations, 24×768 personalized representations, preservation rank 38): residual base-text norm ≈ 0%, retained personal-text norm ≈ 90.35%. Existing qualitative comparisons indicate preservation of ordinary generations but only partial identity transfer.

Numerical experiment (requires precomputed torch tensor matrices from the original pipeline):

```bash
python code/o_slide/run_experiment.py \
  --x0 /path/to/X0.pt \
  --xpers /path/to/X_pers.pt \
  --projector /path/to/P.pt \
  --output results/o_slide_metrics.json

python code/o_slide/plot_results.py \
  --metrics results/o_slide_metrics.json \
  --output results/o_slide_projection.svg
```

The experiment script can also construct a projector using `--preserve-rank 38` if `--projector` is omitted. To reproduce the *exact* earlier numbers, use the original saved projector and matrices. Do not conflate this experiment with image generation evaluation.
