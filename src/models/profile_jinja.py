from jinja2 import Environment, FileSystemLoader

data_users = {
    "id": 1,
    "name": "Лёха",
    "sex": "муж.",
    "years": 22,
    "city": "Питер",
    "about_me": "Я обучаюсь в СПБГУТ им. Бонч-Бруевича на программную-инженерию! Программирую на Python и C++. Проходил различные онлайн курсы, как платные, так и бесплатные. Создаю различные приложения, тг-ботов, сайты и многое другое, что я считаю интересным!",
    "hobbies": "Python, git, github"
}

async def get_data_profile():
    env = Environment(loader = FileSystemLoader(r'templates'))
    template1 = env.get_template('profile_j_style.jinja')
    template2 = env.get_template('profile_j.jinja')

    with open("templates/profile.html", 'w', encoding="utf-8") as f:
        print(template1.render(), file=f)
        
        f.writelines("    <link href=\"{{ url_for('style_profile', path='/style_profile.css') }}\" rel=\"stylesheet\">")
        
        print(template2.render(profile_info = data_users), file=f)
        
    return True