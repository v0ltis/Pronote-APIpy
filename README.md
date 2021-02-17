# Pronote-APIpy
[Pronote-API](https://github.com/Litarvan/pronote-api) wrapper for Python 


How to install ?

The package is not avaiable yet :)


usage:

```python
import asyncio
import pronoteAPI as Pronote



async def login():
    client = await Pronote.Connexion.login(username='demonstration', password='pronotevs',
                                           url='https://demo.index-education.net/pronote/eleve.html')
    print(client.name)
    print(client.classe)
    
>>> "PARENT Fanny"
>>> "3A"
```
