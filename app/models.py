from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///park.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    ___tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    email = Column(String(55))
    vehicles = relationship('Vehicle', back_populates='owner' )

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer(), primary_key=True)
    license_plate = Column(String(), unique=True, nullable=False)
    make = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))
    vehicle_owner = relationship('User', back_populates='vehicles')
    parking_assignments = relationship('ParkingAssignment', uselist=False)

class ParkingSpace(Base):
    __tablename__ = 'parking_spaces'
    id = Column(Integer(), primary_key=True)
    space = Column(Integer(), unique=True, nullable=False)
    parking_assignmnets = relationship('ParkingAssignment', uselist=False)

class ParkingAssignmnet(Base):
    __tablename__ = 'parking_assignments'
    __table_args__ = (
        UniqueConstraint('vehicle_id', 'parking_space_id', name ='uq_assignment')
    )

    id = Column(Integer(), primary_key = True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    parking_space_id = Column(Integer(), ForeignKey('parking_spaces.id'))

Base.metadata.create_all(engine)


