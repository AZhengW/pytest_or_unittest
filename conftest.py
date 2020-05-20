import pytest


def pytest_collection_modifyitems(session, config, items: list):
    # 自动加标签
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        if 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
