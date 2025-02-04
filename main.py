import pandas as pd
from ntscraper import Nitter
from pprint import pprint
import time
import boto3
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
scraper = Nitter(log_level = 1,skip_instance_check= False)
bedrock=boto3.client(service_name='bedrock-runtime',
                       region_name="us-east-1",
                       aws_access_key_id= '',
                       aws_secret_access_key=''
                     )
llm=Bedrock(model_id="amazon.titan-text-express-v1",client=bedrock,
                model_kwargs={})
def getSentiment(tweet):
  
  QUERY = """
  Analyze the sentiment of the following tweet and provide a one-word answer:
  Tweet: "{tweet}"
  Sentiment: [positive/negative/neutral]
  """
  input = QUERY.format(tweet=tweet)
  conversation = ConversationChain(
    llm=llm, verbose=True, memory=ConversationBufferMemory()
  )
  output=llm.invoke(input)
  #print(output)
  return output
  
  
def getTweet():
  #name = input("enter provider name : ")
  tweets = scraper.get_tweets("apollo pharmacy", mode='term', number=200)
  try:
    with open("tweet.txt",'a') as f:
      f.write(str(tweets['tweets'][0]))
  except Exception as e:
    print(e)
  # df = pd.DataFrame(tweets)
  # print(df)
  data = {
    'link':[],
    'text':[],
    'user':[],
    'likes':[],
    'Date':[],
    'quotes':[],
    'retweets':[],
    'comments':[],
    'sentiment':[]
  }
  
  for tweet in tweets['tweets']:
    data['link'].append(tweet['link'])
    data['text'].append(tweet['text'].replace(',','') if ',' in tweet['text'] else tweet['text'])
    data['user'].append(tweet['user']['name'].replace(',','') if ',' in tweet['user']['name'] else tweet['user']['name'])
    data['likes'].append(tweet['stats']['likes'])
    data['Date'].append(tweet['date'].replace(',','') if ',' in tweet['date'] else tweet['date'])
    data['quotes'].append(tweet['stats']['quotes'])    
    data['retweets'].append(tweet['stats']['retweets'])    
    data['comments'].append(tweet['stats']['comments'])
    data['sentiment'].append(getSentiment(tweet['text'].replace('""','') if '""' in tweet['text'] else tweet['text']))
  
  
  df = pd.DataFrame(data)
  print(df.head())
  df.to_csv("apollo.csv" ,mode='a', index=False)
  
getTweet()
