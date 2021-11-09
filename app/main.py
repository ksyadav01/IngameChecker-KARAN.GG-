from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from riotwatcher import LolWatcher, ApiError
import os
import time

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
        global API_KEY
        InitialList = request.form.get('NameList')
        watcher = LolWatcher(API_KEY)
        region = "na1"
        nameList = InitialList.split(", ")

        for name in nameList:
            player = watcher.summoner.by_name(region, name)
            try:
                playerInGame = watcher.spectator.by_summoner(region, player['id'])
                print(playerInGame)
                if name not in InGameList:
                    InGameList.append(name)
                if name in NotInGameList:
                    NotInGameList.remove(name)
            except:
                NotInGameList.append(name)
                if name not in NotInGameList:
                    NotInGameList.append(name)
                if name in InGameList:
                    InGameList.remove(name)
        # InGameList, NotInGameList = ingame_search.player_ingame(InitialList, API_KEY)
        # time.sleep(3)
        return redirect(url_for('ingame_result'))
    return render_template('ingame_search.html')


@app.route('/ingame_result')
def ingame_result():
    # print(champion)
    # if individual_search_type == "champion_wr":
    #     table = individual_search.champion_search(summoner_name, champion, game_list, match_history_list)
    # if individual_search_type == "your_data":
    #     table = individual_search.your_search(summoner_name, game_list)
    # print(stats)
    # inTbl=zip(*InGameList), outTbl=zip(*NotInGameList)
    print(InGameList)
    print(NotInGameList)
    return render_template('ingame_result.html', a=InGameList, b=NotInGameList)
