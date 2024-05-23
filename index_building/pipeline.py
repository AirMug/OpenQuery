import pyarrow as pa
from fondant.pipeline import Pipeline, Resources

from config import BASE_PATH, CLIP_MODEL, OUTPUT_DIR


pipeline = Pipeline(
    name="index-datacomp-small-12m",
    base_path=BASE_PATH,
)

dataset = pipeline.read(
    "load_from_hf_hub",
    arguments={
        "dataset_name": "mlfoundations/datacomp_small",
        "index_column": "uid",
        "n_rows_to_load": 100,  # Remove this to run on full dataset
    },
    produces={
        "url": pa.string(),
    },
)

dataset = dataset.apply(
    "download_images",
    arguments={
        "n_connections": 4,
    },
    consumes={
        "image_url": "url",
    },
    resources=Resources(
        cpu_limit="4",
        memory_limit="8G",
    ),
    input_partition_rows=100,
)

dataset = dataset.apply(
    "embed_images",
    arguments={
        "model_id": CLIP_MODEL,
        "batch_size": 1,
    },
    resources=Resources(
        cpu_limit="4",
        memory_limit="8",
        # accelerator_number=4,
        # accelerator_name="NVIDIA_TESLA_T4",
        # accelerator_name="",
    ),
)

dataset.write(
    "write_to_file",
    arguments={
        "path": f"{BASE_PATH}/{OUTPUT_DIR}",
        "format": "parquet",
    },
    consumes={
        "embedding": pa.list_(pa.float32()),
        "url": pa.string()
     },
)