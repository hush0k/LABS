
#*1 task
def best_film(film_dict, movie):
    for film in film_dict:
        if film["imdb"] >= 5.5 and film['name'] == movie:
            print(True)
        elif film['imdb'] < 5.5 and film['name'] == movie:
            print(False)
            
#*2 task
def list_above(list):
    second = []
    for i in list:
        if i['imdb'] >= 5.5:
            second.append(i)
    print(second)
    
#*3 task
def categories(list, name):
    categories = None
    for i in list:
        if i['name'] == name:
            categories = i['category']
    
    for i in list:
        if i['category'] == categories:
            print(i)
            
#*4 task
def overall_avarage(list):
    overall_avarage = 0
    for i in list:
        overall_avarage += i['imdb']
    print(overall_avarage / len(list))
    
#*5 task
def cateogory_avarage(moves, category):
    ava = 0
    cnt = 0
    for i in moves:
        if i['category'] == category:
            ava += i['imdb']
            cnt += 1
    print(ava / cnt)
    
          
    
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

task = int(input("Enter task number: "))
if task == 1:
    name = str(input("Enter movie name: "))
    best_film(movies, name)
elif task == 2:
    list_above(movies)
elif task == 3:
    name = str(input("Enter movie name: "))
    categories(movies, name)
elif task == 4:
    overall_avarage(movies)
elif task == 5:
    category = input("Enter movies category: ")
    cateogory_avarage(movies, category)
            