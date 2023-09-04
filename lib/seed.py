from sqlalchemy import create_engine,column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()

session = sessionmaker(bind=engine)()
session = Session()

#define the restaurant class with SQLAlchemy ORM
class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = column(Integer, primary_key=True)
    name = column(String(80), nullable=False)
    price = column(Integer)

#define the relationship between Review and Customer
    reviews = relationship('Review', back_populates ='restaurant')
    customers = relationship('Customer', 
            secondary='review', 
            back_populates='restaurants', 
            veiwonly=True) 
    
    def get_reviews(self):
        return [review for review in self.reviews]
    
    def get_restaurant(self):
        return [restaurant for restaurant in self.restaurants]
    
      @classmethod
    def best (cls):
        # Find the best restaurant based on price
        all_restaurants = session.query(cls).all()
        return f'The best restaurant is {max(all_restaurants, key=lambda restaurant: restaurant.price)}.'

    def all_reviews(self):
        # Retrieve all reviews for the restaurant and return them
        reviews = [review.full_review()
                   for review in self.reviews_relationship]
        return reviews

    def __repr__(self):
        return f'<Restaurant:    id:{self.id}    name:{self.name}    price:{self.price}>\n'

# Define the Customer class with SQLAlchemy ORM


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(10))
    last_name = Column(String(10))

    # Define relationships with Review and Restaurant
    reviews_relationship = relationship('Review', back_populates='customer')

    restaurants = relationship(
        'Restaurant',
        secondary='reviews',
        back_populates='customers',
        viewonly=True)

    def get_reviews(self):
        # Return all reviews written by this customer
        return self.reviews_relationship

    def get_restaurants(self):
        # Return all restaurants that this customer has reviewed

    
