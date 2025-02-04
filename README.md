## Sentiment Analysis on X (formerly Twitter) Comments Using Bedrock

This project performs sentiment analysis on comments and emojis provided by users on any service provider’s official page on X (formerly known as Twitter). The application uses Nitter for scraping tweets and AWS Bedrock for sentiment analysis.

### Features

- **Scrape Tweets**: Retrieve tweets from a specified X handle using Nitter.
- **Sentiment Analysis**: Analyze the sentiment of each tweet using AWS Bedrock.
- **Data Storage**: Store the analyzed data in a CSV file.

### Installation

To run this project, you need to install the following libraries:

```bash
pip install pandas ntscraper boto3 langchain
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sentiment-analysis-x-comments.git
cd sentiment-analysis-x-comments

2. run main.py

### Output

![image](https://github.com/user-attachments/assets/59fe2bfb-e079-4f20-8dac-8908ec4e5c7c)

### CSV file

![image](https://github.com/user-attachments/assets/08e58ad0-aff9-44c9-8e15-f2ecc0b8608d)

