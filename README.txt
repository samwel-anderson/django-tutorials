
1. Add packages from requirments.txt
2. To add packages
    pip freeze > requirements.txt

3. To import packages
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

4. Start App in a specific folder
    a) FIRST CREATE A folder Apps/calvinapp
    b) python manage.py startapp calvinapp ./Apps/calvinapp
    c) modify name in Apps/calvinapp/apps.py from
     name = 'calvinapp' to
     name = 'Apps.calvinapp'
    d) declare app in "INSTALLED_APPS" as 'Apps.calvinapp'



5. Using DRF (Django Rest Framework)
    https://www.django-rest-framework.org/
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support

6. Using Viewset API
    https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/

7. Installing Swagger documentation from "https://github.com/axnsan12/drf-yasg"
    pip install -U drf-yasg
    add 'drf_yasg' in INSTALLED_APPS
    configure schema_view in urls.py

8. Using Generic Based Views
    https://www.cdrf.co/
    https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/views-and-generic-views.html
    https://realpython.com/django-rest-framework-class-based-views/
    https://medium.com/analytics-vidhya/django-rest-framework-generic-views-using-parameters-in-the-url-with-the-query-fd61eba85f4
    http://www.tomchristie.com/rest-framework-2-docs/api-guide/generic-views
    https://www.django-rest-framework.org/tutorial/3-class-based-views/

