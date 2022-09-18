import requests
import json


def _get_mt_session() -> requests.Session:
    s = requests.Session()
    s.headers["user-agent"] = \
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    s.headers["x-requested-with"] = 'XMLHttpRequest'
    s.get("https://www.marinetraffic.com/")
    s.headers["vessel-image"] = '001a96d8cd91fa06e86a2e7b8b81a289e824'
    return s


def get_ships_position_data(tiles: list[tuple[int, int]], zoom: int = 14) -> list:
    s: requests.Session = _get_mt_session()
    rows = []
    for tile in tiles:
        x = tile[0]
        y = tile[1]
        r = s.get(f"https://www.marinetraffic.com/getData/get_data_json_4/z:{zoom}/X:{x}/Y:{y}/station:0")
        print(f"{r.status_code} X={x}, Y={y}")
        if r.status_code < 399:
            rows += r.json()['data']['rows']
            print(f"{r.json()['data']['areaShips']}")
    #with open("get_data_json_4.json", "w") as jfile:
    #    json.dump(r.json(), jfile, indent=4, sort_keys=True)
    return rows


if __name__ == "__main__":
    # TODO print(len(get_all_ships_postion_data()))
    ...

