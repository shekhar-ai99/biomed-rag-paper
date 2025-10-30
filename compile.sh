#!/bin/bash

# Script to compile the LaTeX paper
# This script runs pdflatex twice and bibtex once to ensure
# proper compilation of bibliography and cross-references

echo "Compiling biomed-rag-paper..."

# First pass
echo "Running pdflatex (1st pass)..."
pdflatex -interaction=nonstopmode main.tex

# Run bibtex
echo "Running bibtex..."
bibtex main

# Second pass to resolve references
echo "Running pdflatex (2nd pass)..."
pdflatex -interaction=nonstopmode main.tex

# Third pass to ensure all references are correct
echo "Running pdflatex (3rd pass)..."
pdflatex -interaction=nonstopmode main.tex

# Clean up auxiliary files (optional - comment out if you want to keep them)
echo "Cleaning up auxiliary files..."
rm -f *.aux *.log *.out *.bbl *.blg *.toc *.lof *.lot

echo "Compilation complete! Output: main.pdf"
