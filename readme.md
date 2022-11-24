Kindly go to config.cfg file and put third party movie username and password

First call localhost:8000/register with below request:<br><br>
{
    "username":"admin",
    "password":"password"
}

above api response will be below: <br><br>

{"token":"<token_value>"}

while calling an GET api localhost:8000/movies?page=<page_number>  <br>
provide key name as "api-key" in headers with token value<br>.

You will get below response:<br>
{
    "message": {
        "count": 45466,
        "next": "https://demo.credy.in/api/v1/maya/movies/?page=3",
        "previous": "https://demo.credy.in/api/v1/maya/movies/",
        "results": [{
            "title": "San Michele aveva un gallo",
                "description": "Sentenced to life imprisonment for illegal activities, Italian International member Giulio Manieri holds on to his political ideals while struggling against madness in the loneliness of his prison cell.",
                "genres": "",
                "uuid": "cc51020f-1bd6-42ad-84e7-e5c0396435a8"
        }]
}

