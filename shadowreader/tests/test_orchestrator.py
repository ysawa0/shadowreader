"""
Copyright 2018 Edmunds.com, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
"""

from classes.app import App
from classes.mytime import MyTime
from libs import orchestrator


def test_init_apps_from_test_params():
    defaults = {
        'apps_to_test': ['test-app1', 'test-app2', 'test-app3'],
        'test_params': {
            "rate": 100,
            "loop_duration": 60,
            "replay_start_time": "2018-3-20-16-00",
            "base_url": "http://qa-www.pytest.com",
            "identifier": "qa",
        },
        "overrides": [],
        'timezone': 'US/Pacific'
    }

    apps = orchestrator.init_apps_from_test_params(defaults)
    app1 = apps[0]
    app2 = App(
        name='test-app1',
        replay_start_time=MyTime().from_epoch(
            epoch=1521586800, tzinfo='US/Pacific'),
        rate=100,
        base_url='http://qa-www.pytest.com',
        identifier='qa',
        loop_duration=60)

    assert app1 == app2 and len(apps) == 3


def test_init_apps_from_test_params_w_override():
    defaults = {
        'apps_to_test': ['test-app1', 'test-app2'],
        'test_params': {
            "rate": 100,
            "loop_duration": 60,
            "replay_start_time": "2018-3-20-16-00",
            "base_url": "http://qa-21-www.pytest.com",
            "identifier": "qa-21",
        },
        "overrides": [{
            "app": "test-app1",
            "rate": 50,
            "loop_duration": 30,
            "replay_start_time": "2018-3-20-17-00",
            "base_url": "http://qa-11-www.pytest.com",
            "identifier": "qa-11",
        }, {
            "app": "test-app2",
            "rate": 0,
            "loop_duration": 30,
            "replay_start_time": "2018-3-20-17-00",
            "base_url": "http://qa-11-www.pytest.com",
            "identifier": "qa-11",
        }],
        'timezone':
        'US/Pacific'
    }

    apps = orchestrator.init_apps_from_test_params(defaults)
    app1 = apps[0]
    app1_copy = App(
        name='test-app1',
        replay_start_time=MyTime(epoch=1521590400),
        rate=50,
        base_url='http://qa-11-www.pytest.com',
        identifier='qa-11',
        loop_duration=30)

    assert app1 == app1_copy and len(apps) == 1