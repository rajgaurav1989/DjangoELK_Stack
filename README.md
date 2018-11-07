# DjangoELK_Stack

prerequisite : -

1. install pip
2. install elasticsearch
3. install logstash
4. install kibana 
5. pip install virtualenv


steps to Run : - 

1. brew services start elasticsearch
2. brew services start kibana
3. git clone git@github.com:rajgaurav1989/DjangoELK_Stack.git
4. cd DjangoELK_Stack
5. virtualenv venv
6. source venv/bin/activate
7. pip install -r requirements.txt
8. /usr/local/bin/logstash -f ./logstash.conf 
8. python manange.py runserver
9. open browser goto http://localhost:8000/admin/
10. username : 'raj'  password: 'raj'   
11. create a superuser from ui with properemailId, as it will be used to get your confirmation mail
12. logout from credentials
13. configure ADMIN_EMAIL_PASSWORD, CRON_EMAIL_PASSWORD,CRON_EMAIL in ELK_App/settings.py
14. login with you credentials
15. test the app


Steps to run optional task : -

1. sudo chmod u+x mycron.py
2. crontab -e
3. */1 * * * * /usr/bin/python /path/to/mycron.py
