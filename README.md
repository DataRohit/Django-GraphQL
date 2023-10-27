# Django Rest Framework Course

## Overview
This is a comprehensive Django - GraphQL course that takes covers full CRUD functionality with JWT Authentication. You can follow the commits in this repository sequentially to see all the changes made step by step to achieve the full functionality of the GraphQL API.

## Project Details
**Project Hosting:** Vercel [here](https://django-graph-ql.vercel.app/)

**Database:** Initially uses sqlite3 (recommended for beginners), later integrated with Postgres.

**Credits:** The project is based on the course provided by
 - [Very Academy](https://www.youtube.com/@veryacademy)

## Django Apps and Features
 - [***restapi***](https://django-graph-ql.vercel.app/restapi/)
   - Returns a simple json message

 - [***books***](https://django-graph-ql.vercel.app/books/)
   - Query Books
   - Filter Books

 - [***quiz***](https://django-graph-ql.vercel.app/quiz/)
   - CRUD Quiz Categories
   - Query - Category, Quiz, Questions and Answers
   - Filter - Category, Quiz, Questions and Answers

 - [***users***](https://django-graph-ql.vercel.app/users/)
   - Register User
   - Verify User
   - Authenticate User
   - Send Re-Verification Email
   - Send Password Rest Email

# Requirements

   - aniso8601==9.0.1
   - asgiref==3.7.2
   - certifi==2023.7.22
   - charset-normalizer==3.3.1
   - Django==4.1.12
   - django-cors-headers==4.3.0
   - django-filter==23.3
   - django-graphql-jwt==0.4.0
   - graphene==3.3
   - graphene-django==3.1.5
   - graphql-core==3.2.3
   - graphql-relay==3.2.0
   - idna==3.4
   - promise==2.3
   - psycopg2-binary==2.9.9
   - PyJWT==2.8.0
   - python-dotenv==1.0.0
   - requests==2.31.0
   - six==1.16.0
   - sqlparse==0.2.4
   - text-unidecode==1.3
   - urllib3==2.0.7
   - whitenoise==6.6.0

All the above metioned packages are listed in [requirements.txt](https://github.com/DataRohit/Django-GraphQL/blob/main/requirements.txt) file.

# Concepts Covered
 - Simple JSON Web Response
 - Custom User Model
 - GraphQL Schema
 - GraphQL Mutations
 - GraphQL Connection Fields
 - GraphQL Auth
 - JWT Integration
 - Postgres Integration