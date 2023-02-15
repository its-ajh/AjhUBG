from django.template import Library;register = Library()


@register.filter(name='times') 
def times(number):
    return range(number)





@register.filter(name='checker')
def checker(lyrics):
    import json
    
    with open('notsogreatwords.json', 'r') as f:
      data = json.load(f)
      le =lyrics
      for word in lyrics.lower().split():
        if word in data:
         le =lyrics.replace(word, "(WATCH YOUR MOUTH)")
      return le