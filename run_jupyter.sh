#!/usr/bin/env bash

# Expand notebooks
for notebook_script in notebooks/notebook_*.py; do
    echo Expanding $notebook_script
    jupytext --to notebook $notebook_script > /dev/null 2>&1
done

# Run jupyter
jupyter notebook

# Clean up generated notebooks
rm -rf notebooks/.ipynb_checkpoints
rm -rf .ipynb_checkpoints
rm notebooks/*.ipynb
