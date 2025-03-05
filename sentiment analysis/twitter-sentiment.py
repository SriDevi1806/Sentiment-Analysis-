from transformers import AutoTokenizer, AutoModelForSequenceClassification

from scipy.special import softmax


tweet = "Hello Guys!  :)"

tweet_word = []

for word in tweet.split(" "):
    if word.startswith("@")and len(word)> 1:
        word = "@user"

    elif word.startswith("http"):
        word = "http"
    tweet_word.append(word)

tweet_proc = " ".join(tweet_word)

roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)

tokenizer = AutoTokenizer.from_pretrained(roberta)

lables = ["Negative", "Netural", "Positive"]


#sentiment analaysis 

encoded_tweet = tokenizer(tweet_proc, return_tensors ="pt")

#utput = model(encoded_tweet["input_ids"],encoded_tweet['attention_mask'])
output = model(**encoded_tweet)

scores = output[0][0].detach().numpy()
scores = softmax(scores)
print(scores)

for i in range(len(scores)):
    l = lables[i]
    s = scores[i]
    print(l,s)