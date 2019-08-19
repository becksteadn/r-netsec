import requests
import re

def handler(event, context):
    r = requests.get('https://api.pushshift.io/reddit/search/submission/?subreddit=netsec&limit=10')
    for post in r.json()['data']:
        if post['domain'] == "github.com":
            m = re.search('github.com\/([a-zA-Z0-9-_]+)\/([a-zA-Z0-9_-]+)', post['url'])
            try:
                print('{}/{}'.format(m.group(1), m.group(2)))
                s = requests.put('https://api.github.com/user/starred/{}/{}'.format(m.group(1), m.group(2)), headers={'Accept': 'application/vnd.github.v3+json'}, auth=requests.auth.HTTPBasicAuth('r-netsec', ''))
                if s.status_code != 204:
                    print(s.status_code)
            except Exception as e:
                pass
    return {}

if __name__ == "__main__":
    handler({}, {})