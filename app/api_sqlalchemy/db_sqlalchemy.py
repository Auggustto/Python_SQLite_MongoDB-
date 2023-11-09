from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Client(Base):
    __tablename__ = "customer_account"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(Integer, nullable=False, unique=True)
    address = Column(String, nullable=False)

    account = relationship("Account", back_populates="client")

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    type_account = Column(String, server_default='basic')
    agency = Column(Integer)

    user_id = Column(Integer, ForeignKey("customer_account.id"), nullable=False)
    client = relationship("Client", back_populates="account")

engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

