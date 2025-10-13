from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

EMBED_MODEL = None

def get_embedding_model():
    global EMBED_MODEL
    if EMBED_MODEL is None:
        EMBED_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
    return EMBED_MODEL

def embed_texts(texts):
    model = get_embedding_model()
    return model.encode(texts, show_progress_bar=False, convert_to_numpy=True)

def cluster_embeddings(embeddings, n_clusters=5):
    if len(embeddings) < n_clusters:
        n_clusters = max(1, len(embeddings))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings)
    return labels
