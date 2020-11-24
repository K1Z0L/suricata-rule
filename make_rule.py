site = ["youtube.com", "en.wikipedia.org", "twitter.com", "facebook.com", "amazon.com", "yelp.com", "reddit.com", "imdb.com", "fandom.com", "pinterest.com", "tripadvisor.com", "instagram.com", "walmart.com", "craigslist.org", "ebay.com", "linkedin.com", "play.google.com", "healthline.com", "etsy.com", "indeed.com"]

for i, s in enumerate(site):
    data = f'alert tls any any -> any any (msg:"{s} access"; content:"{s}"; sid:{10000+i}; rev:1;)'
    print(data)