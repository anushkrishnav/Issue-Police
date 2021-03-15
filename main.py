import os
import requests
import github

def count_issues(name, token):
    owner = name
    repo = "Issue-spam-blocker"
    author = name
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{owner}/{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw=(r.json())
    return raw['total_count']

def get_latest_issue(name,token):
    owner = name
    repo = "Issue-spam-blocker"
    author = name
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{owner}/{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw=(r.json())
    k = raw['items']
    k = k[0]
    return k['number']

token = os.environ['INPUT_TOKEN']
author = os.environ['INPUT_AUTHOR']

def close_issue(num):
    issue = repo.get_issue(num)
    issue.create_comment('bonk !! You cannont create more than 3 Issues at a time close your old issues to make a new one')
    issue.edit(state = 'closed')


github = github.Github(token)
repo = github.get_repo(os.environ['GITHUB_REPOSITORY'])
issue = repo.create_issue(
    title="title",
    body="body",
    assignees=author,
)
count_issues(name=author,token=token)

numb = get_latest_issue(name=author,token=token)
if count_issues >= 4:
    close_issue(numb)

