# index building
cd index_building

python3 -m venv .env
source .env/bin/activate

pip install -r requirements.txt
pip install dask huggingface_hub
mkdir datacomp_small
wget -O datacomp_small/image.index https://huggingface.co/datasets/fondant-ai/datacomp-small-clip/resolve/main/faiss?download=true -q --show-progress

python download_metadata.py

cd ..

# start backend knn service
cd clip_index_back
sh start_index_service.sh
cd ..

# query demo
cd query
python demo.py