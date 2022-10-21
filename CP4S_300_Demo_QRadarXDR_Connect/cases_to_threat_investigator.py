#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Action Module circuits component to send cases to threat investigator
"""
import logging

from circuits.core.handlers import handler
from requests.auth import HTTPBasicAuth
from resilient_circuits.actions_component import (ActionMessage,
                                                  ResilientComponent)
from resilient_lib import RequestsCommon, make_payload_from_template

LOG = logging.getLogger(__name__)

# name of the config section where this lives
CONFIG_DATA_SECTION = "send_to_threat_investigator_component"

"""
Example config section in component app.config file. 
All information needed in this python is set in component app.config fileself.

[resilient]
cafile = false

# where the component file will live
componentsdir=/var/rescircuits/components 

[send_to_threat_investigator_component]
# same msg dest that the rule is configured to post to
queue=l300_xdr_ti 
# Cloud Pak Host, change for each 
cp4s_base_host=https://deployment-9pnitj.test.cloudpak.security.ibm.com
cp4s_ti_endpoint=/api/advisor/v1/config/mock/investigations
# API Key from Cloud Pak Hamburger Menu > API Key. 
cp4s_api_key=58cc5965
# Sort the secret of the API Key in a Secret in the App Config pane
cp4s_api_secret=$CP4SAPIKEYSECRET
# path and name of the json tempate used
path_json_template=/var/rescircuits/ti_template.json.jinja2

"""


class CasesToThreatInvestigator(ResilientComponent):

    def __init__(self, opts):
        super(CasesToThreatInvestigator, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # The queue name can be specified in the config file under this component "queue"
        self.channel = "actions." + self.options.get("queue")

    @handler("l300_xdr_ti") # NAME OF ACTION (MAKE SURE ALL LOWERCASE AND NO SPACES)
    def _incident_created(self, event, *args, **kwargs):
        """The @handler() annotation without an event name makes this
           a default handler - for all events on this component's queue.
           This will be called with some "internal" events from Circuits,
           so you must declare the method with the generic parameters
           (event, *args, **kwargs), and ignore any messages that are not
           from the Action Module.
        """
        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        # for external rest requests
        rc = RequestsCommon(self.opts, self.options)

        # grab information from the event
        source_case = event.message["incident"]
        source_case_id = source_case.get("id")
        source_case_org = source_case.get("org_id")
        source_case_timestamp = source_case.get("create_date") - (1000*60*10)
        source_case_timestamp_end = source_case.get("create_date") - (1000*60*10) + 544415
        source_case_timestamp_303605 = source_case.get("create_date") - (1000*60*10) + 303605
        source_case_timestamp_476495 = source_case.get("create_date") - (1000*60*10) + 476495
        source_case_timestamp_73539 = source_case.get("create_date") - (1000*60*10) + 73539
        source_case_timestamp_3665 = source_case.get("create_date") - (1000*60*10) + 3665
        source_case_timestamp_43522 = source_case.get("create_date") - (1000*60*10) + 43522
        source_case_timestamp_228615 = source_case.get("create_date") - (1000*60*10) + 228615

        LOG.info(source_case_id, source_case_org)

        cp4s_url = self.options.get("cp4s_base_host")
        cp4s_resource_endpoint = self.options.get("cp4s_ti_endpoint")
        cp4s_api_key = self.options.get("cp4s_api_key")
        cp4s_api_secret = self.options.get("cp4s_api_secret")
        template_path = self.options.get("path_json_template")

        jinja_payload = {
            "case_id": source_case_id,
            "org_id": source_case_org,
            "create_date": source_case_timestamp,
            "end_date": source_case_timestamp_end,
            "date_303605": source_case_timestamp_303605,
            "date_476495": source_case_timestamp_476495,
            "date_73539": source_case_timestamp_73539,
            "date_3665": source_case_timestamp_3665,
            "date_43522": source_case_timestamp_43522,
            "date_228615": source_case_timestamp_228615
        }
        ti_payload = make_payload_from_template(None, template_path, jinja_payload)
        ti_headers = {
            "Content-Type": "application/json"
        }

        rc.execute("POST", cp4s_url + cp4s_resource_endpoint,
                   json=ti_payload,
                   auth=HTTPBasicAuth(cp4s_api_key, cp4s_api_secret),
                   headers=ti_headers)
