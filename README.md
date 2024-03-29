
<p align="center"><img src="https://github.com/amithkk/Minerva/raw/master/logo_transparent.png" alt="Minerva Logo" width="250"/></p>
<p align="center"><a href="https://www.python.org/"><img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="Python Logo"/></a></p>



---

Django based research paper and literature CMS for colleges written with an Angular Student Frontend and support for email notifications. This repository contains the open source administration backend and student research paper view

## Features
 - Ability to sort, filter, index, bulk import and export research papers/publications with Author Tracking
 - Individual administration for authors for their own publications
 - Export statistics for papers 
 - Email notifications and automatic author account creation on making a publication.
 - APIs for plugins for potential integration into aggregators such as IEEE
 - Record attendances for conferences and other events
 - Create attendance reports
 
## Installation
 - Setup virtualenv with your enviroment manager of choice
 - Setup database configuration in `settings.py`, uses SQLite by default. Certain queries might not work without a Postgres db attached
 - Migrate DB with `manage.py syncdb`
 - Launch development server using `manage.py runserver`
 - \[OPTIONAL\] Setup nginx with `uwsgi` for running this in production. Detailed instructions are given on [USWGI's Page](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)


## Screenshots

![Login](https://github.com/amithkk/Minerva/raw/master/docs/login.png)
![Add Paper](https://github.com/amithkk/Minerva/raw/master/docs/addpaper.png)

---
Made with ❤ and ☕ by [Amith K K](https://amithkk.github.io)
