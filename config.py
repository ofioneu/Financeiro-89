#Este arquivo será o responsável por dizer ao Python em que ambiente nosso projeto estará rodando, se ele estará em produção.

#Inicialmente teremos 3 subclasses, pois precisaremos rodar nosso projeto em 3 ambientes diferentes teste ou desenvolvimento. 

import os
import random, string

#superclasse chamada Config, cujas constantes são herdadas pelas subclasses
class Config(object):
    CSRF_ENABLED = True
    SECRET = 'ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:root@localhost:5432/financeiro_89'
    SENDGRID_API_KEY = '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'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    
    
#Anbiente de Development
class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
    

#Ambiente de Testing
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

#Ambiente de Production
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/login/' % (IP_HOST, PORT_HOST)


#Dicionario que inicializa os ambientes
app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

# app_active: ela receberá um dos três valores: development, testing e production. 
# #Esse valor será atribuído através de uma variável de ambiente, ou seja,poderemos trocá-lo dinamicamente.
# Usamos a função os.getenv  ('NOME_DA_CHAVE') para setar um valor a ela através da criação de uma variável 
#de ambiente que tenha o nome da chave que escolhermos
app_active = os.getenv('FLASK_ENV')