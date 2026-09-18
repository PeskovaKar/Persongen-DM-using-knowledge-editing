# Personalization of Text-to-Image Diffusion Models

This repository contains the thesis project of **Karina Peskova**.

The project focuses on personalization of text-to-image diffusion models using **knowledge editing techniques**. The main goal is to study whether a new visual concept can be inserted into a pretrained diffusion model by directly modifying a limited subset of its parameters, instead of fully fine-tuning the model.

## Main Idea

Standard personalization methods such as DreamBooth or LoRA usually require additional training. In this project, we investigate an alternative approach based on **model editing**.

## Research Questions

The project studies several questions related to diffusion model personalization:

* Can model editing replace or approximate LoRA-based personalization?
* Which model parameters are responsible for storing personalized visual concepts?
* How does the choice of concept identifier affect personalization quality?
* How does prior model knowledge interfere with newly introduced concepts?
* How can projection-based editing be relaxed to preserve both old and new knowledge?

## Model

**Stable Diffusion v1.4** and the Hugging Face `diffusers` framework.

## Repository Structure

-
