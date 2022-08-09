# K-Drama-Recommendation-System
Data Preperation:
The dataset is created with the help of webscrapping techniques using beautifulsoup from rakuten viki and mydramalist websites. The dataset contains a total of 677 dramas. The dataset contains the title and the description of the drama.

Recommendation System:
For this model I have used content based recommendation system approach. I have used TfidfVectorizer for data preprocessing and sigmoid kernal to find the similarity between the dramas. The output is an similarity matrix.
The GUI is made using the gradio package, the user can give the input title of the drama he recently seen and number of recommendations he want. The output will be the drama names with the similarity scores sorted in high to low.
