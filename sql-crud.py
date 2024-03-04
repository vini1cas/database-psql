from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")

base = declarative_base()

class Programmer(base):
    __tablename__ = "programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nationality = Column(String)
    gender = Column(String)
    famous_for = Column(String)

Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    nationality = "British",
    gender = "F",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    nationality = "British",
    gender = "M",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    nationality = "American",
    gender = "F",
    famous_for = "COBOL Language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    nationality = "American",
    gender = "F",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    nationality = "American",
    gender = "M",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    nationality = "British",
    gender = "M",
    famous_for = "World Wide Web"
)

vinicius_de_castro = Programmer(
    first_name = "Vinicius",
    last_name = "De Castro",
    nationality = "Brazilian",
    gender = "M",
    famous_for = "Junior Developer"
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(margaret_hamilton)
# session.add(grace_hopper)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(vinicius_de_castro)


# programmer = session.query(Programmer).filter_by(id=9).first()
# programmer.famous_for = "Revolutionizing App"

# session.commit()

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "M":
#         person.gender = "Male"
#     elif person.gender == "F":
#         person.gender = "Female"
#     else:
#         print("Gender not defined")
#     session.commit()

fname = input("Enter a First Name:")
lname = input("Enter a Last Name:")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# defensive programming 

if programmer is not None:
    print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n)")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Record has been deleted")
    else:
        print("Programmer not deleted")

else:
    print("No records found")


programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" / "
    )