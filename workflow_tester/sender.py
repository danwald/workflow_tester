import logging
import sys
import click
import requests

import content

logger = logging.getLogger(__name__)


@click.command()
@click.option('-t', '--to', required=True)
@click.option('-f', '--frm', required=True)
@click.option('-b', '--body', required=True)
@click.option('-a', '--account-sid', default='1234')
@click.option('-s', '--sms-sid', default='5678')
@click.option('-u', '--sms-status', default=3, show_default=3)
@click.option('-u', '--url', default='http://localhost:8000/testMessage/', show_default=True)
@click.option('-h', '--headers', default=None, show_default=True)
def main(to, frm, body, account_sid, sms_sid, sms_status, url, headers):
    """Console script for workflow_tester."""
    message = content.Message(
        To=to, From=frm, Body=body, AccountSid=account_sid, SmsSid=sms_sid, SmsStatus=sms_status
    )
    logger.debug(f'{message} --> {url}')
    response = requests.post(
        url,
        data=message.json(),
        headers={'Content-type': 'application/json', 'Accept': 'text/plain'}
    )
    logger.debug(f'response: {response.status_code} {response.json()}')


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
