#!/usr/bin/env python

"""Tests for `workflow_tester` package."""

import pytest

from click.testing import CliRunner

from workflow_tester import workflow_tester
from workflow_tester import receiver
from workflow_tester import sender


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_receiver_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(receiver.main)
    assert result.exit_code == 0
    assert 'workflow_tester.receiver.main' in result.output
    help_result = runner.invoke(receiver.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_sender_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(sender.main)
    assert result.exit_code == 0
    assert 'workflow_tester.sender.main' in result.output
    help_result = runner.invoke(sender.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
