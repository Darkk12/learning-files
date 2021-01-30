import requests
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
header = {'Accept': 'application/vnd.github.v10+json'}
r = requests.get(url, header)
print(f'Status Code: {r.status_code}')
dict = r.json()
print(f'Total Repositories: {dict["total_count"]}')
print(f'Repositories Returned: {len(dict["items"])}')
rep_dict = dict['items']
# for key in sorted(rep_dict):
#     print(key)
links, details, name, stars = [], [], [], []
for i in rep_dict:
    name.append(i['name'])
    stars.append(i['stargazers_count'])
    owner = i['owner']['login']
    description = i['description']
    details.append(f'{owner}<br />{description}')
    link = i['html_url']
    links.append(f"<a href = '{link}'>{link}</a>")
data = [{'type': 'bar', 'text': details, 'x': links, 'y': stars, 'opacity': 0.7, 'marker': {'color': 'rgb(180,100,250)',
                                                          'line': {'width': 1.5, 'color': 'rgb(255,10,10)'}}}]
my_layout = {'title': 'Most Starred Projects on GitHub', 'titlefont': {'family': 'Arial','size': 36},
             'xaxis': {'title': 'Repository', 'titlefont': {'family': 'Times New Roman', 'size': 28}, 'tickfont': {'size': 12}},
              'yaxis': {'title': 'Stars', 'titlefont': {'family': 'Times New Roman', 'size': 28}, 'tickfont': {"size": 12}}}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'HTML files/API_repository.html')
