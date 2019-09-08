def  getMovieTitles(substr):
    if not isinstance(substr,str):
        return None
    import json, requests
    final = []
    r = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title=" + substr)
    a = json.loads(r.text)
    totalpages = a['total_pages']
    if totalpages == 0:
        return None
    for i in range(1,totalpages+1):
        r = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title="+ substr + "&page=" + str(i))
        a = json.loads(r.text)
        for movie in a['data']:
            final.append(movie['Title'])
    return sorted(final)


result = getMovieTitles('Spiderman')
print(result)