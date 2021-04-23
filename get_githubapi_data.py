import requests
import json
import os
import time

def get_repos_and_stars(username,api_token):
    start = time.time()
    headers = {'Authorization': 'token '+api_token}
    s = requests.Session()
    s.headers.update(headers)
    response = s.get(f"https://api.github.com/users/{username}")
    if response.status_code == 404:
        return 404
    else:
        response=response.json()
    public_repos = response['public_repos']
    current_page = 1

    output = {}
    output['userdata'] = {'username' : username, 'repos_count' : public_repos}
    output['repos'] = []
    total_stargazers = 0

    for page in range(public_repos//100+1):
        response = s.get(f"https://api.github.com/users/{username}/repos",params = {'per_page':100,'page':current_page}).json()
        for repo in response:
            output['repos'].append(
                {
                    'name': repo['name'],
                    'stargazers_count': repo['stargazers_count']
                })
            total_stargazers += int(repo['stargazers_count'])
        current_page+=1
    output['userdata']['total_stargazers'] = total_stargazers
    end=time.time()
    print(end-start)
    return output

if __name__ == "__main__":
    pass