#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --mem=8G
#SBATCH --time=00:01:00

module load ml-gpu
cd /work/LAS/cjquinn-lab/zefuh/text2command/text2command/sentenceBERT
ml-gpu /work/LAS/cjquinn-lab/zefuh/text2command/DL_env/bin/python sentenceBERT.py > log
