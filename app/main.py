from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import the retrieval logic from retriever.py
from retriever import search_reviews

# Initialize Flask app
app = Flask(__name__, template_folder="static", static_folder="static")

# Displays a search box and retrieved results
@app.route("/", methods=["GET", "POST"])
def home():
    query = ""       # User query (text input)
    results = []     # Retrieved reviews

    # If the user submits a query via POST
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        if query:
            results = search_reviews(query)  # Perform the retrieval

    # Render the HTML template with results
    return render_template("index.html", query=query, results=results)

# Run the Flask app 
if __name__ == "__main__":
    app.run(debug=True)
