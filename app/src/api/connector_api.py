import requests
from app.src.constants import tags


class ConnectApi:
    def get_tasks_by_tag(self):
        tag_list = tags
        list_to_data = []
        for tag in tag_list:
            req = requests.get(f'https://codeforces.com/api/problemset.problems?tags={tag}')
            data = req.json()

            for problem in data["result"]["problems"]:
                task = {
                    'index': problem["index"],
                    'contestId': problem["contestId"],
                    'category': tag,
                    'topics': problem["tags"],
                    'title': problem["name"] + " - " + problem["index"],
                    'solutions': None,
                    'complexity': problem["rating"] if problem["rating"] else None,
                }

                for stat in data["result"]["problemStatistics"]:
                    if task['contestId'] == stat['contestId'] and task['index'] == stat['index']:
                        task['solutions'] = stat["solvedCount"]
                list_to_data.append(task)

        return list_to_data

    def make_list(self):
        data = self.get_tasks_by_tag()


c = ConnectApi()
print(c.get_tasks_by_tag())
