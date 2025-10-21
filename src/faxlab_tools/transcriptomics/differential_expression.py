import anndata as ad
import scvi
import logging




# Function to examine Differential Gene Expression between two samples within a specific cluster

sample_A = "001"
sample_B = "002"

cluster_A = "1"
cluster_B = "2"

idx1 = [(adata.obs["Sample_Name"] == sample_A) & (adata.obs["leiden"] == cluster_A)]
idx2 = [(adata.obs["Sample_Name"] == sample_B) & (adata.obs["leiden"] == cluster_B)]


def deg_scvi_idx(
  adata,
  model,
  *,
  idx1=None,
  idx2=None,
  log_foldchange_cutoff=0.3,
  n_genes_to_plot=25,
  verbosity=False,
):
  global logger

  try:
    scvi_de = model.differential_expression(
      idx1=idx1,
      idx2=idx2,
      mode="change",
      silent=True,
    )
  except Exception as e:
    logger.warning(
      f"Differential expression failed for idx1 {idx1} vs idx2 {idx2} . It is likely that one of the samples contain no cells within one of the groups: {e}"
    )
    return (None, f"Error: {e}")

  # Make a list out of the statistically significant DE genes
  gene_list = scvi_de[(scvi_de["is_de_fdr_0.05"])].index.tolist()

  scvi_de_fc = scvi_de[
    (scvi_de["is_de_fdr_0.05"]) & (abs(scvi_de.lfc_mean) > log_foldchange_cutoff)
  ]

  scvi_de_fc = scvi_de_fc.sort_values("lfc_mean", ascending=False)

  logger.debug(
    f"Of the {len(gene_list)} statistically significant genes (p-adj < 0.05), there are {len(scvi_de_fc)} genes which have a greater than {log_foldchange_cutoff} change in the Log2FC"
  )

  if verbosity:
    display(gene_list)

  return (scvi_de_fc, None)


df, error = deg_scvi_idx(
  adata, scvi_model, idx1=idx1, idx2=idx2, log_foldchange_cutoff=0.3, n_genes_to_plot=25
)
