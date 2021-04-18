#TAccess Tokens
consumer_key= '####################'
consumer_secret= '##############################################'
access_token='##################################################'
access_token_secret='#############################################'
#Autenticando
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify = True)


for j in range(15,26): # fazer 1 a 25 se der certo
    df = pd.DataFrame(columns=['tweet_id',
                                'created_at',
                                 'text',
                                 'HouseRep', 'location', 'verified', 'followers_count', 'favourites_count' , 'retweeted'])
    for i in range(0+j*20,20 + j*20):
        alltweets = []  
        print(i)
                #make initial request for most recent tweets (200 is the maximum allowed count)
        try:
            new_tweets = api.user_timeline(screen_name = screen_name[i],count=200, tweet_mode='extended') #extended so it doesn´t truncate text
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
        except:
            pass

                #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print(f"getting tweets before {oldest}")

                    #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name[i],count=200,max_id=oldest,tweet_mode='extended')
                    #save most recent tweets
            alltweets.extend(new_tweets)
                    #print(alltweets[0])

                    #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
            
        for tweet in alltweets:
                try:
                    outtweets = [tweet.id_str, tweet.created_at, tweet.full_text, tweet.user.screen_name, tweet.user.location, tweet.user.verified, tweet.user.followers_count, tweet.user.favourites_count, tweet.retweeted]
                    df.loc[len(df)] = outtweets
                except:
                    pass
                    
                    
    df.to_csv('df_fixed_{0}'.format(j))