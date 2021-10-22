import requests

def getTopHeadlinesForCountry(country):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=89eed2be904741288b6e80b2647dcb10"
    articles = requests.get(url).json()['articles']
    return articles

def getTopHeadlinesForCategory(category):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey=89eed2be904741288b6e80b2647dcb10"
    articles = requests.get(url).json()['articles']
    return articles

def getEverythingRelatedToSearchQuery(query, page=1):
    url = f"https://newsapi.org/v2/everything?q={query}&page={page}&apiKey=89eed2be904741288b6e80b2647dcb10"
    try:
        articles = requests.get(url).json()['articles']
        return articles 
    except:
        return []
