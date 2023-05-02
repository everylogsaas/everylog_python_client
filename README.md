# everylog_python_client

EveryLog provides a simple way to receive notifications for important application events that you choose.

## Installation

The distribution is hosted on pypi at: '#'. To directly install the package from pypi, run from your terminal::

    $ pip install everylog_python_client

# Usage

## Setup

This is to be set once globally (instantiated) from within the project.

```py
from everylog.everylog_python_client import EveryLogPythonClient

client = EveryLogPythonClient()
client.setup(api_key='<YOUR_API_KEY>', projectId='<YOUR_PROJECT_NAME>')

```

# Notifying the logs whenever you choose to.

Uses the instantiated object from the class and notify by setting different options.

```

# @param [Dictionary] notify_options
# @option notify_options [String, options[:projectId]]  :projectId name of the project
# @option notify_options [String]  :title to display in the application and if enabled in the notification
# @option notify_options [String]  :summary is a not so long text to display on the application and if enabled in the notification
# @option notify_options [String]  :body it can contain a long text simple formatted, no html to display in the application
# @option notify_options [Array]   :tags it can be used to categorize the notification, must be strings
# @option notify_options [String]  :link it can be used to display on the application and if enabled in the notification
# @option notify_options [Boolean] :push if True, a push notification is sent to application
# @option notify_options [String]  :icon
# @option notify_options [Array]   :externaChannels
# @option notify_options [Dictionary] :properties
# @option notify_options [Array]   :groups

client.notify({...notify_options})

```

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the EveryLog python client project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/everylogsaas/everylog_python_client/blob/master/CODE_OF_CONDUCT.md).