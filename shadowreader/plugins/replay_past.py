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
from classes.mytime import MyTime
from libs import s3


def main(**kwargs):
    cur_timestamp = kwargs.get('app_cur_timestamp', None)
    app = kwargs.get('app_name', '')

    cur_timestamp = MyTime.from_epoch(epoch=cur_timestamp, tzinfo='UTC')

    s3_parsed_data_key = s3._generate_s3_key(
        mytime=cur_timestamp, app_name=app)
    return s3_parsed_data_key