#!/bin/bash
# Verify all 6 IEEE figures exist

echo "🔍 Verifying 6 IEEE Figures..."
echo "================================"
echo ""

FIGURES=(
    "fig1_trust_vs_fact.pdf:Figure 1: Trust-Fact Correlation"
    "fig2_auc_comparison.pdf:Figure 2: AUC-ROC Comparison"
    "fig3_rouge_per_query.pdf:Figure 3: ROUGE-Fact per Query"
    "fig4_lig_heatmap.png:Figure 4: LIG Attention Heatmap"
    "fig5_trust_distribution.pdf:Figure 5: Trust Distribution"
    "fig6_precision_at_k.pdf:Figure 6: Retrieval Precision@K"
)

ALL_PRESENT=true

for entry in "${FIGURES[@]}"; do
    FILE="${entry%%:*}"
    DESC="${entry##*:}"
    
    if [ -f "$FILE" ]; then
        SIZE=$(ls -lh "$FILE" | awk '{print $5}')
        echo "✅ $DESC"
        echo "   File: $FILE ($SIZE)"
    else
        echo "❌ $DESC"
        echo "   File: $FILE (MISSING)"
        ALL_PRESENT=false
    fi
    echo ""
done

echo "================================"
if [ "$ALL_PRESENT" = true ]; then
    echo "✅ All 6 IEEE figures present!"
    echo ""
    echo "Total size:"
    du -sh fig*.pdf fig4*.png | awk '{sum+=$1} END {print "   " sum " KB"}'
    echo ""
    echo "Ready for IEEE paper submission! 🎉"
else
    echo "❌ Some figures are missing."
    echo "Run: bash ./run_full_analysis.sh"
fi
echo "================================"
