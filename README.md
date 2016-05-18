# pingApp
This is a simple Django Web Application that allows you to ping multiple hosts at once, to check whether they are reachable from your system or not. The results are displayed in an HTML table. By default, the values are updated every two seconds, but you can change it according to your own needs.
You must have Python and Django installed on your system. As an example, I added 3 hosts, but you can change them by modifying the addresses list in mainApp/views.py file.

#Running the application:
Browse to the project folder in your terminal and type:
python manage.py runserver

Then open your web browser and go to the following address:
localhost:8000/

Here is a screenshot of the app running in Chromium Browser in Ubuntu:

![alt tag](https://github.com/nikssardana/pingApp/blob/master/screenshot.png)

