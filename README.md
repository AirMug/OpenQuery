# Open-Ended Relational Query
Guide the on chain data retrieval process by providing explicit natural language instructions, via large multimodal models(LMMs) and large language models(LLMs). 

## Why we call it "Open-Ended"?
For information retrival, we want to get back information that matches data we inputed(e.g. images, texts).
Usually in this context, 'match' is used interchangeablly as "being similar/close". This is just too restrictful!

<p align="center">
    <img src="./media/lake_titicaca.jpg" alt="Lake Titicaca: What are other sight-seeings in the country?">
    <p align="center"> Lake Titicaca -> What are other sight-seeings in the country? </p>
</p>
We want to express more search intents! To give you an idea, say you're in Lake Titicaca, you shoot and upload an image, hoping to know other great sight-seeings in the country where the lake locates, the desired result returned should not be those that are similar to Lake Titicaca, we want to query information not based on "being similar", so traditional information retrival system cannot handle our search requests in such cases.

In this project, we propose open-ended relational query, where the search intents (by texts) are explicitly incorporated into the query process thanks to the multi-modal integration we shall talk about below

## Query Process
### Intergrate Multiple Modalities
Specifically, to integrate multiple deep modalities, we firstly apply CLIP to the text input and image query, resulting text embedding and vision embedding, which are then concatenated, 

<p align="center">
    <img src="./media/CLIP.png" alt="CLIP: Text Encoder and Vision Encoder", style="width: 50%; height: auto;">
    <p align="center"> CLIP: Text Encoder and Vision Encoder </p>
</p>

To further fuse the two embeddings, multiple self attention layers and another multi head attention pooler are employed to consecutively compress the multimodal inputs into a single embedding, let's call it **r** and this is our final embedding for the query.

<p align="center">
    <img src="./media/fusion_compression.png" alt="Fusion and Compression of multi-modal embeddings", \>
    <p align="center"> Fusion and Compression for multi-modal embeddings </p>
</p>

### Build Index Service for Targets
What should be return for query requests? We crawl images across the blockchain ledger, for each image, we add a default dummy text "" along with it to the two way encoders to get the final embedding, which we call r_t, we then store all the embeddings and build a KNN service that you can query into, then gives back k nearest neighrbors in the embedding space. To know more index building, refer to folder **index_building**, if you also want to dive deep into the way the backend hosting the Index Service, you can go to the folder **clip_index__back**.

### Start Services
A utility scripts **run.sh** is provided to start the query service locally.

```shell
# open a terminal, run
sh run.sh
```

## About this project

### History of participation in other hackthons
None, it's a new project.

### History of awards/grants/funding
None for a new project.