# coding: utf-8
def update_subscriptions(silence=False):
    from tools import *
    import xbmcaddon
    import json

    token = xbmcaddon.Addon('script.tvshowtime').getSetting('token')
    # settings.log('token %s' % token)
    # browser.headers['Authorization'] = 'token %s' % token
    # response = browser.get('https://api.tvshowtime.com/v1/user?access_token=%s' % token)
    response = browser.get('https://api.tvshowtime.com/v1/library?limit=100&access_token=%s' % token)
    shows = json.loads(response.text)['shows']
    if len(shows) > 0:
        titles = []
        ids = []
        for show in shows:
            settings.log("Found show: %s(%d)" % (show['name'], show['id']))
            titles.append(show['name'])
            ids.append(show['id'])
        subscription(titles=titles, id=ids, typeList='SHOW', folder=settings.showFolder, silence=silence)
        settings.notification("Found %d shows from TVShow Time" & len(shows))
    else:
        settings.notification("No shows found in TVShow Time")

update_subscriptions()
