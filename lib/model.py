# Import necessary libraries and create an SQLite database engine
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Create a SQLAlchemy engine that connects to an SQLite database file named 'restaurant.db'
engine = create_engine('sqlite:///restaurant.db')

# Create a base class for declarative models
Base = declarative_base()

# Create a session maker for interacting with the database using the engine
Session = sessionmaker(bind=engine)
session = Session()

# Define the Restaurant class with SQLAlchemy ORM
class Restaurant(Base):
    __tablename__ = 'restaurants'

    # Define columns for the 'restaurants' table
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Integer)

    # Define relationships with the 'Review' and 'Customer' models
    reviews_relationship = relationship('Review', back_populates='restaurant')
    customers = relationship(
        'Customer',
        secondary='reviews',
        back_populates='restaurants',
        viewonly=True)

    # Various methods to interact with Restaurant objects

# Define the Customer class with SQLAlchemy ORM
class Customer(Base):
    __tablename__ = 'customers'

    # Define columns for the 'customers' table
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(10))
    last_name = Column(String(10))

    # Define relationships with the 'Review' and 'Restaurant' models
    reviews_relationship = relationship('Review', back_populates='customer')
    restaurants = relationship(
        'Restaurant',
        secondary='reviews',
        back_populates='customers',
        viewonly=True)

    # Various methods to interact with Customer objects

# Define the Review class with SQLAlchemy ORM
class Review(Base):
    __tablename__ = 'reviews'

    # Define columns for the 'reviews' table
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Define relationships with the 'Restaurant' and 'Customer' models
    restaurant = relationship('Restaurant', back_populates='reviews_relationship')
    customer = relationship('Customer', back_populates='reviews_relationship')


