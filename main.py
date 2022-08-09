import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
import gradio as gr
tfidf=TfidfVectorizer(min_df=3,max_features=None,strip_accents='unicode',analyzer='word',token_pattern=r'\w{1,}',ngram_range=(1,3),stop_words='english')
df=pd.read_csv('Dataset.csv')
df['description']=df['description'].fillna('')
for i in range(len(df['title'])):
    df['title'][i]=df['title'][i].lower()
    df['description'][i]=df['description'][i].lower()

tfidf_matrix=tfidf.fit_transform(df['description'])

sigmoid=sigmoid_kernel(tfidf_matrix,tfidf_matrix)

indices=pd.Series(df.index,index=df['title']).drop_duplicates()

def give_rec(Title,Top_recommendations):
    title=Title.lower().strip()
    index=indices[title]
    sigmoid_score=list(enumerate(sigmoid[index]))
    sigmoid_score=sorted(sigmoid_score,key=lambda  x: x[1],reverse=True)
    sigmoid_score=sigmoid_score[1:int(Top_recommendations)+1]
    movie_index=[i[0] for i in sigmoid_score]
    x= df['title'].iloc[movie_index]
    text=''
    for idx, col in enumerate(x):
        text += '{}: {}\n'.format(col, sigmoid_score[idx])
    return text

interface = gr.Interface(fn=give_rec,
                         inputs=[gr.inputs.Textbox(lines=2, placeholder='Enter your comment'),gr.inputs.Textbox(lines=1, placeholder='How many recommendations do need?')],outputs='text')
interface.launch(share=True)