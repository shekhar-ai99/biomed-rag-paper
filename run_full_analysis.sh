#!/bin/bash
set -e  # Exit on error

echo "═══════════════════════════════════════════════════════════"
echo "  Biomedical RAG — Full Analysis Pipeline (IEEE 2025)"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Step 1: Generate synthetic MIMIC-III data
echo "📋 Step 1/4: Generating synthetic MIMIC-III data..."
python generate_dummy_mimic.py
echo ""

# Step 2: Run full RAG pipeline
echo "🚀 Step 2/4: Running RAG pipeline on dummy data..."
python run_rag_on_dummy.py
echo ""

# Step 3: Generate 6 IEEE publication figures
echo "📊 Step 3/4: Generating 6 IEEE publication figures..."
python plot_6_paper_figures.py
echo ""

echo "📊 (Python) Generating statistical summary and LaTeX table..."
python generate_summary.py

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "✅ DONE! All results generated successfully."
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "📋 Check outputs:"
echo "   • results_dummy.json       - RAG results"
echo "   • results_summary.txt      - Statistical summary"
echo "   • results_summary.tex      - LaTeX table for paper"
echo "   • fig1_trust_vs_fact.pdf   - Trust-Fact correlation"
echo "   • fig2_auc_comparison.pdf  - AUC-ROC comparison"
echo "   • fig3_rouge_per_query.pdf - ROUGE-Fact per query"
echo "   • fig4_lig_heatmap.png     - LIG attention heatmap"
echo "   • fig5_trust_distribution.pdf - Trust distribution"
echo "   • fig6_precision_at_k.pdf  - Retrieval precision@k"
echo ""
