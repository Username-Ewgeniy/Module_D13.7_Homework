 <!--Проверка отправки из почты в shell  -->

<!-- py manage.py shell  --> 

from django.core.mail import send_mail

send_mail(
    'Test Subject',
    'Test message body',
    'EMAIL_HOST_USER',
    ['EMAIL_ADMIN'],
    fail_silently=False,
)
<!-- >>>1 т.е. True  --> 



<!-- файл .env -->

EMAIL_HOST_USER = ea.webportal
EMAIL_HOST_PASSWORD = <!--!!! пароль для приложения в яндекс id !!! -->
EMAIL_ADMIN = ea.webportal@yandex.ru
EMAIL_SERVER = ea.webportal@yandex.ru
DEFAULT_FROM_EMAIL = ea.webportal@yandex.ru



<!-- requirements.txt  -->

pip freeze > requirements.txt 
pip install -r requirements.txt