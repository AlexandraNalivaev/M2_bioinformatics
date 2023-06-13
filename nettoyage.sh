#!/bin/bash

#SBATCH --job-name=cleaning
#SBATCH --output=/shared/projects/darkdino/finalresult/Tara_align/out/cleaning_%j.out

#SBATCH --time=2:00:00

#SBATCH --partition=fast
#SBATCH -A darkdino
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=100GB

SAMPLE=ERR1719220
# Indicate directory where unprocessed metaT sample is stored
DIR=/shared/projects/darkdino/finalresult/Tara_align/$SAMPLE
# LOAD version of TRIMMOMATIC
TRIMMOMATIC=/shared/home/analivaev/Trimmomatic-0.39/trimmomatic-0.39.jar

module load java-jdk/11.0.9.1

# Quality Control

java -jar $TRIMMOMATIC PE -threads 30 -phred33 $DIR/$SAMPLE'_1.fastq' $DIR/$SAMPLE'_2.fastq' $DIR/$SAMPLE'_1-trimmed.fastq' $DIR/$SAMPLE'_output_forward_unpaired.fq' $DIR/$SAMPLE'_2-trimmed.fastq' $DIR/$SAMPLE'_output_reverse_unpaired.fq' LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 > $DIR/$SAMPLE'_trimmomatic.txt' 2>&1

