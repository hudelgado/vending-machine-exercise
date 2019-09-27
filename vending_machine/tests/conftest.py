import os
import tempfile

import pytest
from vending_machine import create_app
from vending_machine.db import get_db, init_db, load_sample

@pytest.fixture
def app():
  """A new app instance with sample data."""
  db_fd, db_file = tempfile.mkstemp()
  app = create_app({'DATABASE': 'sqlite:///%s' % db_file, 'TESTING': True})
  with app.app_context():
    init_db()
    load_sample()
  yield app
  os.close(db_fd)
  os.unlink(db_file)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
