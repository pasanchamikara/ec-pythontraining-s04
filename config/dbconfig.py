from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:127.0.0.1/testdb", echo=True, pool_size=6, max_overflow=10, encoding='latin1')
# engine = create_engine("mysql+pymysql://root:pass@localhost/mydb")

engine.connect()

print(engine)