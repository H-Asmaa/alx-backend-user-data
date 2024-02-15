## FOLDER STRUCTURE



[0x01. Basic authentication](https://github.com/H-Asmaa/alx-backend-user-data/tree/main/0x01-Basic_authentication)
```
> 	[api]
> 		[v1]
> 			[auth]
> 				__ init __ .py
> 				auth.py
> 				basic_auth.py
> 			[views]
> 				__ init __ .py
> 				index.py
> 				users.py
> 			__ init __ .py
> 			app.py
> 		__ init __ .py
> 	[models]
> 		__ init __ .py
> 		base.py
> 		user.py
```

**UNDERSTANDING THE STRUCTURE**<br>
This structure is the typical layout for a python project, this one is specifically related to basic authentication in an API.
- When ever you see a file __ init __ .py inside a folder, it means that the folder is a python package.
- The folder [models] containing the models base.py and user.py
	- `base.py` : The base class that defines methods for initializing the attributes and converting to a JSON dictionary, and loading from file.... The  basic methods that we will be using to interact with the storage.
	- `user.py` : A class inheriting from Base that defines the attributes for a user, and defines methods that check the password's validity...
- The root folder [api] is the core of the application, it contains all the sub directories.
	- The folder [v1] is specifying the version 1 of this application. It contains the file app.py and __ init __ .py.
		- The folder [auth] containing the two classes we will be working with so far.
			- `auth.py` : The authentication class, that contains a method that checks if the path requested requires an authentication or not after checking it existence in the excluded paths. It has another method that extracts the header from the request.
			- `basic_auth.py` : Containing BasicAuth class that inherits from Auth and that is where we see the mechanism of one of the simplest API authentication which is **Basic Authentication**. The last method returns a user object after taking a couple of phases.
				1. extracting the base64 from authorization field in the header, which requires checking if the authorization header starts with `Basic` meaning it was encoded to base64. Then removing the `Basic` string.
				2. Decoding that encoded string to get the original string.
				3. Getting the user's email and password from the base64 decode.
				4. Getting the user instance with the looked up credentials.
				5. Finally returning the instance.
		- The folder [views]
			- `users.py` : basic endpoints of the API. This file contains the routes for the user and the method for each route.
			- `index.py` : All users endpoints. This file contains the routes for /status, /stats, /unauthorized, /forbidden.
		- `app.py` : The main entry point for  the API. Since we are setting a flask application that serves as an API, we will see some error handling in there, and a before request. Above there is the check for the content of the environment variable that we will set when running the application. And based on that content we are determining which class to instantiate from.
## SETUP THE APPLICATION
```bash
pip3 install -r requirements.txt
```
## RUNNING THE APPLICATION
```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```
- *API_HOST=0.0.0.0* : Sets the host IP address where the Flask development server will listen for incoming requests. It is set to *0.0.0.0* meaning the application will listen for requests from any IP address since *0.0.0.0* is bind address.
- *API_PORT=5000* : Specify that the port number is *5000*.
- *AUTH_TYPE=basic_auth* : Setting the environment variable *AUTH_TYPE* to be *basic_auth*.
- *python3 -m api.v1.app* : Executing the python module *app* that is within the folder [api]/[v1] using python3.
## THE ROUTES
- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
