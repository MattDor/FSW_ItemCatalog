from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item

#
# Populate item store with a pre-defined list of categories
#

engine = create_engine("sqlite:///itemstore.db")

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

categories = ("Mammals","Birds","Fishes","Reptiles","Amphibians","Insects","Arachnoids")

item_list = {
	"Mammals"		: 	("Lion","Elephant","Rhino"),
	"Birds"			:	("Eagle","Starling","Finch"),
	"Fishes"		:	("Marlin","Shark","Sea Horse"),
	"Reptiles"		:	("Crocodile","Snake","Turtle"),
	"Amphibians"	:	("Frog","Toad","Salamander"),
	"Insects"		:	("Mosquito","Fly","Bee"),
	"Arachnoids"	:	("Scorpion","Spider","Mite")
}

for category in categories:

	category_obj = Category(name = category)
	session.add(category_obj)
	session.commit()

	for item in item_list[category]:
		print item
		item_obj = Item(name=item, category=category_obj)
		session.add(item_obj)
		session.commit()

