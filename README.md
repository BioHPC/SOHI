# SOHI: Soil-Omics Health Indicators Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-Pending-blue)](http://doi.org)
[![Status](https://img.shields.io/badge/Status-Prototype-orange)]()

**SOHI** is an explainable AI framework designed to predict specific, measurable soil-health outcomes—specifically **Soil Organic Carbon (SOC)** and **Potentially Mineralizable Nitrogen (PMN)**—from genome-resolved metagenomes.

This platform integrates high-performance bioinformatics, causal inference (SEM), and explainable machine learning (TreeSHAP) to move beyond taxonomic inventories toward actionable, functional soil diagnostics.

---

## 📂 Repository Structure

This repository is organized to support the three core objectives of the SOHI framework:

### 1. Context Harmonization & Bioinformatics Core (`/context_harmonizer`, `/workflow`)
- **Context Harmonizer:** A Python module to standardize heterogeneous metadata (e.g., normalizing pH methods, texture classes, and units).
- **Bioinformatics Pipeline:** Snakemake workflows for:
  - Metagenomic assembly (MEGAHIT/OMEGA)
  - High-fidelity binning (MetaBAT2, MaxBin2, CONCOCT)
  - Functional annotation (KEGG, CAZy)

### 2. Causal & Predictive Engine (`/modeling`)
- **Multi-Level Feature Aggregation (MLFA):** Scripts to aggregate MAGs into "Microbial Cooperatives" and genes into "Functional Modules" (C/N/P cycling).
- **Causal Modeling:** Structural Equation Models (SEM) to filter features based on ecological plausibility.
- **Explainable AI:** XGBoost/Random Forest implementations with **TreeSHAP** integration to generate "SOHI Indicator Cards."

### 3. Validation & Benchmarking (`/benchmarks`)
- Protocols and datasets for the registered benchmark.
- Scripts for computational cross-validation against archived historical data (e.g., Morrow Plots).

---

## Getting Started

### Prerequisites
- **Conda** or **Mamba**
- **Docker** (optional, for containerized runs)

### Installation
```bash
git clone [https://github.com/BioHPC/SOHI.git](https://github.com/BioHPC/SOHI.git)
cd SOHI

# Create the environment
conda env create -f workflow/envs/sohi_core.yaml
conda activate sohi_core

## Usage Example

### 1. Harmonize Metadata

Standardize heterogeneous soil and environmental metadata using the context harmonizer.

```bash
python context_harmonizer/harmonize.py \
  --input raw_metadata.csv \
  --schema context_harmonizer/schema.json \
  --output clean_metadata.csv
```

---

### 2. Run the Modeling Engine

Predict soil health indicators (e.g., PMN) using aggregated functional features and harmonized metadata.

```bash
python modeling/predict_pmn.py \
  --features aggregated_modules.tsv \
  --metadata clean_metadata.csv
```

---

## Contact

Dr. Tae Hyuk Ahn  
Department of Computer Science  
Saint Louis University  
taehyuk.ahn@slu.edu

Dr. Laibin Huang  
Department of Biology  
Saint Louis University
laibin.huang@slu.edu
