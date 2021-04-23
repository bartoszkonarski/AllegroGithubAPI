from flask import Flask,make_response,jsonify
from flask_restful import Api, Resource
from get_githubapi_data import get_repos_and_stars
from flask_caching import Cache
import os

app = Flask(__name__)
api = Api(app)
cache = Cache(app,config={'CACHE_TYPE':'SimpleCache'})
app.config['JSON_SORT_KEYS'] = False
app.config['GITHUB_API_TOKEN'] = os.environ['GITHUB_API_TOKEN']

class GithubUser(Resource):
    @cache.cached(timeout=60)
    def get(self,username):
        output = get_repos_and_stars(username,app.config['GITHUB_API_TOKEN'])
        if output == 404:
            return make_response(jsonify({'message':'Error 404: user not found'}),404)
        response = make_response(jsonify(output),200)
        response.headers["Content-Type"] = "application/json"
        return response

api.add_resource(GithubUser,"/api/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
