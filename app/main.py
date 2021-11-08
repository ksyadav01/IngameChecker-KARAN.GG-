from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
import os
import Ingame_Search

app = Flask(__name__)
API_KEY = os.environ.get('API_KEY')

InitialList = ""  # Initial list of names provided by user
InGameList = []  # Players in game
NotInGameList = []  # Players not in game


@app.route('/')
@app.route('/home')
def home():
    if request.method == 'POST':
        global InitialList
        global InGameList
        global NotInGameList
        InitialList = request.form.get('NameList')
        InGameList, NotInGameList = Ingame_Search.player_ingame(InitialList, API_KEY)
        return redirect(url_for('ingame_list'))
    return "<h1>Welcome to CodingX</h1>" #render_template('ingame_search.html')


@app.route('/ingame_list')
def ingame_result():
    # print(champion)
    # if individual_search_type == "champion_wr":
    #     table = individual_search.champion_search(summoner_name, champion, game_list, match_history_list)
    # if individual_search_type == "your_data":
    #     table = individual_search.your_search(summoner_name, game_list)
    # print(stats)
    return render_template('ingame_result.html', inTbl=zip(*InGameList), outTbl=zip(*NotInGameList))
