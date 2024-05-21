from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_connection_config import db_config


class DatabaseConnect:
    engine = create_engine(
        f'mysql+mysqlconnector://{db_config.login}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()
