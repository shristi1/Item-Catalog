from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com")
session.add(User1)
session.commit()

#Add Soccer Cleats and Shinguards to Soccer
category = Category(name="Soccer")

session.add(category)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Soccer Cleats", description="An item of footwear worn when playing soccer. Those designed for grass pitches have studs on the outsole to aid grip.", creation_date = datetime.datetime(2003, 8, 4, 12, 30, 45), category=category, )

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Shinguards", description="a piece of equipment worn on the front of a player's shin to protect them from injury.", creation_date = datetime.datetime(2003, 8, 4, 12, 30, 45), category=category)

session.add(categoryItem2)
session.commit()

#Add items to Basketball
category = Category(name="Basketball")

session.add(category)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Hoop", description="Horizontal circular metal hoop supporting a net through which players try to throw the basketball.", creation_date = datetime.datetime(2003, 8, 4, 12, 30, 45), category=category, )

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Basketball Ball", description="A sphere shaped object used in the game of basketball to scare points.", creation_date = datetime.datetime(2003, 8, 4, 12, 30, 45), category=category)

session.add(categoryItem2)
session.commit()

