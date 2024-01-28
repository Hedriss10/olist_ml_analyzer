"""
    RefractorSQL é feito para manipular os arquivos .csv que contem na pasta data do diretorio
    Basicamente ele irá processar os dados de forma rápida contendo boas paticas de desenvolvimento
    de engenharia de dados básicas é isso mesmo irei transformar os dados para .sql
    O sgdb que iremos utilizar para poder fazer o insert do arquivos é o postgreSQL 
    E finalizaremos o projeto lá 
"""

import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
from tqdm import tqdm

# Carregamento das variáveis de ambiente
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

load_dotenv(dotenv_path)

USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
HOSTNAME = os.environ.get("HOST_NAME")
PORT = os.environ.get("PORT")
DATABASE = os.environ.get("DATABASE")

class ExploreArquiveFolder:
    def explore_arquive(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder_database = os.path.join(path, 'database')
        return folder_database
    
    def csv_files(self):
        csv = [f for f in os.listdir(self.explore_arquive()) if f.endswith('.csv')]   
        return csv 

class ConfigDB:
    db_config = {
        'user': USER_NAME,
        'password': PASSWORD,
        'host': HOSTNAME,
        'port': PORT,
        'database': DATABASE,
    }

    def create_connection(self, db_config=db_config):
        
        try :
            
            if None in db_config.values():
                raise ValueError("Alguma variável de ambiente não foi definida corretamente.")

            port = str(db_config['port']) if db_config['port'] is not None else '5432' # passando a conexão padrão 
            self.engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{port}/{db_config['database']}")
            return self.engine

        except (OperationalError) as e:
            print(f"{e} -> Não existe um o banco olist dentro do postgresql.")

    def exit_engine(self):
        self.engine.dispose()

class InserDBPg:        
    def insert(self, csv_files, csv_directory, engine):
        for csv_file in tqdm(csv_files, desc="Inserindo no PostgreSQL"):
            df = pd.read_csv(os.path.join(csv_directory, csv_file))
            
            table_name = csv_file.split(".")[0]    
            df.to_sql(table_name, engine, index=False, if_exists="replace")

if __name__ == "__main__":
    explore_folder = ExploreArquiveFolder()
    csv_files_list = explore_folder.csv_files()
    config_db = ConfigDB()
    db_engine = config_db.create_connection()
    inserter = InserDBPg()
    inserter.insert(csv_files_list, explore_folder.explore_arquive(), db_engine)
    config_db.exit_engine()
    print("Inserção no PostgreSQL concluída com sucesso.")
