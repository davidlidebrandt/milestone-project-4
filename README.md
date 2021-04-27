# 

<img src=""
     alt=""
     style="height: 100px; width: 200px;" />
     
<img src=""
     alt=""
     style="height: 100px; width: 200px;" />

<img src=""
     alt=""
     style="height: 100px; width: 200px;" />

<img src=""
     alt=""
     style="height: 100px; width: 200px;" />

This project intends to create a basic (fictional) store that sells fitness equipment both on the web and in physical stores.
By providing the user with the opportunity to purchase relevant equipment through a smooth user experience 
the store looks to attract both new and revisiting customers.


[Link to the deployed project](https://fitness-equipment.herokuapp.com/)

# Table Of Contents


* [UX](#ux)
* [Features](#features)
* [Database](#database)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## UX

The main purpose of the project is to create a fullstack website using the python Django web framework. The site is intended to mimic a 
simple but working site for a company that sells fitness equipment both online and in physical stores. The main targeted customers would
be people looking to buy fitness equipment for home use, which is particularly relevant in the current situation.

The purpose for the developer is to showcase proficiency in working with the Django framework and building an application using the MVC 
pattern. The project includes use of the built in Django authentication system in conjunction with the added Django allauth package for handling
all user authentication. The project includes a fair bit of custom Python, JavaScript and CSS code which intends to showcase proficiency in
those languages. As means of payment the Stripe platform has been integrated in to the project and on the frontend JQuery and Bootstrap has 
been used which displays an ability to work with external libraries.

As the size of the project is quite small all custom static files are hosted on the same platform as the Django project itself using the 
WhiteNoise package. In a larger project this would not be advisable and the use of a cloud storage provider such as Amazon's S3 would be 
more appropriate but would also require entering of credit card details as that service is not free of charge after a certain 
threshold.


### Design

The design of the project has been kept fairly simple with a navigation bar in the top and a footer in the bottom which looks the same across 
all pages as well as a main window which looks similar across the pages.

Some inspiration for the design of the site was taken from [Gymgrossisten](https://www.gymgrossisten.com/) ,a swedish company's site who sell supplements and fitness equipment.

The two main colors used are black and a lighter green (#a5d6a7) with a darker green (#4caf50) when hovering over certain elements. The two main colors
provides clear contrast and makes it easy to read and distinguish different elements.

The font chosen for the project is Montserrat with a fallback of sans-serif, the font looks clear yet modern which fits well with the purpose of the site.



### User Stories

#### Regular user 
 
 * As a user I want to easily find relevant equipment so that I can compare and purchase any products I choose.

 * As a user I want to be able to see my current items in my shopping bag/chart and the total prize so that I 
 can keep track of how much I am spending.

 * As a user I want to be able to easily add and remove items from my shopping bag/chart so that I get exactly
 what I want without having to restart the process.

 * As a user I want to be notified before and after any important actions are taken so that I do not accidentally
 perform some unwanted action.

 * As a user I want the navigation on the site to be consistent and easy to understand so that I do not spend 
 unnecessary time trying to access different content.

* As a user I want the checkout and payment process to be clear and fast so that I do not spend time and effort 
on tasks that decrease positive experience of the site.

* As a user I want conformation of any orders and payments so that I can keep track of what I have ordered.

* As a user I want to be able to read reviews and ratings of products from other users so that I can decide
if it is worth buying.

* As a user I want to be able to sign up to save my contact details for an even faster
and smoother checkout and overall user experience.

* As a user I want the sign up process to be fast, smooth and easy to understand so that I quickly get access to
the features provided.

#### Logged in/Signed up user

* When signing up I want to confirm my email address to ensure my email is connected to my account.

* As a logged in user I want to easily be able to edit my profile contact and credit card details incase that
is needed.

* As a logged in user I want to be able to write my own reviews and add ratings on the products on the page.



#### Wireframes and Mockups

* [Wireframe Mobile](static/images/wireframes-mockups/wireframe-mobile.png)
* [Wireframe Tablet](static/images/wireframes-mockups/wireframe-tablet.png)
* [Wireframe Desktop](static/images/wireframes-mockups/wireframe-desktop.png)

* [Mockup Mobile](static/images/wireframes-mockups/mockup-mobile.png)
* [Mockup Tablet](static/images/wireframes-mockups/mockup-tablet.png)
* [Mockup Desktop](static/images/wireframes-mockups/mockup-desktop.png)


## Database

All models and data are stored via relational SQL databases in this project, in development the built in to Django SQlite database will
be used and in production a PostgreSQL database will be used.

The models that will be stored in the database are:

* Order 

* OrderItem

* Store

* Product 

* Category 

* Manufacturer 

* Review 


### Order fields

* id 
* date
* amount_paid
* shipping_address
* customer_name
* customer_email
* user: foreign key User, optional 


### OrderItem fields

* product: foreign key Product
* order: foreign key Order
* quantity


### Product fields

* name
* description
* image_url: optional
* category: foreign key Category
* manufacturer: foreign key Manufacturer
* prize
* discount_rate: foreign key Discount, optional
* units_sold 

### Category 

* name
* image_url

### Manufacturer

* name

### Review 

* by_user: foreign key User
* product: foreign key Product
* description
* rating

### Store

* name
* city
* address
* phone_number
* open_hours



## Features

### Existing Features





### Future Features




## Technologies Used

* HTML

For the basic structure of the web page.

* CSS

For the styling of the HTML elements.

* JavaScript

To add interactivity to the project.

* [Django](https://www.djangoproject.com/)

Django was the backend web framework used to handle all backend processes such as interactions with the
database, authentication and rendering of HTML templates and more.

* [Python](https://www.python.org/)

Custom Python code was written in conjunction with Django to handle all of the backend processes.

* [PostgreSQL](https://www.postgresql.org/)

PostgreSQL was the database used to store all the models in the production environment. All interactions with the database
was handled through the Django Object-Relational Mapper (ORM) and no raw SQL queries where made.

* [SQlite](https://www.sqlite.org/index.html)

The Django preinstalled SQlite database was used as the database in the development environment. As with the production PostgreSQL 
database all interactions where made through the Django ORM.

* [JQuery](https://jquery.com/)

JQuery functions where used to manipulate the DOM, take actions and to make AJAX calls.

* [Bootstrap](https://getbootstrap.com/)

Bootstrap was used to provide structure and responsiveness to the site by using their container
, row, offset and col classes. Helper classes for margin, padding, font weight and text transform such
as their m, p, fw, text-uppercase classes where heavily used throughout the project to speed up the
front end development. A navbar and some dropdown elements where components included in the project.

*[Stripe](https://stripe.com/)

Stripe was used to handle all payments on the site.

* [Github](https://github.com/)

Github was used to store the repository.

* [Gitpod](https://www.gitpod.io/)

Gitpod was the IDE used to create the project.

* [Git](https://git-scm.com/) 

For version control through the Gitpod terminal.

* [Adobe XD](https://www.adobe.com/products/xd.html)

Adobe XD was used to create the wireframes and mockups for the project.

* [Materialize](https://materializecss.com/)

Materialize was not used directly in the project but the colors were chosen by using their color palette.

* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

Chrome DevTools was heavily used throughout the project,  mainly by debugging and testing with help of the console and
checking the responsiveness of the page with their screen rendering tools.

* http://whatismyscreenresolution.net/multi-screen-test 

For testing the responsiveness across different devices.



## Testing

* The CSS was run through the https://jigsaw.w3.org/css-validator/ without any errors found.

* The HTML was run through the https://validator.w3.org/, the errors that are found are all related to
the Django templating language. Since Django is creating HTML files by using templates and injecting variables
from the backend the validator gives errors that are not actually present at runtime.

* The JavaScript was run through the https://jshint.com/ linter, no errors found. Two warnings occur regarding 
unused variables, these can be ignored since these functions are used and called when submitting forms.

* The cornflakes(flake8) linter was installed as an extension to the development environment and validated
the Python code throughout the project.

* The responsiveness was tested by simulating a vide variety of devices such as phones, tablets and desktops using
the Chrome DevTools and http://whatismyscreenresolution.net/multi-screen-test. The sites look well down to 320 pixels
wide.

* The site was tested on three different browsers: Google Chrome, Mozilla Firefox and Microsoft Edge.


### Answering User Stories





## Deployment

### Publishing the project

The project was deployed on [Heroku](https://dashboard.heroku.com/), the following steps were taken:

1. Created a requirements.txt file by typing: "pip3 freeze --local > requirements.txt" in the terminal.
2. Created a procfile by typing echo web: "web: gunicorn fitness_equipment.wsgi > Procfile" in the terminal.
3. Logged in to Heroku.
4. Pressed the button "new" and then "create new app".
5. Chose an app name and a region and pressed create app.
6. Went to deployment section.
7. Under deployment method pressed Github.
8. Chose the right repository in the list, pressed search and then connect.
9. Pressed enable automatic deploys under automatic deploys.
10. Went to settings.
11. Added all the config vars needed for the project.
12. Pressed open app.


### Forking the project
1. Go to and log in to https://github.com/.
2. Go to the repository: https://github.com/davidlidebrandt/milestone-project-4
3. Press the fork button located on the right side.
4. Make your changes to the project.
5. If you wish to merge your changes to the original project:
6. Press the pull request button from your forked repository.
7. Press the button new pull request.
8. Choose the branches you wish to merge.
9. Press the Create pull request button.


### Cloning the project
There are several ways of cloning the project, here I am going to describe how to do it using
the URL and Git Bash.
1. Go to the repository: https://github.com/davidlidebrandt/milestone-project-4
2. Click the Code button.
3. Choose HTTPS and copy the link that is provided.
4. Open Git Bash and navigate to the directory where you want to save the cloned project.
5. Type git clone followed by the url you copied, git clone https://github.com/davidlidebrandt/milestone-project-3.git

## Credits 

### Content



### Media

Background image came from https://pixabay.com/sv/photos/hantel-idrott-vikter-gym-1966247/ by user Jonas_Fehre.

Favicon image came from https://pixabay.com/sv/vectors/skivst%C3%A5ng-vikt-pump-j%C3%A4rn-fitness-3573104/ by user b0red.

Main image on the index page came from https://pixabay.com/sv/photos/cross-fit-zimmer-h%C3%A4lsa-fitness-1126999/ by user GYMer_Jason 





### Acknowledgments

Thanks to my tutors and my mentor at Code Institute for help throughout the project.