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
    commit_url = http://example.com/101-sandbox/rev/
    icon_emoji = :mercurial:

    [hooks]
    changegroup.slackhooks= python:/path/to/slackhooks.py:pushhook

Example of chat message output:

.. image:: http://i.imgur.com/Ivcctgq.png
    :alt: Mercurial push hook chat message
    :align: center

Options
~~~~~~~

#. ``org_name`` is the name of your organization. *It's obligatory and it's a part of your unique webhook URL.*
#. ``token`` is your API token. Currenlty token is given per channel, so you do not have to set channel name manually.
   *It's obligatory and it's a part of your unique webhook URL.*
#. ``repo_name`` is a name of your repository. *It's optional.*
