#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1
#SBATCH --ntasks=1
#SBATCH --time=23:50:00
#SBATCH --mem=32GB
#SBATCH --job-name=RFMD
##SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-user=mdabdullahal.alamin@ucalgary.ca
#SBATCH --output=job_output/job_%j.txt

set -e
echo $1
echo $2

echo Job started
date


echo "========================================================================="

source /global/software/anaconda/anaconda3-2019.10-tensorflowgpu/anaconda3/etc/profile.d/conda.sh
conda activate image

echo "Necessary env loaded"

echo "Going to train model on " $1
# python -u train.py VGG19_without_transfer_learning
python -u train.py $1 $2

echo Job ended
date