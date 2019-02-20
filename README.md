# Politize Recommendation Api

- [x] Authentication
- [x] Create POST
- [x] Create TAGS
- [x] Get recomendations

----

# How to run

- `$ git clone git@github.com:cleberpereiradasilva/politize-recommendation-api.git`
- `$ cd politize-recommendation-api`
- `$ python3 -m venv .env`
- `$ source .env/bin/activate`
- `$ pip install -r requirements`
- `$ cd politize_recommendation`
- `$ python manage.py migrate`
- `$ python manage.py runserver`

----

* Open in your browser `http://localhost:8000/v1`

----

# End points

- Posts: 
    * [GET] 
        - `http://localhost:8000/v1/post`
    * [GET] 
        - `http://localhost:8000/v1/post/:id`
    * [DELETE]
        - `http://localhost:8000/v1/post/:id`
    * [POST]
        - `http://localhost:8000/v1/post/`
        - Fields:
            ```
                {
                    "name": "",
                    "tags": []
                }
            ```
    * [PUT]
        - `http://localhost:8000/v1/post/:id`
        - Fields:
            ```
                {
                    "name": "",
                    "tags": []
                }
            ```
     


- Tags: `http://localhost:8000/v1/tag`
    * [GET] 
        - `http://localhost:8000/v1/tag`
    * [GET] 
        - `http://localhost:8000/v1/tag/:id`
    * [DELETE]
        - `http://localhost:8000/v1/tag/:id`
    * [POST]
        - `http://localhost:8000/v1/tag/`
        - Fields:
            ```
                {
                    "name": "",                   
                }
            ```
    * [PUT]
        - `http://localhost:8000/v1/tag/:id`
        - Fields:
            ```
                {
                    "name": "",                   
                }
            ```  
      



