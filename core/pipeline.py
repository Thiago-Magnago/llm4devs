from loader import load
from transformer import transform
from embeddings import embed_docs, embed_doc
from retriever import store, retrieve

#source = "https://pt.wikipedia.org/wiki/Bel%C3%A9m_(Par%C3%A1)"
source = "https://g1.globo.com/mundo/noticia/2024/05/20/ebrahim-raisi-presidente-do-ira-morre-em-queda-de-helicoptero-diz-tv-estatal.ghtml"

source_loaded = load(source)
#print(source_loaded)

sources_transformed = transform(source_loaded[0].page_content)

#print(len(sources_transformed))
#print(sources_transformed)

sources_embedded = embed_docs(sources_transformed)

#print(len(sources_embedded))

stored = store(sources_transformed, sources_embedded)

query = embed_doc("Quem é o presidente do Irã?")

sources_retrieved = retrieve(query)

#print(sources_retrieved)