import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("social_data.csv")  # e.g., tweets or posts

# Sentiment analysis
df['Sentiment'] = df['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Sentiment_Label'] = df['Sentiment'].apply(lambda x: 'Positive' if x>0 else ('Negative' if x<0 else 'Neutral'))

st.title("📊 Social Data Analysis Dashboard")

# Pie chart for sentiment
fig1 = px.pie(df, names='Sentiment_Label', title="Sentiment Distribution")
st.plotly_chart(fig1)

# Bar chart of top hashtags/keywords
df['hashtags'] = df['text'].str.extract(r"(#\w+)")
top_hashtags = df['hashtags'].value_counts().head(10).reset_index()
fig2 = px.bar(top_hashtags, x='index', y='hashtags', title="Top Hashtags")
st.plotly_chart(fig2)

# WordCloud
st.subheader("Word Cloud")
text = " ".join(str(t) for t in df['text'])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
st.pyplot(plt)
