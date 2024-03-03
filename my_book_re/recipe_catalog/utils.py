from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q
from recipe_catalog.models import Recipe


def q_search(query):
    if query.isdigit() and len(query) <= 3:
        return Recipe.objects.filter(cooking_time=int(query))
    
    vector = SearchVector("name_recipe", "cooking_steps")
    query = SearchQuery(query)
    return Recipe.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()
     
    # for token in keywords:
    #     q_objects |= Q(name_recipe__icontains=token)
    #     q_objects |= Q(description__icontains=token)
    

    # return Recipe.objects.filter(q_objects)



