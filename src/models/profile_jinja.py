from jinja2 import Environment, FileSystemLoader
from fastapi import Cookie

async def get_data_profile(data_users):
    env = Environment(loader = FileSystemLoader(r'templates'))
    template1 = env.get_template('profile_j_style.jinja')
    template2 = env.get_template('profile_j.jinja')

    with open(file="templates/profile.html", mode='w', encoding="utf-8") as f:
        print(template1.render(), file=f)
        
        f.writelines("    <link href=\"{{ url_for('style_profile', path='/style_profile.css') }}\" rel=\"stylesheet\">")
        
        print(template2.render(profile_info = data_users), file=f)
        
    return True

async def get_data_edit_profile(data_users):
    env = Environment(loader = FileSystemLoader(r'templates'))
    template1 = env.get_template('profile_edit_style.jinja')
    template2 = env.get_template('profile_edit.jinja')
    
    with open(file="templates/menu_profile/edit_profile.html", mode='w', encoding="utf-8") as f:
        print(template1.render(), file=f)
        
        f.writelines("    <link href=\"{{ url_for('style_edit_profile', path='/style_edit_profile.css') }}\" rel=\"stylesheet\">")
        
        print(template2.render(profile_info= data_users), file=f)