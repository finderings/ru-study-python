from flask import Flask, request


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        users_data = {}

        def not_found():
            return {"errors": {"name": "User not found"}}, 404

        def wrong_content_type():
            return {"errors": {"content_type": "Wrong content type"}}, 415

        @app.route("/user", methods=["POST"])
        def user_create():
            content_type = request.headers.get("Content-Type")
            if content_type != "application/json":
                return wrong_content_type()
            user = request.json
            if "name" not in user:
                error = {"errors": {"name": "This field is required"}}
                return error, 422
            users_data.update(user)
            new_user = {"data": f"User {user['name']} is created!"}
            return new_user, 201

        @app.route("/user/<name>", methods=["GET"])
        def user_name(name):
            if "name" not in users_data:
                return not_found()
            getted_name = {"data": f"My name is {users_data['name']}"}
            return getted_name, 200

        @app.route("/user/<name>", methods=["PATCH"])
        def update_user(name):
            content_type = request.headers.get("Content-Type")
            if content_type != "application/json":
                return wrong_content_type()
            if "name" not in users_data:
                return not_found()
            user = request.json
            users_data.update(user)
            updated_user = {"data": f"My name is {user['name']}"}
            return updated_user, 200

        @app.route("/user/<name>", methods=["DELETE"])
        def delete_user(name):
            if "name" not in users_data:
                return not_found()
            del users_data["name"]
            return "", 204
