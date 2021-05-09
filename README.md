# YearView (Shopify Fall 2021 Backend Dev Challenge)

![Yearview](https://user-images.githubusercontent.com/69891859/117560163-5df75400-b059-11eb-81bb-a84ebec9cbed.gif)


You can check out a full demo of the project [here](https://www.youtube.com/watch?v=iAI6MHgDDDA)

Or go [here](https://www.youtube.com/watch?v=2wQqpM33VCY) if you want to save a few minutes of cringe...

## What is it/Inspiration

YearView is a secure photo storage app that allows one to keep track of their photos and reminisce upon the memories they made throughout the year.

Have you ever looked back and thought damn New Years was just last week, but you wake up and it's the start of fricking May?! What happened in between?? Well, with YearView, you will be able to see what you did in all those months and realize all that you have accomplished!

## Features

- Add pictures 1 by 1 or in bulk, allowing different image formats such as png or jpg
- Delete pictures
- Search/filter pictures by common characteristics
- Securly upload/delete pictures
- A month view that allows you to see the pictures you added in each month
- Secure Login/Account Creation mechanism (only you can see your pictures)

## Endpoints

|Endpoint | Use |
|---------|-----|
|/        | Landing page where user can enter login credentials and enter the app|
|/signup  | Page where user can create an account and set up their username, password and name |
|/check   | Once user enters login credentials, they get tested with the data in Mongo to ensure the correct person is accessing this account|
|/user    | Once user is successfully logged in, they will be able to use all features of app and upload pictures|
|/user/add-image| Endpoint where user can upload a picture and assign values to it such as: description, category etc.|
|/user/[image-key]| Retrieves an image from the DB based on the key |
|/user/month/[month-name] | User can see all the pictures they added in a certain month |
|/user/image/info/[image-key] | User can see the information about a specific image such as: description, category and the date it was added |
|/user/image/delete/[image-key]| Deletes an image from the DB corresponding to its specific key |
|/user/filter/[image_filter] | Switches the category of the filter, allowing user to customize which images are shown |
|/signout | Signs the user out of the app |

## Tools

- Python (Server)
- Flask (Server)
- MongoDB (Server)
- HTML/CSS/JS (Client)

## Installation

1. Git clone this repo onto your local (i.e copy the following into your command prompt)

        git clone https://github.com/parth-p29/Shopify-Fall-2021-Backend-Dev-Challenge.git

2. Run the following to install all dependencies:

        pip install -r requirements.txt
        
3. Create an account on [MongoDB](https://www.mongodb.com/try) and make a new DB and copy the Mongo Connection String
4. Traverse to app.py and place the connection you got into here:

        app.config['MONGO_URI'] = 'YOUR CONNECTION STRING + &ssl=true&ssl_cert_reqs=CERT_NONE'

5. Start the app by running "flask run" and go to [localhost:5000](http://localhost:5000/) into your browser
6. Enjoy! 

## Usage (Examples)

This is a simple mechanism for creating an account and logging in:

- Passwords are 64-bit encrpyted
- Many edge cases are considered such as if the confirm password doesn't match the entered password, if the username is already taken, if a wrong password is entered, etc.

![Yearview (1)](https://user-images.githubusercontent.com/69891859/117579267-1ce65a80-b0c0-11eb-8c1a-c69c48dcb247.gif)

This is how a user can upload pictures and view the certain pictures they added in a specific month

- Each image is connected to a secure key, ensuring safe image upload and retrieval
- Images can be uploaded in bulk thus, saving time when having to save large amounts of pictures
- Users can look back upon the months and see what they did in each one to retain fond memories
- The color of the month gets brighter depending on the amount of images uploaded

![Yearview (3)](https://user-images.githubusercontent.com/69891859/117579560-700cdd00-b0c1-11eb-8517-2a553bea605a.gif)

Users can also filter images based on the category they gave them

![Yearview (4)](https://user-images.githubusercontent.com/69891859/117579834-c0386f00-b0c2-11eb-890e-d12401626745.gif)

Clicking on an image will allow you to see it's information such as: description, category and the day it was added. You will also be able to delete the image from the repository

![Yearview (5)](https://user-images.githubusercontent.com/69891859/117580020-ce3abf80-b0c3-11eb-975f-65807c6ab53d.gif)

## Testing/Security

Unit tests are contained within the app_tests.py and monthblock_tests.py files and for security as mentioned before, all passwords, images and delete operations are encrypted  allowing full saftey to anyone who may be in concern.

















