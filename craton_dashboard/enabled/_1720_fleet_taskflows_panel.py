# Copyright 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


PANEL = 'fleet.taskflows'

PANEL_DASHBOARD = 'project'

PANEL_GROUP = 'fleet_management'

ADD_PANEL = (
    'craton_dashboard.content.fleet_management.taskflows.panel.Taskflows')

ADD_INSTALLED_APPS = ['craton_dashboard', ]

ADD_ANGULAR_MODULES = ['horizon.dashboard.project.fleet_management']

AUTO_DISCOVER_STATIC_FILES = True
