from app import db
from models import BlogPost

#create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Excellent", "I\'m excellent."))
db.session.add(BlogPost("Okay", "I\'m okay."))
db.session.add(BlogPost("Bad", "I\'m bad."))
db.session.add(BlogPost("Flask", "discoverflask.com"))
db.session.add(BlogPost("postgres", "we setup a local postgres instance"))



#commit the changes
db.session.commit()