# IS 601 - Project 3


## Project Description
This project's goal was to use a REST API and use Postman to test the GET, POST, PUT, and DELETE request methods.

The data was taken from [this](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html) csv source and converted to SQL statements using [this](https://sqlizer.io/#/) online tool.


## API Endpoint Testing using Postman
As the project was built, each API endpoint was manually tested using Postman. The screenshots below show the results.

### Get All Players
API Endpoint of `localhost:5000/api/vi/players` with a `GET` request.
![api_all_players](screenshots/postman-get-all-players.png)

### View a Single Player By Id
API Endpoint of `localhost:5000/api/vi/player/:id` with a `GET` request for a given player `:id`.
![api_all_players](screenshots/postman-get-player.png)