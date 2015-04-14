#
# python duplicate_trustees.py <source_election_uuid> <destination_election_uuid>
#

import os
import sys
import uuid

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from helios.models import *
import copy

source_election_uuid = sys.argv[1]
destination_election_uuid = sys.argv[2]

source_election = Election.objects.get(uuid=source_election_uuid)
destination_election = Election.objects.get(uuid=destination_election_uuid)

trustees = source_election.trustee_set.exclude(public_key=None)

for trustee in trustees:
    destination_trustee = copy.deepcopy(trustee)

    destination_trustee.id = None
    destination_trustee.uuid = uuid.uuid1()
    destination_trustee.election = destination_election
    destination_trustee.save()

threshold_scheme = ThresholdScheme.objects.get(election=source_election)

destination_threshold_scheme = copy.deepcopy(threshold_scheme)

destination_threshold_scheme.id = None
destination_threshold_scheme.election = destination_election

destination_threshold_scheme.save()

destination_election.frozen_trustee_list = True
destination_election.encrypted_shares_uploaded = True
destination_election.save()
