from flask import jsonify



@main.route("/")
@main.route("/home")
def home():
    B = "This is the home page"
    return jsonify(B)


@main.route("/about")
def about():
    G = "about page"
    return jsonify(G)
