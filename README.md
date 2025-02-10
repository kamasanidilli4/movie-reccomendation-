# 🎬 Movie Recommender System  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Sklearn-orange)  
![NLP](https://img.shields.io/badge/NLP-Text%20Processing-purple)  
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)  
![Status](https://img.shields.io/badge/Status-Active-success)  

## 🚀 Overview  
**Movie Recommender System** is a **content-based recommendation engine** built using **Machine Learning & NLP**. It analyzes **movie genres, actors, directors, and plot features** to recommend similar movies. The system is deployed as a **Streamlit web app** for user-friendly interaction.  

🔗 **Live Demo:** [Movie Minds](https://movie-mind.streamlit.app/)  

---

## 📌 Features  
✅ **Content-Based Filtering** – Recommends movies based on textual data analysis.  
✅ **NLP & ML Integration** – Uses **Bag of Words & Cosine Similarity** for pattern recognition.  
✅ **Interactive Web App** – Built with **Streamlit** for smooth user experience.  
✅ **Data Visualization** – Heatmaps & correlation matrices for insights.  
✅ **Scalable Model** – Works with a dataset of **13K+ movies** from **IMDB & TMDB**.  

---

## 🛠️ Technologies Used  
- **Python (Pandas, NumPy, Scikit-learn, NLTK)** 🐍  
- **Machine Learning (Bag of Words, Cosine Similarity)** 🤖  
- **Natural Language Processing (NLP, Stemming, Tokenization)** 📝  
- **Streamlit (Web App Development)** 🌐  
- **Data Visualization (Seaborn, Matplotlib)** 📊  

---

## 📂 Project Structure  
Movie-Recommender-System/ │── 📂 dataset/ # Processed movie datasets (IMDB, TMDB) │── 📂 StreamlitWebApp/ # Streamlit UI files │── 📜 preparing_dataset_1.ipynb # Data preprocessing step 1 │── 📜 preparing_dataset_2.ipynb # Data preprocessing step 2 │── 📜 preparing_dataset_3.ipynb # Data preprocessing step 3 │── 📜 MakingCombinedDataset.ipynb # Merges datasets │── 📜 model_making.ipynb # ML Model creation │── 📜 movie-recommender-system.py # Streamlit web app │── 📜 requirements.txt # Python dependencies │── 📜 README.md # Project documentation

yaml
Copy
Edit

---

## ⚡ Installation & Setup  
Follow these steps to set up the project **locally**:  

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/YourUsername/Movie-Recommender-System.git
cd Movie-Recommender-System
🔹 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 3. Prepare the Dataset
Run the following Jupyter Notebooks in order:

plaintext
Copy
Edit
1️⃣ preparing_dataset_1.ipynb  
2️⃣ preparing_dataset_2.ipynb  
3️⃣ preparing_dataset_3.ipynb  
Then, merge datasets:

plaintext
Copy
Edit
🔄 Run MakingCombinedDataset.ipynb
🔹 4. Train the Model
plaintext
Copy
Edit
🏗️ Run model_making.ipynb to train the recommendation engine
🔹 5. Run the Streamlit Web App
bash
Copy
Edit
cd StreamlitWebApp
streamlit run movie-recommender-system.py
✅ The app will launch in your browser! 🎉

🏗️ How It Works
1️⃣ Data Acquisition
📌 IMDB & TMDB datasets (15K movies) from Kaggle.

2️⃣ Data Preprocessing
✅ Extracted Title, Genres, Top Cast, Directors, Writers.
✅ Text Cleaning: Removed missing values, tokenized text, and applied stemming.
✅ Named Entity Recognition: Merged names (e.g., Sam Worthington → SamWorthington).

3️⃣ Data Visualization
📊 Used heatmaps & correlation matrices to analyze trends.

4️⃣ Model Creation
🔹 Algorithm: Bag of Words (BoW)
🔹 Similarity Metric: Cosine Similarity
🔹 Feature Engineering: Merged genres, actors, and directors into a single ‘Tags’ column.

python
Copy
Edit
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = CountVectorizer(max_features=13000, stop_words='english')
vectors = vectorizer.fit_transform(movie_data['Tags']).toarray()

similarity = cosine_similarity(vectors)
✅ Generates a 13K x 13K similarity matrix for recommendations.

5️⃣ Recommendation Logic
The system suggests the top 5 similar movies based on the computed similarity scores.

python
Copy
Edit
def recommend(movie):
    index = movie_data[movie_data['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
    
    recommended_movies = [movie_data.iloc[i[0]].Title for i in distances[1:6]]
    return recommended_movies
📸 Screenshots
🔍 Movie Search & Recommendations

📊 Data Visualization Heatmap

🎯 Results & Evaluation
🔎 Observational Analysis – Detected red flag movies and improved recommendations using manual validation.
📈 Performance Optimizations – Adjusted feature selection & stop-word removal to improve accuracy.

🚀 Future Enhancements
🔹 Hybrid Recommendation Model: Combine content-based & collaborative filtering.
🔹 Real-Time Movie Updates: Fetch new movies dynamically using an API.
🔹 User Feedback Mechanism: Allow users to rate recommendations to improve model performance.
🔹 Enhanced UI & UX: Improve web app interface with interactive visualizations.

🤝 Contributing
We welcome contributions! 🚀

Fork the repository
Create a new branch: git checkout -b feature/new-feature
Make your changes and commit: git commit -m "Add new feature"
Push to your branch: git push origin feature/new-feature
Open a Pull Request 🎉
📜 License
This project is licensed under the MIT License – feel free to modify and use it!

👨‍💻 Author
Developed by Aniket Panchal ✨
📧 Email: AniketPanchal1257@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/aniket-panchal-0a7b3a233/





🌟 If you found this project helpful, give it a star! ⭐
