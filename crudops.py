from sqlalchemy.orm import sessionmaker
from config.dbconfig import engine

Session = sessionmaker(bind = engine)
session = Session()

from migrate import Items

# itemA = Items(id=1, name="Pencil", price="10.0", description="HB pencil")
# itemB = Items(id=2, name="Eraser", price="5.0", description="Eraser")
# itemC = Items(id=3, name="Book", price="15.0", description="Book 40pgs")

# session.add(itemA)
# session.add(itemB)
# session.add(itemC)

# itemD = Items(id=4, name="Pen", price="10.0", description="Black Pen")
# itemE = Items(id=5, name="A4 Sheet", price="2.0", description="White A4")
# itemF = Items(id=6, name="Sharpener", price="5.0", description="Pencil Sharpener")

# session.add_all([itemD, itemE, itemF])

# session.commit()

# result = session.query(Items).all()
# result = session.query(Items).order_by(Items.price)

# for row in result:
#     print("name: " + row.name + ", price: " + str(row.price))

###### Update #######
# result = session.query(Items).filter(Items.price < 10.0)

# for row in result:
#     print("name: " + row.name + ", price: " + str(row.price))


# print("####################################")

# result = session.query(Items).filter(Items.price < 10.0).update({Items.price: (Items.price + (Items.price * 0.05))}, synchronize_session = False)

# session.commit()
# result = session.query(Items).order_by(Items.price)

# for row in result:
#     print("name: " + row.name + ", price: " + str(row.price))


# Delete
# result = session.query(Items).get(3)
# session.delete(result)
# session.commit()

