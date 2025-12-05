# SoluGen AI – RAG Retrieval Assignment

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline focusing **only on the retrieval stage**, as required by the assignment.  
It demonstrates how to retrieve semantically relevant text reviews from a small dataset using **OpenAI embeddings** and **ChromaDB**, without any LLM or text generation.

---

## 1. Dataset Selection and Reasoning

**Dataset Used:** [Amazon Fine Food Reviews (Subset)](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)  
**Source:** Kaggle

### Why this dataset
- **Semantically meaningful**, allowing natural-language search.  
- **Free and publicly available** to ensure reproducibility.  

The *Amazon Fine Food Reviews* dataset fits these perfectly:
- Each review is 1–3 sentences long — short, natural, and human-written.  
- Reviews express clear opinions (e.g., “too sweet”, “bad packaging”), making them ideal for **semantic search**.  
- It is a well-known NLP dataset — credible, interpretable, and rich in meaning.  

To meet the assignment constraints, only a **subset of 100 reviews** was used and stored as `small_reviews.csv`.  
This keeps the project lightweight while remaining realistic for semantic retrieval.

### Thought process

I aimed for a dataset that feels **human and intuitive**, so semantic retrieval would be easily interpretable.  
For example:
- *“Find reviews about candy that’s too sweet”* :returns reviews about excessive sweetness.  
- *“Show opinions about product quality”* : retrieves reviews mentioning satisfaction or disappointment.  

I chose to extract a small subset from a large rather than using an obscure small one, to ensure data quality, credibility, and real world linguistic diversity while still keeping the project lightweight.

---

## 2. Vector Database: ChromaDB

**Chosen Vector DB:** [ChromaDB](https://www.trychroma.com)

### Justification

Several alternatives were considered, but **ChromaDB** was chosen because:
1. **Local and free** – no need for external servers or API keys.  
2. **Lightweight** – ideal for small experiments and student environments.  
3. **Integrates natively with OpenAI embeddings**.  
4. **Simple API** – add and query vectors in just a few lines.  
5. **Zero-cost deployment** – fully local and reproducible.  

### Design reasoning
The goal was to show conceptual understanding of **vector databases**:  
how textual meaning can be represented as numerical vectors and compared via distance metrics.  
ChromaDB provides the perfect sandbox for this — minimal setup, fast results, and easy inspection of stored vectors.  

---

## 3. Embedding Model

**Model:** `text-embedding-3-small` 
### Why this model
- High semantic accuracy with minimal cost.  
- 1536-dimensional vectors, sufficient for nuanced text representation.  
- Optimized for sentence-level text (short reviews).  
- Cost $0.01 total.

### Thought process

The focus was on efficiency and reproducibility.  
This model allows:
- **Accurate retrieval** for short sentences.  
- **Minimal expenses** (far below the $1 limit).  
- **Reusable embeddings** – generated once and cached locally.  
---

## 4. RAG Retrieval Pipeline
### Chunking Strategy

Each review is already short, so each one was treated as **a single semantic chunk** — preserving coherence and simplifying retrieval.

| Parameter  | Value        | Rationale |
|-------------|--------------|------------|
| Chunk size  | Full review  | Each review is already one coherent unit |
| Overlap     | 0 characters | No overlap needed for short text |

---

### Retrieval Parameters

| Parameter          | Value          | Reason |
| ------------------ | -------------- | ------- |
| Vector DB          | ChromaDB       | Local, fast, simple |
| Distance metric    | L2 (Euclidean) | Intuitive measure of semantic distance |
| Distance threshold | 1.3            | Filters out weak or noisy matches |
| Top-K              | 5              | Shows the 5 closest semantic matches |

**Retrieval process:**
1. The user enters a query.  
2. The query is embedded with the same model (`text-embedding-3-small`).  
3. The system compares the query vector with stored review vectors in Chroma.  
4. The top 5 reviews with the lowest distances are returned.  

This ensures the results are not keyword-based but **meaning-based**, representing true semantic similarity.

---

## 5. Application Architecture

### Chosen Technologies

| Component  | Technology | Reason |
|-------------|-------------|---------|
| Backend     | Flask       | Lightweight Python framework, easy integration |
| Frontend    | HTML/CSS     | Minimal UI, focuses on retrieval display |
| Vector DB   | ChromaDB     | Local, fast, free |
| Embeddings  | OpenAI `text-embedding-3-small` | Accurate, cost-effective |
| Dataset     | Kaggle (subset) | Human-written, interpretable text |

### Design reasoning

The architecture was intentionally simple and modular:
- `utils.py` :prepares and subsets the dataset.  
- `retriever.py` : handles embedding and vector retrieval.  
- `main.py` :Flask app that connects UI and backend.  
- `index.html`: displays results clearly to users.  

---

## 6. Development Thought Process

1. **Start small** — first validate embedding + similarity in the console.  
2. **Add structure** — split the logic into clear modules (`retriever`, `utils`, `app`).  
3. **Test retrieval logic** — use console mode for debugging before adding Flask.  
4. **Build the UI** — make it simple and functional (no distractions).  
5. **Add safety checks** — handle empty queries, missing data, or no results gracefully.  
6. **Ensure reproducibility** — all data and results can be regenerated locally.

This workflow demonstrates prioritizing correctness and clarity before complexity.

---

## 7. Example Queries
To test the system, use short, meaningful queries in the search box, such as:
- sweet candy  
- bad flavor  
- good product quality  
- spicy chips  
- coffee taste  

## 8. Summary and Reflection

By focusing on clarity and justification over complexity, the solution meets all technical and reasoning requirements of the **SoluGen AI RAG Retrieval Assignment**.

