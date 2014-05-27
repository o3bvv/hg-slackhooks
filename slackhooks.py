# -*- coding: utf-8 -*-
import urllib2
import json

from collections import namedtuple
from mercurial.cmdutil import show_changeset


config_group = 'slackhooks'
Config = namedtuple(
    'HgSlackHooksConfig',
    field_names=[
        'token',
        'org_name',
        'repo_name',
        'commit_url',
        'username',
        'icon_emoji',
        'icon_url',
    ])


def get_config(ui):
    token = ui.config(config_group, 'token')
    org_name = ui.config(config_group, 'org_name')
    repo_name = ui.config(config_group, 'repo_name', default=None)
    commit_url = ui.config(config_group, 'commit_url', default=None)
    username = ui.config(config_group, 'username', default="mercurial")
    icon_emoji = ui.config(config_group, 'icon_emoji', default=None)
    icon_url = ui.config(config_group, 'icon_url', default=None)

    return Config(token, org_name, repo_name, commit_url, username, icon_emoji,
                  icon_url)


def pushhook(node, source, ui, hooktype, repo, **kwargs):
    if source != 'push':
        return False

    config = get_config(ui)

    changesets = get_changesets(repo, node)
    count = len(changesets)
    messages = render_changesets(ui, repo, changesets, config)

    text = "{user} pushes {count} changeset{plural}: \n```{changes}```".format(
        user=ui.username(),
        count=count,
        plural="s" if count > 1 else "",
        changes=messages)

    post_message_to_slack(text, config)


def get_changesets(repo, node):
    node_rev = repo[node].rev()
    tip_rev = repo['tip'].rev()
    return range(tip_rev, node_rev - 1, -1)


def render_changesets(ui, repo, changesets, config):
    url = config.commit_url
    if url is None:
        node_template = "{node|short}"
    else:
        node_template = "<{url}{{node|short}}|{{node|short}}>".format(url=url)

    template = " | ".join([
        "{branch}",
        node_template,
        "{date(date, '%Y-%m-%d [%H:%M:%S]')}",
        "{desc|strip|firstline}",
    ]) + "\\n"

    displayer = show_changeset(ui, repo, {'template': template})
    ui.pushbuffer()
    for rev in changesets:
        displayer.show(repo[rev])
    return ui.popbuffer()


def post_message_to_slack(message, config):
    target_url = "https://{org_name}.slack.com/services/hooks/incoming-webhook?token={token}".format(
        org_name=config.org_name,
        token=config.token)
    payload = {
        'text': message,
        'username': config.username,
    }
    payload_optional_key(payload, config, 'icon_url')
    payload_optional_key(payload, config, 'icon_emoji')
    request = urllib2.Request(target_url, "payload=%s" % json.dumps(payload))
    urllib2.build_opener().open(request)


def payload_optional_key(payload, config, key):
    value = config.__getattribute__(key)
    if value:
        payload[key] = value
