import sqlite3, pytest, tempfile, os

from vending_machine import create_app
from vending_machine.db import get_db, init_db, load_sample
from vending_machine.models import Product

def test_get_close_db(app):
  with app.app_context():
    db = get_db()
    assert db is get_db()

def test_init_db_command(runner, monkeypatch):
  class Recorder(object):
    called = False

  def fake_init_db():
    Recorder.called = True

  monkeypatch.setattr('vending_machine.db.init_db', fake_init_db)
  result = runner.invoke(args=['init-db'])
  assert 'Initialized' in result.output
  assert Recorder.called

def test_load_sample_command(runner, monkeypatch):
  class Recorder(object):
    called = False

  def fake_load_sample():
    Recorder.called = True

  monkeypatch.setattr('vending_machine.db.load_sample', fake_load_sample)
  result = runner.invoke(args=['load-sample'])
  assert 'Loaded' in result.output
  assert Recorder.called