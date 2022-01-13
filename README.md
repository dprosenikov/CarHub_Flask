# CarHub_Flask

## Setup

In order to run the app, you need to install first all dependencies from requirements.txt

## Summary

The app contains 12 endpoints.

1. Register(accessible for anyone) - creates a user in the DB
2. Login(accessible for anyone) - logs in the user based on the username and password and if succesful, a jwt is being
   generated
3. Delete profile(login required & user must be either ADMIN or the owner of the profile) - deletes the selected profile
   and all cars added by this profile
4. Get all profiles(login required & user must be ADMIN) - lists all profiles along with the cars added by each of them
5. All cars(accessible for anyone) - lists all cars from the DB
6. My cars(login required) - lists all cars added by the logged-in user
7. Add car(login required) - creates a record in the DB and adds the car with the details from the schema
8. Car details(accessible for anyone) - displays the details for the selected car
9. Edit car(login required & user must be either ADMIN or the owner of the car) - modifies the data for the selected car
10. Delete car(login required & user must be either ADMIN or the owner of the car) - deletes the selected car
11. Search in the app by car brand(accessible for anyone) - returns all cars that contain the searched string in their
    brand names(case insensitive)
12. Google search(3rd party service accessible for anyone) - uses Google search to find results for the searched string.
    At the moment this is set to search in certain website(www.caroftheyear.org) and returns the first 10 results. It
    can be modified to search in any particular website or in the web in general.
