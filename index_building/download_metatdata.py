import dask.dataframe as dd
from dask.diagnostics import ProgressBar

ddf = dd.read_parquet("hf://datasets/fondant-ai/datacomp-small-clip/id_mapping")
ddf = ddf.rename(columns={"image_path": "url"})
ddf = ddf.repartition(npartitions=1)

with ProgressBar():
    ddf.to_parquet("datacomp_small/metadata")