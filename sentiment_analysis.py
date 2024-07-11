import streamlit as st
from textblob import TextBlob

# Streamlit app
st.title("Sentiment Analysis of Reviews")

# User input for review
review = st.text_area("Enter your review:")

# Analyze sentiment when the button is pressed
if st.button("Analyze Sentiment"):
    if review:
        # Perform sentiment analysis
        blob = TextBlob(review)
        sentiment = blob.sentiment
        
        # Display the sentiment scores
        st.write("Sentiment Scores:")
        st.write(f"Polarity: {sentiment.polarity:.2f} (range: -1 to 1, where -1 is negative and 1 is positive)")
        st.write(f"Subjectivity: {sentiment.subjectivity:.2f} (range: 0 to 1, where 0 is objective and 1 is subjective)")
        st.write(f"Overall Sentiment: {'Positive' if sentiment.polarity > 0 else 'Negative' if sentiment.polarity < 0 else 'Neutral'}")
    else:
        st.error("Please enter a review to analyze.")

# To run the app, save this code in a file (e.g., sentiment_analysis.py) and run `streamlit run sentiment_analysis.py` in the terminal
