import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def get_data_dimensions(df):
    return df.shape

def get_null_counts(df):
    return df.isnull().sum()

def has_duplicates(df):
    return df.duplicated().any()

def get_summary_statistics(df):
    return df.describe(include="all")

def get_movies_by_director(df, director="Masahiko Murata"):
    return df[df["director"] == director]

def get_mean_runtime(df):
    # Assuming 'duration' column is in the format "90 min"
    movie_df = df[df["type"] == "Movie"]
    movie_df["duration_mins"] = movie_df["duration"].str.extract(r'(\d+)').astype(float)
    return movie_df["duration_mins"].mean()

def get_top_country(df):
    return df["country"].value_counts().idxmax()

def plot_rating_bar_chart(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="rating", order=df["rating"].value_counts().index)
    plt.title("Distribution of Movie Ratings")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("ratings_bar_chart.png")  # Save for test verification

def get_total_counts(df):
    return df["type"].value_counts().to_dict()
