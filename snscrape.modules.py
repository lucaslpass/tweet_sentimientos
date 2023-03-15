import logging
import snscrape.modules.twitter

import pandas as pd

query ="Python"
tweets = []
limit = 1





logging.basicConfig(level = logging.DEBUG)
next(snscrape.modules.twitter.TwitterUserScraper('textfiles', retries = 0).get_items())
df=pd.DataFrame(tweets)
print(df.dtypes)