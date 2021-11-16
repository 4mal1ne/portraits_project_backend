# portraits_project_backend
___
# ***Quick start***: 
>### *download project :* 
>`git clone git@github.com:4mal1ne/portraits_project_backend.git`
>> ***Open project in you IDE***
> ___
>> ***Create migrations with*** `python3 manage.py makemigrations`
> ***and*** `python3 manage.py migrate`
> ___
>> ***Create superuser with*** `python3 manage.py createsuperuser`
>>> ***Download needed libraries like :***  
>> :white_check_mark: 'rest_framework'   
>> :white_check_mark: 'rest_framework.authtoken'  
>> :white_check_mark: 'rest_framework_swagger'  
>> :white_check_mark: 'djoser'   
>> :white_check_mark: 'Pillow'
> ___
>> ***Create main static folder with :*** `python3 namage.py collectstatic`
>___
>> ***run server :*** `python3 manage.py runserver`


# ***How it works :***

>### *For check all works API input this path to your browser:*
> `"your local host path/"` *+ :*  
>`api/v1/artworks/all_artworks` **Show you all artworks API.**   
> `api/v1/artworks/all_comments` **Show you all comments API.**   
> `api/v1/artworks/main_app/artworks/` **You can create a new work.**   
> `api/v1/artworks/main_app/comments/` **You can create a new comment for some work.**    
> `api/v1/artworks/detail/<int:pk>/` **Change\delete your work.**  
> ___
> `api/v1/create_auth/` **Register user.**  
> `docs/` **All the info about how worked this API.**  
> `swagger-docs/` **Show all available requests.**