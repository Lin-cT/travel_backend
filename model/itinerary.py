from __init__ import db
from datetime import datetime

class Itinerary(db.Model):
    __tablename__ = 'itinerary'  # table name is plural, class name is singular

    # Define the Player schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _itinerary = db.Column(db.Text, nullable=False)  

    # constructor of a Player object, initializes the instance variables within object (self)
    def __init__(self, itinerary):
        self._itinerary = itinerary    # variables with self prefix become part of the object, 
    # a name getter method, extracts name from object

    @classmethod
    def Create(cls, itinerary):
        try:
            text = cls(itinerary = itinerary)
            db.session.add(text)
            db.session.commit()
            return text
        except Exception as e:
            print(f"Error creating text upload: {e}")
            db.session.rollback()
            return None