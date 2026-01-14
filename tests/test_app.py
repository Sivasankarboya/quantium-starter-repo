import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app("app")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None


def test_visualisation_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    dropdown = dash_duo.find_element("#region-picker")
    assert dropdown is not None
