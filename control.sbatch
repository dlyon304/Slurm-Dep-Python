#!/bin/bash
#SBATCH --cpus-per-task=3
#SBATCH --mem=8G

eval $(spack load --sh miniconda3)

python3 main.py
