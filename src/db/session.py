import psycopg2

from psycopg2 import Error, InterfaceError
from core.config import config


class DataBaseUsers():
    
    connection = psycopg2.connect(
        host=config.POSTGRESQL_HOST.get_secret_value(),
        database=config.POSTGRESQL_DATABASE.get_secret_value(),
        user=config.POSTGRESQL_USER.get_secret_value(),
        password=config.POSTGRESQL_PASSWORD.get_secret_value(),
        port = config.POSTGRESQL_PORT.get_secret_value()
    )
    
    cursor = connection.cursor()
    
    async def user_check(self, login_id: int):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    
                    check_users = f"SELECT login_id FROM public.web_place_users WHERE login_id = {login_id};"
                    cursor.execute(check_users)
                    connect.commit()
                    check_users = cursor.fetchall()
                    
                    check_users_pay = f"SELECT balance FROM public.place_users_balance WHERE login_id = {login_id};"
                    cursor.execute(check_users_pay)
                    connect.commit()
                    check_users_pay = cursor.fetchall()
                    
                    if check_users and check_users_pay:
                        return False
                    else:
                        return True
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка проверки пользователя в БД!", login_id)
    
    async def user_add_login_id(self, login_id: int):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    
                    add_users = f"INSERT INTO public.web_place_users (login_id) VALUES ({login_id});"
                    cursor.execute(add_users)
                    connect.commit()
            
            return True
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка добавления логина пользователя!", login_id)
            
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    
                    add_users_balance = f"INSERT INTO public.place_users_balance (login_id, balance) VALUES ({login_id}, {0});"
                    cursor.execute(add_users_balance)
                    connect.commit()
            
            return True
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка добавления баланса пользователя!", login_id)
    
    async def user_full_add(self, login_id: int, name: str, age: int, gender: str, city: str, about: str, hobbies: str):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    update_user = f"UPDATE public.web_place_users SET (name, age, gender, city, about, hobbies) = ('{name}', {age}, '{gender}', '{city}','{about}', '{hobbies}') WHERE login_id = {login_id};"
                    cursor.execute(update_user)
                    connect.commit()
            
            return True
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка добавления данных пользователя!", login_id)
            
    async def user_data(self, login_id: int):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    data_user = f"SELECT * FROM public.web_place_users WHERE login_id = {login_id}"
                    cursor.execute(data_user)
                    connect.commit()
                    ds = list(cursor.fetchall()[0])
                    
                    if ds[1] is None:
                        ds[1] = "-"
                    
                    if ds[2] is None:
                        ds[2] = 0
                    
                    if ds[3] is None:
                        ds[3] = "Другой"
                        
                    if ds[4] is None:
                        ds[4] = "-"
                        
                    if ds[5] is None:
                        ds[5] = "-"
                        
                    if ds[6] is None:
                        ds[6] = "-"
                    
                        
                    users = {
                        "id": ds[0],
                        "name": ds[1],
                        "age": ds[2],
                        "gender": ds[3],
                        "city": ds[4],
                        "about_me": ds[5],
                        "hobbies": ds[6]
                    }
            
            return users
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка данных пользователя!", login_id)
            
            
class UserAuth():
    
    connection = psycopg2.connect(
        host=config.POSTGRESQL_HOST.get_secret_value(),
        database=config.POSTGRESQL_DATABASE.get_secret_value(),
        user=config.POSTGRESQL_USER.get_secret_value(),
        password=config.POSTGRESQL_PASSWORD.get_secret_value(),
        port = config.POSTGRESQL_PORT.get_secret_value()
    )
    
    cursor = connection.cursor()
    
    async def check_auth_user(self, login_id: int, password: str):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    
                    user_auth = f"SELECT * FROM public.place_users_account WHERE login_id = {login_id} and password = '{password}';"
                    cursor.execute(user_auth)
                    connect.commit()
                    user_auth = cursor.fetchall()

                    flag = True
                    
                    if user_auth:
                        pass
                    else:
                        flag = False
                        
                    return flag
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка проверки пользователя в БД!", login_id)
            

class UserPay():
            
    connection = psycopg2.connect(
        host=config.POSTGRESQL_HOST.get_secret_value(),
        database=config.POSTGRESQL_DATABASE.get_secret_value(),
        user=config.POSTGRESQL_USER.get_secret_value(),
        password=config.POSTGRESQL_PASSWORD.get_secret_value(),
        port = config.POSTGRESQL_PORT.get_secret_value()
    )
    
    cursor = connection.cursor()
    
    async def user_balance(self, login_id: int):
        
        try:
            with self.connection as connect:
                with connect.cursor() as cursor:
                    
                    user_pay = f"SELECT balance FROM public.place_users_balance WHERE login_id = {login_id};"
                    cursor.execute(user_pay)
                    connect.commit()
                    user_pay = cursor.fetchall()[0][0]
                    
                    user = {
                        "balance": user_pay
                    }
                    
            return user
            
        except (InterfaceError, Error) as error:
            print(error, "Ошибка проверки баланса пользователя в БД!", login_id)