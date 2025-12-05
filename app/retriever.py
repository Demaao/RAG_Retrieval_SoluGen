import os
import pandas as pd
from openai import OpenAI
import chromadb
from dotenv import load_dotenv


# Load API key from .env file ,to keep it private
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Connect to OpenAI API
client = OpenAI(api_key=api_key)

# Initialize Chroma vector database
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="reviews_collection")

# Load small dataset (100 reviews)
data_path = "data/small_reviews.csv"
df = pd.read_csv(data_path)

# Use only the "Text" column and remove empty values
texts = df["Text"].dropna().tolist()[:100]

# Create embeddings and store in ChromaDB
# collection.count() returns the number of items currently stored in the database
# We only create embeddings if the database is empty, to avoid duplication
if collection.count() == 0:
    print("Creating embeddings for reviews...")

    for i, text in enumerate(texts):
         # Create an embedding vector for each review using OpenAI
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        vector = response.data[0].embedding

        # Add each embedding to the vector database
        collection.add(
            ids=[f"review_{i}"],    # unique ID for each review
            embeddings=[vector],    # the vector representation
            documents=[text]        # original text 
        )

    print(f"Stored {len(texts)} reviews with embeddings in Chroma DB.")


# Review Retrieval 
def search_reviews(query: str, top_k: int = 5, distance_threshold: float = 1.3):
    """
    Search for the most similar reviews to a user query.
    Uses cosine/L2 similarity between query and stored embeddings.
    """

    # Handle empty input
    if not query.strip():
        print("Error: Empty query.")
        return []

    # Create embedding for the user query
    response = client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    )
    query_vector = response.data[0].embedding

    # Query the Chroma vector database
    # This finds the most similar embeddings (closest distances)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )

    # Filter by distance (smaller distance = more similar)
    filtered_results = []
    for i, distance in enumerate(results["distances"][0]):
        if distance <= distance_threshold:
            filtered_results.append({
                "rank": i + 1,
                "distance": round(distance, 3),
                "text": results["documents"][0][i]
            })

    return filtered_results

# Interactive testing (run locally)
# For testing the retrieval system directly in the console
if __name__ == "__main__":
    print("Review Retrieval System (RAG)")
    print("Enter a sample query \n")

    query = input("Enter your question: ")
    matches = search_reviews(query)

    print(f"\nFound {len(matches)} relevant reviews:\n")

    if matches:
        for m in matches:
            print(f"Rank {m['rank']} | Distance: {m['distance']}")
            print(m['text'][:300], "\n---\n")
    else:
        print("No relevant reviews found for this query.\n")