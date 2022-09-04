from flask import Flask
from utils import *

if __name__ == '__main__':
    candidates_file = 'candidates.json'

    candidates = load_candidates(candidates_file)

    app = Flask(__name__)


    @app.route("/")
    def page_main():
        main_page = get_all(candidates)
        return main_page


    @app.route("/candidates/<int:pk>")
    def page_candidates(pk):
        result = get_by_pk(candidates, pk)
        return result


    @app.route("/skills/<skill>")
    def page_skills(skill):
        result = get_by_skill(candidates, skill)
        return result


    app.run(host='127.0.0.1', port=5000)
