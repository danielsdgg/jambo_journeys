from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, User, Hotel, Park, Ranger, Review, Booking
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jambo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the jambo API'})

@app.route('/users', methods=['GET','POST'])
def get_users():
    if request.method == 'GET':
        users = User.query.all()
        user_list = []
        for user in users:
            user_dict = user.to_dict()
            user_list.append(user_dict)
        response = make_response(
            jsonify(user_list),
            200
        )
        return response
    elif request.method == 'POST':
        new_user = User(
            username = request.form.get('username'),
            phone_number = request.form.get('phone_number'),
            password = request.form.get('password'),

        )
        db.session.add(new_user)
        db.session.commit()

        response = make_response(
            jsonify(new_user.to_dict()),
            201
        )
        return response
    
@app.route('/user/<int:id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        user = User.query.filter_by(id=id).first()
        if user:
            response = make_response(
                jsonify(user.to_dict()),
                200
            )
            return response
        else:
            response = make_response(
                jsonify({'message': 'User not found'}),
                404
            )
            return response
    if request.method == 'DELETE':
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            response = make_response(
                jsonify({'message': 'User deleted'}),
                200
            )
            return response
        else:
            response = make_response(
                jsonify({'message': 'User not found'}),
                404
            )
            return response
    
@app.route('/hotels', methods=['GET','POST'])
def get_hotels():
    if request.method == 'GET':
        hotels = Hotel.query.all()
        hotel_list = []
        for hotel in hotels:
            hotel_dict = hotel.to_dict()
            hotel_list.append(hotel_dict)
        response = make_response(
            jsonify(hotel_list),
            200
        )
        return response
    elif request.method == 'POST':
        new_hotel = Hotel(
            name = request.form.get('name'),
            image_url = request.form.get('image_url'),
            description = request.form.get('description'),
            location = request.form.get('location'),
            prices = request.form.get('prices'),
        )
        db.session.add(new_hotel)
        db.session.commit()

        response = make_response(
            jsonify(new_hotel.to_dict()),
            201
        )
        return response
    
@app.route('/hotel/<int:id>', methods=['GET', 'PATCH' , 'DELETE'])
def get_hotel(id):
    if request.method == 'GET':
            hotel = Hotel.query.filter_by(id=id).first()
            if hotel:
                response = make_response(
                    jsonify(hotel.to_dict()),
                    200
                )
                return response
            else:
                response = make_response(
                    jsonify({'message': 'Hotel not found'}),
                    404
                )
                return response
            
    if request.method == 'PATCH':
        hotel = Hotel.query.filter_by(id=id).first()
        if hotel:
            attributes_to_update = ['name', 'image_url', 'description', 'location', 'prices']
            for attribute in attributes_to_update:
             value = request.form.get(attribute)
             if value: 
                setattr(hotel, attribute, value)
            db.session.commit()

            response = make_response(
                jsonify(hotel.to_dict()),
                200
            )
            return response
        else:
            response = make_response(
                jsonify({'message': 'Hotel not found'}),
                404
            )
            return response
            
    if request.method == 'DELETE':
        hotel = Hotel.query.filter_by(id=id).first()
        if hotel:
            db.session.delete(hotel)
            db.session.commit()

            response = make_response(
                jsonify({'message': 'Hotel deleted'}),
                200
            )
            return response
        else:
            response = make_response(
                jsonify({'message': 'Hotel not found'}),
                404
            )
            return response
        
@app.route('/parks', methods=['GET','POST'])
def get_parks():
    if request.method == 'GET':
        parks = Park.query.all()
        park_list = []
        for park in parks:
            park_dict = park.to_dict()
            park_list.append(park_dict)
        response = make_response(
            jsonify(park_list),
            200
        )
        return response
    
    if request.method == 'POST':
        new_park = Park(
            name = request.form.get('name'),
            image_url = request.form.get('image_url'),
            description = request.form.get('description'),
            location = request.form.get('location'),
            prices = request.form.get('prices'),
        )
        db.session.add(new_park)
        db.session.commit()

        response = make_response(
            jsonify(new_park.to_dict()),
            201
        )
        return response
    
@app.route('/park/<int:id>', methods=['GET', 'PATCH' , 'DELETE'])
def get_park(id):
    if request.method == 'GET':
       park = Park.query.filter_by(id=id).first()
       if park:
           response = make_response(
               jsonify(park.to_dict()),
               200
           )
           return response
    
    if request.method == 'PATCH':
      park = Park.query.filter_by(id=id).first()
      if park:
        attributes_to_update = ['name', 'image_url', 'description', 'location']
        for attribute in attributes_to_update:
            value = request.form.get(attribute)
            if value: 
                setattr(park, attribute, value)
        db.session.commit()

        response = make_response(
            jsonify(park.to_dict()),
            200)
        return response
      else:
        response = make_response(
            jsonify({'message': 'Park not found'}),
            404)
        return response
      
    if request.method == 'DELETE':
        park = Park.query.filter_by(id=id).first()
        if park:
            db.session.delete(park)
            db.session.commit()

            response = make_response(
                jsonify({'message': 'Park deleted'}),
                200)
            return response
        else:
            response = make_response(
                jsonify({'message': 'Park not found'}),
                404)
            return response

@app.route('/rangers', methods=['GET','POST'])
def get_rangers():
    if request.method == 'GET':
        rangers = Ranger.query.all()
        ranger_list = []
        for ranger in rangers:
            ranger_dict = ranger.to_dict()
            ranger_list.append(ranger_dict)
        response = make_response(
            jsonify(ranger_list),
            200
        )
        return response
    elif request.method == 'POST':
        new_ranger = Ranger(
            name = request.form.get('name'),
            gender = request.form.get('gender'),
        )
        db.session.add(new_ranger)
        db.session.commit()
        response = make_response(
            jsonify(new_ranger.to_dict()),
            201
        )
        return response
    
@app.route('/ranger/<int:id>', methods=['GET', 'PATCH' , 'DELETE'])
def get_ranger(id):
    if request.method == 'GET':
        ranger = Ranger.query.filter_by(id=id).first()
        if ranger:
            response = make_response(
                jsonify(ranger.to_dict()),
                200
            )
            return response
        else:
            response = make_response(
                jsonify({'message': 'Ranger not found'}),
                404
            )
            return response
    
    if request.method == 'PATCH':
        ranger = Ranger.query.filter_by(id=id).first()
        if ranger:
            attributes_to_update = ['name', 'gender']
            for attribute in attributes_to_update:
                value = request.form.get(attribute)
                if value: 
                    setattr(ranger, attribute, value)
            db.session.commit()

            response = make_response(
                jsonify(ranger.to_dict()),
                200)
            return response
        else:
            response = make_response(
                jsonify({'message': 'Ranger not found'}),
                404)
            return response
        
    if request.method == 'DELETE':
        ranger = Ranger.query.filter_by(id=id).first()
        if ranger:
            db.session.delete(ranger)
            db.session.commit()

            response = make_response(
                jsonify({'message': 'Ranger deleted'}),
                200)
            return response
        else:
            response = make_response(
                jsonify({'message': 'Ranger not found'}),
                404)
            return response

@app.route('/reviews', methods=['GET', 'POST'])
def get_reviews():
    if request.method == 'GET':
        reviews = Review.query.all()
        review_list = []
        for review in reviews:
            review_dict = review.to_dict()
            review_list.append(review_dict)
        response = make_response(
            jsonify(review_list),
            200
        )
        return response
    if request.method == 'POST':
        new_review = Review(
            name = request.form.get('name'),
            email = request.form.get('email'),
            feedback = request.form.get('feedback'),
            user_id = request.form.get('user_id'),
        )
        db.session.add(new_review)
        db.session.commit()

        response = make_response(
            jsonify(new_review.to_dict()),
            201
        )
        return response

@app.route('/bookings', methods=['GET', 'POST'])
def get_bookings():
    if request.method == 'GET':
        bookings = Booking.query.all()
        booking_list = []
        for booking in bookings:
            booking_dict = booking.to_dict()
            booking_list.append(booking_dict)
        response = make_response(
            jsonify(booking_list),
            200
        )
        return response
    
    if request.method == 'POST':
        new_booking = Booking(
            user_id = request.form.get("user_id"),
            hotel_name = request.form.get("hotel_name"),
            park_name = request.form.get("park_name"),
            check_in = request.form.get('check_in'),
            check_out = request.form.get('check_out'),
        )
        db.session.add(new_booking)
        db.session.commit()

        response = make_response(
            jsonify(new_booking.to_dict()),
            201
        )
        return response


if __name__ == '__main__':
    app.run(debug=True)
    
