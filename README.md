# PersonGen: Preserving Knowledge While Personalizing Diffusion Models

[![License](https://badgen.net/github/license/kisnikser/m1p-template?color=green)](LICENSE)

<table>
<tr>
<td><b>Author</b></td>
<td>Karina Peskova</td>
</tr>
<tr>
<td><b>Consultant</b></td>
<td>Sergey Karpukhin</td>
</tr>
<tr>
<td><b>Advisor</b></td>
<td>Aibek Alanov</td>
</tr>
</table>

## Assets

- [LinkReview](LINKREVIEW.md)
- [Code](code)
- [Paper](paper/main.pdf)
- [Slides](slides/main.pdf)

## Abstract

This research project studies personalization and concept editing of text-to-image
diffusion models.

The main goal is to investigate how a pretrained diffusion model can be adapted
to generate a new visual concept while preserving previously learned knowledge.

The project combines DreamBooth LoRA personalization with AlphaEdit-based model
editing methods. We analyze the role of cross-attention layers and study whether
key/value attention parameters contain sufficient information for transferring
personalized concepts.

## Research Questions

- How is personalized concept information represented inside diffusion models?
- Can model editing methods preserve the original model knowledge after personalization?
- What is the contribution of cross-attention key/value matrices to concept transfer?
- How do training parameters influence personalization quality?

## Method

The experimental pipeline consists of:

1. Fine-tuning Stable Diffusion using DreamBooth LoRA.
2. Extracting cross-attention parameters from the personalized model.
3. Constructing text embedding representations of original and personalized concepts.
4. Applying AlphaEdit-style constrained editing.
5. Comparing generation quality and concept preservation.

## Experiments

The project includes experiments with:

- different textual identifiers;
- LoRA checkpoints;
- learning rates;
- editing parameters;
- interpolation between LoRA and edited weights.

Evaluation focuses on:

- similarity of generated images to the target concept;
- preservation of pretrained generation abilities;
- influence of editing on model behavior.

## Citation

```bibtex
@article{peskova2026personalgen,
  title={PersonGen: Preserving Knowledge While Personalizing Diffusion Models},
  author={Karina Peskova},
  year={2026}
}
```

## Licence

MIT License.
