from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Resume',
        'DENYS YATSENKO \n'
        '+380631301236 \n'
        'TELEGRAM - @denysyatsenko \n'
        'GitHub - https://github.com/denysyatsenko228 \n'
        'PROFILE \n'
        'I am energetic, stress-resistant and communicative.'
        'I love Python and have been working with language for almost a year now. '
        'I am passionate about programming, ready to solve emerging problems and develop in this.\n'
        'EXPERIENCE \n'
        '1. Created a Python course on Moodle \n'
        '2. Websites scraping experience \n'
        '3. Experience in creating online stores using Django \n'
        '4. Created mini games in Python \n'
        'EDUCATION \n'
        '3rd year student of Telecommunications NATIONAL TECHNICAL UNIVERSITY OF UKRAINE '
        '"IGOR SIKORSKY KYIV POLYTECHNIC INSTITUTE" | 2018 - Now'
        'SKILLS \n'
        'I have experience working with Python and the Django framework \n'
        'Basic knowledge of HTML, CSS and JS \n'
        'GIT, PostgreSQL \n'
        'Knowledge of OOP principles \n'
        'User Interface understanding \n'
        'Self Motivated \n'
        'Strong Communication Skills \n'
        'Extremely organized \n'
        'Knowledge of basic algorithms in python \n'
        'English(B2 UPPER INTERMEDIATE) \n',
        'dayyz2000@gmail.com',
        [user_email],
        fail_silently=False
    )