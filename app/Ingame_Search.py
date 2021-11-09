from riotwatcher import LolWatcher, ApiError


def player_ingame(list, key):
    watcher = LolWatcher(key)
    region = "na1"
    nameList = list.split(", ")
    inList = ['Players In Game']
    outList = ['Players Not In Game']

    for name in nameList:
        player = watcher.summoner.by_name(region, name)
        print(player)
        try:
            playerInGame = watcher.spectator.by_summoner(region, player['id'])
            inList.append(name)
        except:
            playerInGame = ""
            outList.append(name)
    return inList, outList


print(player_ingame('YNO BLITZ, MAMMOTHMAN65', "RGAPI-627f53b1-5772-4e5f-9801-5cf3f97d9ddb"))
