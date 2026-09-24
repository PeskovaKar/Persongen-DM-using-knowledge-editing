# PersonGen: Knowledge-Preserving Personalization of Diffusion Models

[![License](https://badgen.net/github/license/kisnikser/m1p-template?color=green)](LICENSE)

<table>
    <tr>
        <td align="left"> <b> Author </b> </td>
        <td> Karina Peskova </td>
    </tr>
    <tr>
        <td align="left"> <b> Consultant </b> </td>
        <td> Sergey Karpukhin </td>
    </tr>
    <tr>
        <td align="left"> <b> Advisor </b> </td>
        <td> Aibek Alanov </td>
    </tr>
</table>

## Assets

- [LinkReview](LINKREVIEW.md)
- [Code](code)
- [Paper](paper/main.pdf)
- [Slides](slides/main.pdf)

## Abstract

This research project studies personalization and concept editing of
text-to-image diffusion models.

The goal of the work is to investigate how a pretrained diffusion model
can learn new visual concepts while preserving previously acquired knowledge.

We combine DreamBooth LoRA personalization with AlphaEdit-based editing
methods and analyze the role of cross-attention parameters in concept transfer.

## Research Questions

- How is personalized concept information stored inside diffusion models?
- Can editing methods preserve pretrained model knowledge after personalization?
- Are cross-attention key/value matrices sufficient for concept transfer?

## Method

The proposed pipeline includes:

1. DreamBooth LoRA fine-tuning of Stable Diffusion.
2. Extraction of cross-attention key/value matrices.
3. Construction of concept embedding representations.
4. AlphaEdit-based model editing.
5. Evaluation of generated images and preservation of original capabilities.

## Experiments

Experiments include:

- different textual identifiers;
- LoRA training checkpoints;
- learning rate selection;
- AlphaEdit parameters;
- interpolation between LoRA and edited weights.

## Citation

```bibtex
@article{peskova2026personalization,
  title={PersonGen: Knowledge-Preserving Personalization of Diffusion Models},
  author={Karina Peskova},
  year={2026}
}
