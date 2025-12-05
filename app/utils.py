import pandas as pd
import os

def create_small_subset(input_path="data/Reviews.csv", output_path="data/small_reviews.csv", n=100):
    """
    Create a small subset (100 rows) from the original Kaggle dataset.
    If the large file is missing, use the small version instead.
    Raise an error only if both files are missing.
    """

    # If the large dataset is missing
    if not os.path.exists(input_path):
        # If the small subset already exists continue without errors
        if os.path.exists(output_path):
            return
        # If both are missing, raise an error
        raise FileNotFoundError(
            f"Neither {input_path} nor {output_path} exist. Please add at least one dataset."
        )

    # Read the large file and create a smaller version
    df = pd.read_csv(input_path)
    # Take only the first n rows (n = 100)
    small_df = df.head(n)
     # Save the smaller version into a new file
    small_df.to_csv(output_path, index=False)
    print(f" Created {output_path} with {len(small_df)} rows.")

if __name__ == "__main__":
    create_small_subset()