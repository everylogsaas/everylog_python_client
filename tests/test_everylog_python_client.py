import unittest
from evelylog.everylog_python_client import EverylogPythonClient
from unittest import mock


class TestEverylogPythonClient(unittest.TestCase):
    def test_setup(self):
        options = {
            'api_key': 'API_KEY',
            'projectId': 'PROJECT_ID',
            'everylog_url': 'https://api.everylog.io/api/v1/log-entries'
        }
        self.client = EverylogPythonClient()
        self.client.setup(options) 
        self.assertEqual(self.client.options['api_key'], 'API_KEY')
        self.assertEqual(self.client.options['projectId'], 'PROJECT_ID')
        self.assertEqual(self.client.options['everylog_url'], 'https://api.everylog.io/api/v1/log-entries')

    def test_create_log_entry(self):
        options = {
            'api_key': 'API_KEY',
            'projectId': 'PROJECT_ID',
            'everylog_url': 'https://api.everylog.io/api/v1/log-entries'
        }
        self.client = EverylogPythonClient()
        self.client.setup(options) 
        log_entry_options = {
            'title': 'Test Title',
            'summary': 'Test Summary',
            'body': 'Test Body',
            'tags': ['tag1', 'tag2'],
            'link': 'https://example.com',
            'push': True,
            'icon': '',
            'externalChannels': [],
            'properties': [{}],
        }

        expected_status_code = 200

        with mock.patch("requests.post") as mock_post:
            mock_response = mock.Mock()
            mock_response.status_code = expected_status_code
            mock_post.return_value = mock_response

            response = self.client.create_log_entry(log_entry_options)

            mock_post.assert_called_once_with(
                self.client.SETUP_DEFAULTS["everylog_url"],
                data=mock.ANY,
                headers=mock.ANY
            )

            self.assertEqual(mock_response.status_code, expected_status_code)

    def test_create_log_entry_with_invalid_token(self):
            options = {
                'api_key': 'INVALID_API_KEY',
                'projectId': 'PROJECT_ID',
            }
            self.client = EverylogPythonClient()
            self.client.setup(options) 
            log_entry_options = {
                'title': 'Test Title',
                'summary': 'Test Summary',
                'body': 'Test Body',
                'tags': ['tag1', 'tag2'],
                'link': 'https://example.com',
                'push': True,
                'icon': '',
                'externalChannels': [],
                'properties': [{}],
            }

            expected_data = { 'message': 'You are not authorized to perform this action' }
            expected_status_code = 401
            
            with mock.patch("requests.post") as mock_post:
                mock_response = mock.Mock()
                mock_response.json.return_value = expected_data
                mock_response.status_code = expected_status_code
                mock_post.return_value = mock_response

                response = self.client.create_log_entry(log_entry_options)

                mock_post.assert_called_once_with(
                    self.client.SETUP_DEFAULTS["everylog_url"],
                    data=mock.ANY,
                    headers=mock.ANY
                )

                self.assertEqual(mock_response.status_code, expected_status_code)
                self.assertEqual(response, expected_data)
