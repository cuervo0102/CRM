import logging


logging.basicConfig(level=logging.DEBUG)
user_login_handler = logging.FileHandler('logs/users_login.log')


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
user_login_handler.setFormatter(formatter)



logger = logging.getLogger(__name__)
logger.addHandler(user_login_handler)