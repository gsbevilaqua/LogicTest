import json

managers = dict()
watchers = dict()

with open('source_file_2.json') as file:
    data = json.load(file)

ordered_data = sorted(data, key=lambda k: k['priority'])

for project in ordered_data:
    for manager in project['managers']:
        if manager in managers:
            managers[manager].append(project['name'])
        else:
            managers[manager] = [project['name']]
    for watcher in project['watchers']:
        if watcher in watchers:
            watchers[watcher].append(project['name'])
        else:
            watchers[watcher] = [project['name']]

with open('managers.json', 'w') as outfile:
    json.dump(managers, outfile, indent=1)

with open('watchers.json', 'w') as outfile:
    json.dump(watchers, outfile, indent=1)