import requests
from time import sleep

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'client-version': 'v2.46.33',
    'cookie': '你的 cookie，通过浏览器 F12开发者工具可以抓取到',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://weibo.com/u/page/follow/2683853775',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2024.11.13.2',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': '3UY8KpdL9LuW4UUF9liAvCGM',
}


def 关注列表():
    params = {
        'page': '1', # 这个1可以不用改，微博默认删除后会重新加载
        'uid': '你的 uid',
    }
    response = requests.get('https://weibo.com/ajax/friendships/friends', params=params,  headers=headers)
    if response.status_code == 200:
        data = response.json()
        users = data['users']
        return users
    else:
        return None
def 取消关注(uid):
    json_data = {
    'uid': uid
    }
    
    response = requests.post('https://weibo.com/ajax/friendships/destory', headers=headers, json=json_data)
    if response.status_code == 200:
        res = response.json()
        print(f"取消订阅 {res.get('screen_name', 'false')} : {res.get('ok', 'false')}")
    else:
        print(f"取消订阅失败 {response.status_code}")


if __name__ == '__main__':
    
    users = 关注列表()
    for i in range(len(users)):
        uid = users[i]['id']
        取消关注(uid)
        # sleep(1)