import requests
import json


def get_all_vessels_postion_data() -> list:
    s = requests.Session()
    s.headers["user-agent"] = \
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    s.headers["x-requested-with"] = 'XMLHttpRequest'
    s.get("https://www.marinetraffic.com/")
    s.headers["vessel-image"] = '001a96d8cd91fa06e86a2e7b8b81a289e824'
    rows = []
    for x in range(0, 3):
        for y in range(0, 3):
            r = s.get(f"https://www.marinetraffic.com/getData/get_data_json_4/z:2/X:{x}/Y:{y}/station:1")
            print(f"{r.status_code} X={x}, Y={y}")
            if r.status_code < 399:
                rows += r.json()['data']['rows']
                print(f"{r.json()['data']['areaShips']}")
    #with open("get_data_json_4.json", "w") as jfile:
    #    json.dump(r.json(), jfile, indent=4, sort_keys=True)
    return rows


if __name__ == "__main__":
    print(len(get_all_vessels_postion_data()))

