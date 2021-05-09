# YearView (Shopify Fall 2021 Backend Dev Challenge)

![Yearview](https://user-images.githubusercontent.com/69891859/117560163-5df75400-b059-11eb-81bb-a84ebec9cbed.gif)


You can check out a full demo of the project [here](https://www.youtube.com/watch?v=iAI6MHgDDDA)

Or go [here](https://www.youtube.com/watch?v=2wQqpM33VCY) if you want to save a few minutes of cringe...

## What is it/Inspiration

YearView is a secure photo storage app that allows one to keep track of their photos and reminisce upon the memories they made throughout the year.

Have you ever looked back and thought damn New Years was just last week, but you wake up and it's the start of fricking May?! What happened in between?? Well, with YearView, you will be able to see what you did in all those months and realize all that you have accomplished!

## Features

- Add pictures 1 by 1 or in bulk with multiple file formats
- Delete pictures
- Search/filter pictures by common characteristics
- Securly upload/delete pictures
- A month view that allows you to see the pictures you added in each month
- Secure Login/Account Creation mechanism

## Endpoints

|Endpoint | Use |
|---------|-----|
|/        | Landing page where user can enter login credentials and enter the app|
|/signup  | Page where user can create an account and set up their username, password and name |
|/check   | Once user enters login credentials, they get tested with the data in Mongo to ensure the correct person is accessing this account|
|/user    | Once user is successfully logged in, they will be able to use all features of app and upload pictures|
|/user/add-image| Endpoint where user can upload a picture and assign values to it such as: description, category etc.|
|/user/[image-key]| Retrieves an image based on the key to display to the user |
|/user/month/[month-name] | User can see all the pictures they added in a certain month |
|user/image/info/[image-key] | User can see the information about a specific image such as: description, category and the date it was added |
|user/image/delete/[image-key]| Deletes an image corresponding to its specific key |
|/user/filter/[image_filter] | Switches the category of the filter |
|/signout | Signs the user out of the app |




