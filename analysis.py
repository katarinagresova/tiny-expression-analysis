"""Plot the expression of each gene in each sample."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Raw read counts: one row for each gene, one column for each sample
counts = pd.read_csv("data/example_counts.csv", index_col="gene")

# Normalize for sequencing depth: counts per million (CPM)
cpm = counts / counts.sum() * 1_000_000

# Plot: control in blue, treated in orange
ax = cpm.plot.bar(figsize=(14, 5), rot=0, width=0.8,
                  color=["#9ecae1", "#3182bd", "#fdae6b", "#e6550d"])
ax.set_xlabel("")
ax.set_ylabel("Expression (CPM)")
ax.set_title("Gene expression: control vs treated")
plt.tight_layout()

Path("results").mkdir(exist_ok=True)
plt.savefig("results/expression.png", dpi=150)
print("Saved results/expression.png")
