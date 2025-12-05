# ⚙️ How to Run the RAG Retrieval App

## 1. Prerequisites

Make sure you have the following installed:

* Python 3.9 or newer
* pip (Python package manager)
* A valid OpenAI API key


## 2. Installation

Clone the repository and navigate into the project directory:
Create and activate a virtual environment
Install dependencies: such as :

```bash
pip install -r requirements.txt
```
---

## 3. Set Up API Key

Create a `.env` file in the project root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```
---

## 4. Project Structure

```
rag_retrieval_solugen/
│
├── app/
│   ├── main.py            # Flask app (UI + routing)
│   ├── retriever.py       # Embedding + retrieval logic
│   ├── utils.py           # Data preprocessing (creates small dataset)
│   └── static/
│       ├── index.html     # Simple HTML interface
│       └── style.css      # Minimal styling
│
├── data/
│   └── small_reviews.csv  # Subset of Kaggle dataset
│
├── .env                   # Contains your OpenAI API key
├── requirements.txt       # List of dependencies
├── README.md              # Main report: dataset choice, design decisions, assignment compliance
└── README_RUN.md          # Setup & run guide: how to install, configure, and test the app

```

---

## 5. Running the App

### – Web Interface (Flask)

Start the Flask web app:

```bash
python app/main.py
```
Then open your browser and go to:

```
http://127.0.0.1:5000
```

### Note : you can also test the retrieval system directly through the console.
This mode was mainly used during development and debugging to verify that the retrieval logic works correctly before connecting the web interface


## 7. Troubleshooting

| Issue                      | Solution                                         |
| -------------------------- | ------------------------------------------------ |
| `OPENAI_API_KEY` not found | Check `.env` file and restart terminal           |
| `ModuleNotFoundError`      | Reinstall with `pip install -r requirements.txt` |
| No results retrieved       | Try broader or simpler queries                   |
| Flask server not loading   | Verify you’re on `http://127.0.0.1:5000`         |

---

## Done!
You now have a fully working **RAG Retrieval System** using OpenAI embeddings and ChromaDB.