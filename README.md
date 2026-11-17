# 🧬 Automated Lipinski's Rule of Five Screening Pipeline

A modular Python cheminformatics pipeline built with `pubchempy` and `RDKit` to automate compound querying, 2D structure visualization, and drug-likeness screening.

# Key Features
* **Automated Database Querying:** Fetches connectivity SMILES strings directly from PubChem using chemical names.
* **Dual-Mode Screening:** Supports both individual compound analysis (with 2D molecular structure rendering) and batch list processing into structured Pandas DataFrames
* **Drug-Likeness Evaluation:** Computes Molecular Weight, LogP, H-Bond Donors, and H-Bond Acceptors to evaluate drug candidacy against Lipinski’s Rule of Five (1 Violation Threshold).
# Tech Stack
Python • RDKit • PubChemPy • Pandas • Matplotlib
