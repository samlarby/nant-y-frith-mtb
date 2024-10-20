# Nanny Trail Tribe
## Introduction
The purpose of this website is for users to be able to find out more information about the mountain biking club calle Nanny Trail Tribe. Users will be able to find out basic information about the team behind the club and who helps maintain the trails. To be able to view the trails and found out the locations and descriptions of the trails the users will have to pay a yearly membership. The site will also have a shop selling club merchandise. 


![Mock up image](documentation/readme/)

## Features 
* Navigation bar
    * A simple navigation bar is at the top of the page for users to easily go through. 

![Navigation bar](documentation/readme/navbar.jpg)

* Home page
    * 
    * 

![Home page](documentation/readme/home-page.jpg)

* Login page
    * 

![Login page](documentation/readme/login-page.jpg)

* Register page
    *  

![Register page](documentation/readme/register-page.jpg)


## User Experience

### First time visitors
* As a first time visitor I want to understand what the website is about.
* I want to learn a bit about the Nant Y Frith location and what it has to offer.
* I should be able to create an account for next time that I come back.
### Second time visitors
* On my second visit I should be able to log into my account  and view my profile.
* On viewing my profile it should show my subscription status.
* I should know by now that if I want to learn about trail locations and information I have to subscribe.
* Once subscribed I should be able to view all the trails information. 

### Design Choices
* Colour Scheme
    * The colours used on this page were used as they are forest and natural colours which I believe work well with the theme of the website. 
    
* Typography
    * The font used was Roboto, with sans-serif set as a back up font. Roboto was used as it has an easy readibility and has a clean and modern design.
   
* Imagery
    * The homepage image was taken by myself in the nant y frith woods. All other images used are acknowledged in the acknowledgements section.

    
### Flow chart
* Here is a flow chart of how I wanted the website to work. [Flowchart](documentation/readme/basic-flowchart.jpg)


### Wireframes
* All wireframes were created using Balsamiq wireframes, all designs for desktop are shown and one of the mobile as the only thing to change on small screens is the navbar as you can see [here](documentation/readme/milestone-project-4.png)

## Database design

### Testing
#### Functional Testing

### Validator testing
* PEP 8 Online
    * This validator Service was used to validate the python file in the project to ensure there were no syntax errors in the project. The results were all clear as shown below. 
    <details>
        <summary>PEP 8</summary>
        ![PEP 8](documentation/readme/pep8-validation.jpg "PEP8")
    </details>

* All webpages were tested using lighthouse and all performed to a passable level for performance, accessability, best practises and SEO for both mobile and desktop screen sizes.

### Testing User Stories

* First time visitor goals

* Second time visitor goals

* Future visitor goals
    
## Bugs Found
### Deployment bug to heroku loading static files 
* A bug found whilst deploying to heroku was that the static files werent loading. To fix this I changed the django to django 4.2. Also on my AWS i removed the getobjects from action i the bucket policy. 


## Deployment 
### **Heroku**

This application was built using the Gitpod IDE and deployed via Heroku. Follow these instructions to recreate the deployment process:

**1. Prepare the required files**

In the terminal in your code editor, type:

```
pip3 freeze --local > requirements.txt
```

and then...

```
echo web: python app.py > Procfile
```

These commands create two new files in your root directory which Heroku needs to run the application. Ensure Procfile includes a capital P and there is no file extension. Please check your Procfile and remove the last blank line if there is one, to avoid problems when trying to run your app.

**2. Create the app**

- Go to [Heroku](https://heroku.com/) and login to your account.
- Click 'New' and then 'Create new app'.
- Choose an app name and the region closest to you.

**3. Linking to GitHub**

- Within the deployment method, click 'GitHub'
- With your GitHub profile selected, type in your repo name and then search.
- Once found, click connect.

**4. Environment variables**

- Click on 'Settings' and then 'Reveal Config Vars'.
- Add the required key/value variables from your env.py file.

| Key          | Value              |
| ------------ | ------------------ |
| IP           | 0.0.0.0            |
| PORT         | 5000               |
| SECRET_KEY   | YOUR_SECRET_KEY*   |
| MONGO_URI    | YOUR_MONGO_URI*    |
| MONGO_DBNAME | YOUR_MONGO_DBNAME* |

Values with * are your own values to be created.

**5. Deployment**

- Ensure your two files in step 1 are pushed to GitHub.
- Within the 'Deploy' tab of your Heroku app, click 'Enable Automatic Deploys'
- Just below this, click 'Deploy Branch'.
- Within a few minutes, Heroku should confirm your app has been deployed with a button to view it online.   

   
## Credits
### Image Credits
* Pictures on the trails page are from https://www.freepik.com/ and the attribute is Wirestock, also
https://www.pexels.com with attributes lum3n, Oleksandr P, Lukas Hartmann, Photo by Tyler Lastovich, Anastasia Shuraeva
### Resources used

### Acknowledgements
* I would like to thank my mentor Okwudiri Okoro for their support.
* Also thank you to the slack community. 
* Icons were taken from <https://fontawesome.com/>
* Font was from <https://fonts.google.com/>

* With help to create the javascript I used materialize. Creating the app.py i Used the Code Instittue mini project and also w3 schools and stackoverflow.

* Creating the allauth accounts verification and the base.html main template I used the boutique_ado walk through.

Bugs



Acknowledgments
