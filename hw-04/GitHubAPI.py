import requests

def gitUserInfo(ID):
    info = requests.get(f"https://api.github.com/users/{ID}/repos")
    info = info.json()
    userInfo = []

    for repo in info:
        numCommits = requests.get(f"https://api.github.com/repos/{ID}/{repo['name']}/commits")
        numCommits = len(numCommits.json())
        userInfo.append("Repo: " + repo['name'] + " Number of commits: " + str(numCommits))
    
    return userInfo

# gitUserInfo('francescaseverino')