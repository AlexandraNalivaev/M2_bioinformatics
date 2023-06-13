#!/bin/bash

#SBATCH --job-name=salmon_mapping
#SBATCH --output=/shared/projects/darkdino/finalresult/Tara_align/out/mapping_%j.out

#SBATCH --time=2:00:00

#SBATCH --partition=fast
#SBATCH -A darkdino
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=100GB

SAMPLE=ERR1719220
# Indicate the directory where the metaT  samples (forward and reverse) are stored
DIR_SAMPLE=/shared/projects/darkdino/finalresult/Tara_align/$SAMPLE
# Indicate the directory where SALMON stored its index of reference sequences
DIR_INDEX=/shared/projects/darkdino/finalresult/Tara_align/Ref_seq/index_output_directory
# Indicate directory where you wish to store mapping outputs
DIR_OUTPUT=/shared/projects/darkdino/finalresult/Tara_align/$SAMPLE/salmon_output_directory

# LOAD VERSION OF SALMON
SALMON=/usr/local/genome2/salmon-0.11.3/bin/salmon

$SALMON quant -i $DIR_INDEX -l A -1 $DIR_SAMPLE/$SAMPLE'_1-trimmed.fastq' -2 $DIR_SAMPLE/$SAMPLE'_2-trimmed.fastq' -o $DIR_OUTPUT
