Launchpad Profiles
==================

Launchpad Profiles is an application for students to build a professional skills profile to aid in professional and academic development. It provides a system for tracking development of several branches of professional skillsets, such as Marketing, Entrepreneurship, and Networking. Students recieve badges to track their prograss and growth, and can recieve recommendatations and acknowledgment from superiors and mentors right on the site.

The application also provides ways for students to organize a portfolio of various professional skills, from writing, to design and art, to leadership and networking. They can share their progress on several connected social networks, such as Twitter and Facebook.

## Setup and Build Process ##

1. Clone the [project](https://github.com/brebory/launchpad-profiles) and set up a virtualenv in the project directory. `virtualenv env --no-site-packages`
2. Use the newly created virtualenv to install all dependencies. `source env/bin/activate` then `pip install -r requirements.txt` Pip will download and install all required dependencies into your virtual environment.
3. Set up the database. In development, `sqlite3` is used. In production, `postgresql` is used. Run `python manage.py syncdb` for the initial database setup, and then migrate all required apps. `syncdb` will tell you which apps need to be migrated with `python manage.py migrate [appname]`. 
4. Run the application with `python manage.py runserver`

## Git Branching Model and Development Process ##

Always create a feature branch to work on new features. `git checkout -tb [feature-branch-name]` 
Do not work directly on master or develop. Merge branches back in to develop once they're in a stable state for testing. Merge develop back into master once sufficient testing is done on develop.
Write unit tests! Use the `unittest` module to make sure that all aspects of features are working before you merge back into develop.

## Issues and Code Review ## 

We'll be using Github Issues as our management system for code reviews and bug tracking. Participate in the discussion around each issues to raise any questions and concerns you may have about specific features or to discuss bugfixes.

## Design Contacts ##

Signum Design is handling the design and illustration assets involved. Try to use CSS to style as much as possible, without resorting to background images. Any illustrations needed should be submitted as a work request to Kate for Signum to complete.

Kate's email: [kharmon9@kent.edu](mailto:kharmon9@kent.edu)
Signum's email: [signumdesignksu@gmail.com](mailto:signumdesignksu@gmail.com)
