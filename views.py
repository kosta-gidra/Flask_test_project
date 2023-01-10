from flask.views import MethodView
from flask import jsonify, request
from database import AdModel, get_session_maker, UserModel
from errors import ApiError

Session = get_session_maker()


class AdView(MethodView):

    def get(self, ad_id: int):
        with Session() as session:
            ad = session.query(AdModel).get(ad_id)
            if ad is None:
                raise ApiError(404, 'ad not found')
            return jsonify({
                'id': ad.id,
                'header': ad.header,
                'description': ad.description,
                'date': ad.date,
                'owner_id': ad.owner
            })

    def post(self):
        input_json = request.get_json(force=True)
        with Session() as session:
            if session.query(AdModel).get(input_json['id']):
                raise ApiError(409, 'ad already exists')
            new_add = AdModel(id=input_json['id'], header=input_json['header'],
                              description=input_json['description'],
                              owner=input_json['owner'])
            session.add(new_add)
            session.commit()
            dict_to_return = {'status': 200,
                              'data from client': input_json}
        print('data from client:', input_json)
        return jsonify(dict_to_return)

    def delete(self, ad_id: int):
        with Session() as session:
            ad = session.query(AdModel).get(ad_id)
            if ad is None:
                raise ApiError(404, 'ad not found')
            session.delete(ad)
            session.commit()
        dict_to_return = {'status': 200}
        return jsonify(dict_to_return)


class UserView(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            user = session.query(UserModel).get(user_id)
            if user is None:
                raise ApiError(404, 'user not found')
            return jsonify({
                'id': user.id,
                'name': user.name,
            })

    def post(self):
        input_json = request.get_json(force=True)
        with Session() as session:
            if session.query(UserModel).get(input_json['id']):
                raise ApiError(409, 'user already exists')
            new_user = UserModel(id=input_json['id'], name=input_json['name'])
            session.add(new_user)
            session.commit()
            dict_to_return = {'status': 200,
                              'data from client': input_json}
        print('data from client:', input_json)
        return jsonify(dict_to_return)

    def delete(self, user_id: int):
        with Session() as session:
            user = session.query(UserModel).get(user_id)
            if user is None:
                raise ApiError(404, 'user not found')
            session.delete(user)
            session.commit()
        dict_to_return = {'status': 200}
        return jsonify(dict_to_return)
