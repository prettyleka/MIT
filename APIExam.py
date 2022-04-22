import requests_with_caching
def get_movies_from_tastedive(NameOfMovie):
    baseurl='https://tastedive.com/api/similar'
    params_diction={}
    params_diction['q']=NameOfMovie
    params_diction['type']='movies'
    params_diction['limit']='5'
    resp = requests_with_caching.get(baseurl, params=params_diction)
    NameOfMovie_ds=resp.json()
    return NameOfMovie_ds

def extract_movie_titles(x):
    namesOnly=[]
    for d in range(len(x['Similar']['Results'])):
        namesOnly.append(x['Similar']['Results'][d]['Name'])
    return namesOnly


def get_related_titles(y):
    newNames=[]
    for z in y:
        newNames.append(extract_movie_titles(get_movies_from_tastedive(z)))
    Names2=[]
    for i in range(len(newNames)):
        for j in newNames[i]:
            if j not in Names2:
                Names2.append(j)
    return Names2



#only titles
import requests_with_caching
def get_movie_data(titleOfMovie):
    baseurl='http://www.omdbapi.com/'
    params_diction={}
    params_diction['t']=titleOfMovie
    params_diction['r']='json'
    resp=requests_with_caching.get(baseurl,params=params_diction)
    titleOfMovie_ds=resp.json()
    return titleOfMovie_ds


def get_movie_rating(x):
    rating=0
    l=x['Ratings']
    for i in range(len(l)):
        if l[i]['Source']=='Rotten Tomatoes':
            st=l[i]['Value'].replace('%','')
            t=int((st))
            rating+=t
    return rating