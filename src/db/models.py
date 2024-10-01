import psycopg2

from psycopg2 import Error, InterfaceError
from ..core.config import config


class DataBaseUsers():
    
    connection = psycopg2.connect(
        host=config.POSTGRESQL_HOST.get_secret_value(),
        database=config.POSTGRESQL_DATABASE.get_secret_value(),
        user=config.POSTGRESQL_USER.get_secret_value(),
        password=config.POSTGRESQL_PASSWORD.get_secret_value(),
        port = config.POSTGRESQL_PORT.get_secret_value()
    )
    
    cursor = connection.cursor()

    async def sql_check_users(self, login_id):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    
                    check_users = f"SELECT login_id FROM public.web_place_users WHERE login_id = {login_id};"
                    cursor.execute(check_users)
                    connect.commit()
            
            flag = True
            
            if check_users:
                pass
            
            else:
                flag = False
                
            return flag
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка проверки пользователя в БД!", login_id)
    
    async def sql_users_add(self, login_id, name, age, gender, city, about, hobbies):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    
                    add_users = f"INSERT INTO public.web_place_users (login_id, name, age, gender, city, about, hobbies) VALUES ({login_id}, '{name}', {age}, '{gender}', '{city}','{about}', '{hobbies}');"
                    cursor.execute(add_users)
                    connect.commit()
            
            return True
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка добавления пользователя!", login_id)
