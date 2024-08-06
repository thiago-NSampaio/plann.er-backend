from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///storage.db', echo=True)

Base = declarative_base()


class Trip(Base):
    __tablename__ = 'trips'
    id = Column(String, primary_key=True)
    destination = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    owner_name = Column(String)
    owner_email = Column(String)
    status = Column(String, nullable=True)


class EmailToInvite(Base):
    __tablename__ = 'emails_to_invite'
    id = Column(String, primary_key=True)
    trip_id = Column(String, ForeignKey('trips.id'))
    email = Column(String, nullable=False)


class Link(Base):
    __tablename__ = 'links'
    id = Column(String, primary_key=True)
    trip_id = Column(String, ForeignKey('trips.id'))
    link = Column(String, nullable=False)
    title = Column(String, nullable=False)


class Participant(Base):
    __tablename__ = 'participants'
    id = Column(String, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'), nullable=False)
    emails_to_invite_id = Column(Integer, ForeignKey(
        'emails_to_invite.id'), nullable=False)
    name = Column(String, nullable=False)
    is_confirmed = Column(Integer)


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(String, primary_key=True)
    trip_id = Column(String, ForeignKey('trips.id'), nullable=False)
    title = Column(String, nullable=False)
    occurs_at = Column(DateTime)


class InitDB:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)
