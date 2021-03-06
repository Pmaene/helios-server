"""
Glue some events together
"""

from django.conf import settings
from django.core.urlresolvers import reverse
from django.conf import settings
import helios.views
import helios.signals

import views

# TODO This doesn't work for voters that are not also users

def vote_cast_send_message(user, voter, election, cast_vote, **kwargs):
    # Prepare the message
    subject = "%s - Cast Vote" % election.name

    body = """[An English-language version has been included below.]

Je stem in %s werd bewaard.

Je kan je biljet terugvinden op de volgende pagina:

    %s
""" % (election.name, helios.views.get_castvote_url(cast_vote))

    if election.use_voter_aliases:
        body += """
Deze verkiezing gebruikt een alias voor elke kiezer om je privacy te beschermen.
Je alias is: %s.
""" % voter.alias

    body += """
De vingerafdruk van je stem is: %s
""" % cast_vote.vote_hash

    body += """



"""

    body += """
You have successfully cast a vote in %s.

Your ballot is archived at:

    %s
""" % (election.name, helios.views.get_castvote_url(cast_vote))

    if election.use_voter_aliases:
        body += """
This election uses voter aliases to protect your privacy.
Your voter alias is: %s.
""" % voter.alias

    body += """
The fingerprint of your vote is: %s
""" % cast_vote.vote_hash

    body += """
--
%s
""" % settings.SITE_TITLE

    # send it via the notification system associated with the auth system
    user.send_message(subject, body)

helios.signals.vote_cast.connect(vote_cast_send_message)


def election_tallied(election, **kwargs):
    pass

helios.signals.election_tallied.connect(election_tallied)
