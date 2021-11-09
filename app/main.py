from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from riotwatcher import LolWatcher, ApiError
import os

# from app import ingame_search

app = Flask(__name__)
API_KEY = os.environ.get('API_KEY')

InitialList = ""  # Initial list of names provided by user
InGameList = []  # Players in game
NotInGameList = []  # Players not in game


@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        global InitialList
        global InGameList
        global NotInGameList

        InitialList = request.form.get('NameList')
        watcher = LolWatcher(API_KEY)
        region = "na1"
        nameList = InitialList.split(", ")
        InGameList.append('Players In Game')
        NotInGameList.append('Players Not In Game')

        for name in nameList:
            player = watcher.summoner.by_name(region, "name")
            try:
                playerInGame = watcher.spectator.by_summoner(region, player['id'])
                InGameList.append(name)

            except:
                NotInGameList.append(name)
        # InGameList, NotInGameList = ingame_search.player_ingame(InitialList, API_KEY)
        return redirect(url_for('ingame_list'))
    return render_template('ingame_search.html')


@app.route('/ingame_list')
def ingame_result():
    # print(champion)
    # if individual_search_type == "champion_wr":
    #     table = individual_search.champion_search(summoner_name, champion, game_list, match_history_list)
    # if individual_search_type == "your_data":
    #     table = individual_search.your_search(summoner_name, game_list)
    # print(stats)
    return render_template('ingame_result.html', inTbl=zip(*InGameList), outTbl=zip(*NotInGameList))
