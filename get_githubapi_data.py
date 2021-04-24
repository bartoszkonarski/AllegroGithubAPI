import aiohttp
import asyncio
import time
import os
import requests

def get_repos_and_stars(username,api_token):
    start_time = time.time()
    headers = {'Authorization': 'token '+api_token}
    response = requests.get(f"https://api.github.com/users/{username}",headers=headers).json()
    public_repos = response['public_repos']
    pages = public_repos//100+1
    export = {
        'userdata' : {'username' : username, 'full_name' : response['name'],'repos_count' : public_repos},
        'repos' : []}
    output = []

    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = []
            for page in range(pages):
                task = asyncio.ensure_future(get_repos_data(session, page+1))
                tasks.append(task)

            stargazers= await asyncio.gather(*tasks)
            return sum(stargazers)





    async def get_repos_data(session, current_page):
        url = f"https://api.github.com/users/{username}/repos"

        async with session.get(url,params={'per_page':100,'page':current_page},headers=headers) as response:
            stargazers = 0
            result_data = await response.json()
            
            for repo in result_data:
                output.append(
                    {
                        'name': repo['name'],
                        'stargazers_count': repo['stargazers_count'],
                        'repo_url': repo['html_url']
                    })
                stargazers+=repo['stargazers_count']
            return stargazers

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    stargazers = asyncio.run(main())
    
    export['userdata']['total_stargazers'] = stargazers
    export['repos']=sorted(output, key=lambda k: k['name'].lower()) 

    print("--- %s seconds ---" % (time.time() - start_time))
    return export

if __name__ == "__main__":
    pass