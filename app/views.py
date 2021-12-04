import random
import http
from flask import Blueprint, request, jsonify, abort

bp = Blueprint("frontend", "fe", root_path="/")


@bp.route("/ping", methods=['GET', 'HEAD'])
def api_ping():
    return jsonify({"alive": True})


@bp.route("/name", methods=['POST'])
def api_put_new_name():
    name = request.json['name'] or None

    if not name:
        abort(400)

    with open("./first-names", "a+") as fh:
        fh.writelines([name])

    return jsonify({"name": name})


@bp.route("/name", methods=['GET'])
def api_get_random_name():
    filenames = {
        "m": "./first-names.male",
        "f": "./first-names.female"
    }

    count = int(request.args.get('count', 1))

    with open(filenames[request.args['gender']], "r") as fh:
        names = [n.strip() for n in fh.readlines() if not n.startswith("#")]

    with open("./last-names", "r") as fh:
        last_names = [n.strip() for n in fh.readlines() if not n.startswith("#")]

    return jsonify([{
        "firstName": random.choice(names),
        "lastName": random.choice(last_names),
    } for _ in range(count)])

