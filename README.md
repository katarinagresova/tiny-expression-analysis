# tiny-expression-analysis

A small example project. It plots the expression of ten genes in two conditions, control and treated, with two
replicates each.

## Data

`data/example_counts.csv` has raw read counts: one row for each gene, one column for each sample. It is toy data, made
up for a demo.

The raw counts are read-only. The script never changes them, and it writes all output to `results/`.

## Output

`results/expression.png`: the expression of each gene in each sample, in counts per million (CPM).
