from flask import Flask
from flask import jsonify
from views import AdView, UserView
from errors import ApiError, error_handler


app = Flask('app')

app.add_url_rule("/ad/<int:ad_id>", view_func=AdView.as_view('ad'), methods=["GET", "DELETE"])
app.add_url_rule("/ad", view_func=AdView.as_view('ad_post'), methods=["POST"])
app.add_url_rule("/user/<int:user_id>", view_func=UserView.as_view('user'), methods=["GET", "DELETE"])
app.add_url_rule("/user", view_func=UserView.as_view('user_post'), methods=["POST"])

app.errorhandler(ApiError)(error_handler)

if __name__ == '__main__':
    app.run()


