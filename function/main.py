import requests
import re
import os

def handler(event, context):
    r = requests.get('https://api.pushshift.io/reddit/search/submission/?subreddit=netsec&limit=10')
    auth = (os.environ['GH_USERNAME'], os.environ['GH_PASSWORD'])
    starred = list()
    for post in r.json()['data']:
        if post['domain'] == "github.com":
            m = re.search('github.com\/([a-zA-Z0-9-_]+)\/([a-zA-Z0-9_-]+)', post['url'])
            print('{}/{}'.format(m.group(1), m.group(2)))
            try:
                s = requests.put('https://api.github.com/user/starred/{}/{}'.format(m.group(1), m.group(2)), headers={'Accept': 'application/vnd.github.v3+json'}, auth=requests.auth.HTTPBasicAuth(auth[0], auth[1]))
                if s.status_code == 204:
                    starred.append('{}/{}'.format(m.group(1), m.group(2)))
                else:
                    print(s.status_code)
            except Exception as e:
                print(e)
                pass
    return {'starred': starred}

if __name__ == "__main__":
    handler({}, {})