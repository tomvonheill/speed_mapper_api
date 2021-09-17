# random_compliment_generator

Simple API that will grab my internet speed data.

## Setup 
### Install environment
execute the following to set up environment

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip3 install -r requirements.txt

### Run flask app
execute the following to run app

    $ export FLASK_APP=flaskr
    $ flask run
## Endpoints

```GET``` '/all_data'
   
   This endpoint will grab all internet speed data availible, ordered by date tested.
   
   example:
```curl http://127.0.0.1:5000/get_all_data```

returns:
```javascript
{
    "date_time": "Mon, 13 Sep 2021 18:08:08 GMT",
    "download_speed": 115.09311024784216,
    "network_name": "tommy_buns_5g",
    "upload_speed": 4.5475297851678365
},....```