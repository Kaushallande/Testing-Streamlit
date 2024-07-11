import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit app
st.title("Sentiment Analysis of Reviews")

# User input for review
review = st.text_area("Enter your review:")

# Analyze sentiment when the button is pressed
if st.button("Analyze Sentiment"):
    if review:
        # Perform sentiment analysis
        sentiment = analyzer.polarity_scores(review)
        
        # Display the sentiment scores
        st.write("Sentiment Scores:")
        st.write(f"Positive: {sentiment['pos']:.2f}")
        st.write(f"Neutral: {sentiment['neu']:.2f}")
        st.write(f"Negative: {sentiment['neg']:.2f}")
        st.write(f"Overall Sentiment: {'Positive' if sentiment['compound'] >= 0.05 else 'Negative' if sentiment['compound'] <= -0.05 else 'Neutral'}")
    else:
        st.error("Please enter a review to analyze.")

# To run the app, save this code in a file (e.g., sentiment_analysis.py) and run `streamlit run sentiment_analysis.py` in the terminal
