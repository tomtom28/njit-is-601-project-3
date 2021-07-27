# IS 601 - Project 3


## Project Description
This project's goal was to use a REST API and use Postman to test the GET, POST, PUT, and DELETE request methods.

The data was taken from [this](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html) csv source and converted to SQL statements using [this](https://sqlizer.io/#/) online tool.


## API Endpoint Testing using Postman
As the project was built, each API endpoint was manually tested using Postman. The screenshots below show the results.

### Get All Players
API Endpoint of `localhost:5000/api/v1/players` with a `GET` request.
![api_all_players](screenshots/postman-get-all-players.png)

### View a Single Player By Id
API Endpoint of `localhost:5000/api/v1/player/:id` with a `GET` request for a given player `:id`.
![api_get_player](screenshots/postman-get-player.png)


### Add a New Player
API Endpoint of `localhost:5000/api/v1/player` with a `POST` request containing the JSON body playload below.
![api_post_new_player](screenshots/postman-post-new-player.png)

Note that we can query for all players again and see that the new player was added below.
Also note that the player id is 101 since the database will automatically increment the primary key.
![api_get_new_player](screenshots/postman-get-new-player.png)


### Update an existing Player
API Endpoint of `localhost:5000/api/v1/player` with a `PUT` request containing the JSON body playload below.
![api_put_update_player](screenshots/postman-put-update-player.png)

Note that we can query for the player by id again and see that the existing player indeed updated.
![api_get_update_player](screenshots/postman-get-update-player.png)


### Delete an existing Player
API Endpoint of `localhost:5000/api/v1/player/:id` with a `DELETE` using the player `:id`.
![api_delete_player](screenshots/postman-delete-player.png)

Note that we can query for the player by id again and see that the player no longer exists.
![api_get_deleted_player](screenshots/postman-delete-get-no-player.png)


## View Jinja Templates
The project also includes Jinja templates to view the MLB Player data in an HTML format. 
This is the same as was done in [Homework 5](https://github.com/tomtom28/njit-is-601-hw5).

### Homepage (View All Players)
The homepage will be rendered using `index.html` and it will show all the MLB Players in the database.
![jinja_index](screenshots/jinja-index.png)

### View Page (View Player by Id)
A view of one player by their database id will be rendered using `view.html`.
![jinja_view](screenshots/jinja-view.png)

### Add New Player Page
A new player can be added using the `new.html` page.
![jinja_new](screenshots/jinja-new-player.png)

The new player can then be seen at the bottom of the `index.html` page
![jinja_index_new_player](screenshots/jinja-index-new-player.png)

### Edit Existing Player Page
An existing player can be added updated using the `edit.html` page.
![jinja_edit](screenshots/jinja-edit.png)

The edited player can then be viewed by their `id` using the `view.html` page
![jinja_view_edited_player](screenshots/jinja-view-edit-player.png)


### Delete Existing Player
Using the delete button on the edit player page (`view.html` from above), we can remove the player record by `id`.

The player record will then no longer appear on the `index.html` page
![jinja_index_delete_player](screenshots/jinja-delete-player.png)