
<p align="center"><img src="https://github.com/amithkk/Minerva/raw/master/logo_transparent.png" alt="Minerva Logo" width="250"/>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)</p>

---

Django based research paper and literature management system CMS for colleges written with an Angular Student Frontend and support for email notifications. This repository contains the open source administration backend and student research paper view

## Features
 - Ability to sort, filter, index, bulk import and export research papers/publications with Author Tracking
 - Individual administration for authors for their own publications
 - Export statistics for papers 
 - Email notifications and automatic author account creation on making a publication.
 - APIs for plugins for potential integration into aggregators such as IEEE
 
## Installation
 - Setup virtualenv with your enviroment manager of choice
 - Setup database configuration in `settings.py`, uses SQLite by default. Certain queries might not work without a Postgres db attached
 - Migrate DB with `manage.py syncdb`
 - Launch development server using `manage.py runserver`
 - \[OPTIONAL\] Setup nginx with `uwsgi` for running this in productions. Detailed instructions are given on [USWGI's Page](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
 
 ## See it in action!
  [Demo Server](http://demo.amithkk.com/minerva) ![](https://img.shields.io/badge/webapp-down-red.svg)
  
  
 ## One Click Deploy
  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) (soon)
