from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()


# connect to a local postgresql database
def db_setup(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    return db


class Hospital(db.Model):
    __tablename__ = 'Hospital'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(String(120))
    review_avg_score = db.relationship(
        'HospitalReview', backref='Hospital', lazy='dynamic')

    def __init__(self, name, city, state, address, phone, website, review_avg_score):
        self.name = name
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.website = website
        self.review_avg_score = review_avg_score

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short(self):
        return{
            'id': self.id,
            'name': self.name,
        }

    def long(self):
        print(self)
        return{
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
        }

    def detail(self):
        return{
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'phone': self.phone,
            'website': self.website,
            'review_avg_score': self.review_avg_score
        }


class HospitalReview(db.Model):
    __tablename__ = 'HospitalReview'

    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey(
        'Hospital.id'), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('Pet.id'), nullable=False)
    symptom = db.Column(db.String(500), default='')
    review = db.Column(db.String(500), default='')
    satisfied = db.Column(Boolean, default=False)
    review_score = db.Column(db.Integer)
    price_score = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, hospital_id, pet_id, symptom, review, satisfied, review_score, price_score, date):
        self.hospital_id = hospital_id
        self.pet_id = pet_id
        self.symptom = symptom
        self.review = review
        self.satisfied = satisfied
        self.review_score = review_score
        self.price_score = prince_score
        self.date = date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def short(self):
        return{
            'id': self.id,
            'hospital_id': self.hospital_id,
            'satisfied': self.satisfied,
            'review_score': self.review_score
        }

    def detail(self):
        return{
            'hospital_id': self.hospital_id,
            'pet_id': self.Artist.name,
            'symptom': self.symptom,
            'review': self.review,
            'satisfied': self.satisfied,
            'review_score': self.review_score,
            'price_score': self.price_score,
            'date': self.date
        }

    def pet_details(self):
        return{
            'pet_id': self.pet_id,
            'pet_name': self.pet_name,
            'pet_image_link': self.pet_image_link
        }

    def hospital_details(self):
        return{
            'hospital_id': self.hospital_id,
            'hospital_name': self.hospital_name
        }


class Pet(db.Model):
    __tablename__ = 'Pet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    species = db.Column(db.String(120))
    breeds = db.Column(ARRAY(String)) # can be more than 1
    gender = db.Column(db.String(120))
    age = db.Column(db.Integer)
    weight = db.Column(db.Double)
    neuter_spay = db.Column(Boolean, default=False)
    disease_history = db.Column(db.String(500), default='')
    temperament = db.Column(db.String(500), default='')
    image_link = db.Column(db.String(500))
    social_network_link = db.Column(db.String(500))


    def __init__(self, name, city, state, phone, species, breeds, gender,
                 age, weight, neuter_spay, disease_history, temperament, image_link, social_network_link):
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.species = species
        self.breeds = breeds
        self.gender = gender
        self.age = age
        self.weight = weight
        self.neuter_spay = neuter_spay
        self.disease_history = disease_history
        self.temperament = temperament
        self.image_link = image_link
        self.social_network_link = social_network_link

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def short(self):
        return{
            'id': self.id,
            'name':self.name,
        }

    def details(self):
        return{
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'breeds':self.breeds,
            'gender': self.gender,
            'age': self.age,
            'weight': self.weight,
            'temperament': self.temperament,
            'image_link': self.image_link,
            'social_network_link': self.social_network_link,
        }
