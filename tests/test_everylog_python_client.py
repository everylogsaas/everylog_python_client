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

    def test_notify(self):
        options = {
            'api_key': 'API_KEY',
            'projectId': 'PROJECT_ID',
            'everylog_url': 'https://api.everylog.io/api/v1/log-entries'
        }
        self.client = EverylogPythonClient()
        self.client.setup(options) 
        notify_options = {
            'title': 'Test Title',
            'summary': 'Test Summary',
            'body': 'Test Body',
            'tags': ['tag1', 'tag2'],
            'link': 'https://example.com',
            'push': True,
            'icon': '',
            'externalChannels': [],
            'properties': {},
        }

        expected_data = {'body': 'Test Body', 'icon': '', 'id': '644965f31150dc0f426948ce', 'projectId': 'Testing-Project-id', 'properties': {}, 'push': True, 'starred': [], 'summary': 'Test Summary', 'tags': [], 'title': 'Test Title'}
        expected_status_code = 200

        with mock.patch("requests.post") as mock_post:
            mock_response = mock.Mock()
            mock_response.json.return_value = expected_data
            mock_response.status_code = expected_status_code
            mock_post.return_value = mock_response

            response = self.client.notify(notify_options)

            mock_post.assert_called_once_with(
                self.client.SETUP_DEFAULTS["everylog_url"],
                data=mock.ANY,
                headers=mock.ANY
            )

            self.assertEqual(mock_response.status_code, expected_status_code)
            self.assertEqual(response, expected_data)

    def test_notify_with_invalid_token(self):
            options = {
                'api_key': 'INVALID_API_KEY',
                'projectId': 'PROJECT_ID',
                'everylog_url': 'https://api.everylog.io/api/v1/log-entries'
            }
            self.client = EverylogPythonClient()
            self.client.setup(options) 
            notify_options = {
                'title': 'Test Title',
                'summary': 'Test Summary',
                'body': 'Test Body',
                'tags': ['tag1', 'tag2'],
                'link': 'https://example.com',
                'push': True,
                'icon': '',
                'externalChannels': [],
                'properties': {},
            }

            expected_data = { 'message': 'You are not authorized to perform this action' }
            expected_status_code = 401
            
            with mock.patch("requests.post") as mock_post:
                mock_response = mock.Mock()
                mock_response.json.return_value = expected_data
                mock_response.status_code = expected_status_code
                mock_post.return_value = mock_response

                response = self.client.notify(notify_options)

                mock_post.assert_called_once_with(
                    self.client.SETUP_DEFAULTS["everylog_url"],
                    data=mock.ANY,
                    headers=mock.ANY
                )

                self.assertEqual(mock_response.status_code, expected_status_code)
                self.assertEqual(response, expected_data)
