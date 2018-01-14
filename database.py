from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FeatureRequests(Base):
    __tablename__ = 'features'
    
    feature_id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable = False)
    description = Column(String(250))
    client = Column(String(8), nullable = False)
    client_priority = Column(Integer, nullable = False)
    target_date = Column(Date)
    product_area = Column(String(8))


db = create_engine('sqlite:///featurerequests.db')
Base.metadata.create_all(db)
