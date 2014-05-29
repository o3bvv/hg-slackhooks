hg-slackhooks
=============

Mercurial server-side hooks for Slack messaging service.

Examples
~~~~~~~~

To add push hooks for some repo, modify ``.hg/hgrc`` in the central repository::

    [slackhooks]
    org_name = YOUR_ORGANIZATION_NAME
    token = CHANNEL_TOKEN
    repo_name = sample repository
    commit_url = http://46.149.83.248:2080/hg/home/hg/101-discounts-website-test/rev/
    icon_emoji = :mercurial:

    [hooks]
    changegroup.slackhooks= python:/path/to/slackhooks.py:pushhook

Here ``org_name`` are ``token`` obligatory.

.. note:: currenlty ``token`` is given per channel, so you do not have to set channel name manually.

``repo_name`` is optional.
