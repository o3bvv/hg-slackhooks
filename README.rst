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
#. ``commit_url`` is a part of URL for parcilular changeset. If it is specified, link to a changeset will be inserted in description of changeset. Plain text short revision number will be used otherwise.
#. ``username`` is the displayed name. Default: ``mercurial``.
#. ``icon_emoji`` is the name of emoticon, which will be displayed. *It's optional.* You can use ``icon_url`` instead.
#. ``icon_url`` is a direct link to image, which will be displayed. *It's optional.*
