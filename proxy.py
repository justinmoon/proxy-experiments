from argparse import ArgumentParser
from requests import get, post, delete


auth_token = 'abc123'
proxy_url = 'http://localhost:5001'
routes_url = 'http://localhost:5002/api/routes'
headers = {'Authorization': f'token {auth_token}'}


def get_routes():
    return get(routes_url, headers=headers)


def map_route(frm, to):
    payload = {'target': to}
    url = routes_url + frm
    return post(url, headers=headers, json=payload)


def delete_route(route):
    url = routes_url + route
    print(url)
    return delete(url, headers=headers)


if __name__ == '__main__':

    parser = ArgumentParser(description='Test configurable-http-proxy')
    parser.add_argument('--get')
    parser.add_argument('--routes', action='store_true')
    parser.add_argument('--map', nargs='*')
    parser.add_argument('--delete')
    args = parser.parse_args()

    # print(args)
    if args.get:
        url = proxy_url + args.get
        res = get(url)
        print(res.text)
    elif args.routes:
        print('routes:', get_routes().json())
    elif args.map:
        res = map_route(*args.map)
        if res.ok:
            print('routes updated')
        else:
            print(f'error: reason={res.reason} text={res.text}')
    elif args.delete:
        delete_route(args.delete)
        if res.ok:
            print('route deleted')
        else:
            print(f'error: reason={res.reason} text={res.text}')

