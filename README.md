Launchpad Profiles
==================

Launchpad Profiles is an application for students to build a professional skills profile to aid in professional and academic development. It provides a system for tracking development of several branches of professional skillsets, such as Marketing, Entrepreneurship, and Networking. Students recieve badges to track their prograss and growth, and can recieve recommendatations and acknowledgment from superiors and mentors right on the site.

The application also provides ways for students to organize a portfolio of various professional skills, from writing, to design and art, to leadership and networking. They can share their progress on several connected social networks, such as Twitter and Facebook.

## Table of Contents ##

1. [Setup and Build Process](#setup-and-build-process)
2. [Development Process (Backend)](#development-process-backend)
3. [Development Process (Frontend)](#development-process-frontend)

## Setup and Build Process ##

1. Install [python 2](http://www.python.org/getit/) if it's not already on your machine. Install pip, setuptools, and virtualenv. `easy_install setuptools`, `easy_install pip`, `pip install virtualenv`, in that order.
2. Clone the [project](https://github.com/brebory/launchpad-profiles) and set up a virtualenv in the project directory. `virtualenv env --no-site-packages`
3. Use the newly created virtualenv to install all dependencies. `source env/bin/activate` then `pip install -r requirements.txt` Pip will download and install all required dependencies into your virtual environment.
4. Set up environment variables.`export LOCAL_DEV=1`, `export DJANGO_SECRET_KEY={secret key}` (Set the secret key to a strong, long password.) It's recommended to write a bash script to handle this for you.
5. Set up the database. In development, `sqlite3` is used. In production, `postgresql` is used. Run `python manage.py syncdb` for the initial database setup, and then migrate all required apps. `syncdb` will tell you which apps need to be migrated with `python manage.py migrate [appname]`. 
6. Run the application with `python manage.py runserver`.
7. Return to your normal development environment with `deactivate`.

## Development Process (Backend) ##

### Git Branching Model and Development Process ###

* Always create a feature branch to work on new features. `git checkout -tb [feature-branch-name]` 
* Do not work directly on master or develop. Merge branches back in to develop once they're in a stable state for testing. Merge develop back into master once sufficient testing is done on develop.
* Write unit tests! Use the `unittest` module to make sure that all aspects of features are working before you merge back into develop.

### Issues and Code Review ###

We'll be using Github Issues as our management system for code reviews and bug tracking. Participate in the discussion around each issue to raise any questions and concerns you may have about specific features or to discuss bugfixes.

## Development Process (Frontend) ##

### SCSS and Compass ###

[Sass](http://sass-lang.com/) and [Compass](http://compass-style.org/) are reccomended for front-end development. They require [ruby](http://www.ruby-lang.org/en/) to be installed. You can get them with the rubygems package manager after installing ruby. Run `gem install sass` and `gem install compass` to get started.

### Design Contacts ###

Signum Design is handling the design and illustration assets involved. Try to use pure CSS to style as much as possible, without resorting to background images. Any illustrations needed should be submitted as a work request to Kate for Signum to complete.

* Kate's email: [kharmon9@kent.edu](mailto:kharmon9@kent.edu)
* Signum's email: [signumdesignksu@gmail.com](mailto:signumdesignksu@gmail.com)
