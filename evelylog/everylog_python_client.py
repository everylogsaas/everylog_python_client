# evelylog_client.py
import json
import requests

class EverylogPythonClient:
    SETUP_DEFAULTS = {
        "api_key": None,
        "projectId": None,
        "everylog_url": "https://api.everylog.io/api/v1/log-entries"
    }

    LOG_ENTRY_DEFAULTS = {
        "title": "Empty notification",
        "summary": "Empty summary",
        "body": "Empty body",
        "tags": [],
        "link": "",
        "push": False,
        "icon": "",
        "externalChannels": [],
        "properties": {},
        "groups": [],
    }

    def __init__(self):
        self.options = None
        self.log_entry_options = None

    def setup(self, options=None):
        self.options = self._parse_options(options or {}, self.SETUP_DEFAULTS)
        return self

    def create_log_entry(self, log_entry_options=None):
        self.log_entry_options = self._parse_options(log_entry_options or {}, self.LOG_ENTRY_DEFAULTS)
        
        merged_options = {**{"projectId": self.options["projectId"]}, **self.log_entry_options}

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.options["api_key"])
        }

        response = requests.post(self.options["everylog_url"], data=json.dumps(merged_options), headers=headers)
        return response.json()

    def _parse_options(self, options, defaults_to_dup):
        defaults = defaults_to_dup.copy()
        result_parsed_options = options.copy()

        for key in defaults.keys():
            if callable(defaults[key]):
                defaults[key] = defaults[key]()
            if key in result_parsed_options.keys():
                result_parsed_options[key] = result_parsed_options[key]
            else:
                result_parsed_options[key] = defaults[key]

        return result_parsed_options