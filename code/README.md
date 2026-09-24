# Code

This directory contains the source code for the **PersonGen** research project on
knowledge-preserving personalization of text-to-image diffusion models.

The implementation covers the full experimental pipeline: DreamBooth LoRA
personalization, extraction of cross-attention parameters, construction of text
representation matrices, AlphaEdit-based model editing, and evaluation of the
resulting models.

> [!IMPORTANT]
> Jupyter notebooks, if present, are used for visualization and exploratory analysis only.
> The main experimental pipeline is implemented in Python scripts to ensure reproducibility.

## Pipeline

The experimental workflow consists of the following stages:

1. **DreamBooth LoRA personalization**  
   Fine-tune Stable Diffusion on a small set of images representing a target concept.

2. **Cross-attention weight extraction**  
   Extract key and value projection matrices from the personalized model.

3. **Text representation construction**  
   Build embedding matrices for the original and personalized concepts using different
   token-selection strategies.

4. **AlphaEdit-based editing**  
   Apply a knowledge-preserving update to the cross-attention parameters.

5. **Evaluation and ablations**  
   Compare LoRA and edited models across different identifiers, checkpoints,
   learning rates, and editing configurations.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>/code