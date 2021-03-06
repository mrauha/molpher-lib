
# Copyright (c) 2016 Martin Sicho
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

VERSION = None
BUILD_NUMBER = None
PYTHON_VERSION_MAJOR = sys.version_info.major
PYTHON_VERSION_MINOR = sys.version_info.minor
PYTHON_VERSION = '{0}.{1}'.format(PYTHON_VERSION_MAJOR, PYTHON_VERSION_MINOR)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_versionfile(path):
    with open(path, 'r') as versionfile:
        return versionfile.read().strip()

VERSION = load_versionfile(os.path.join(BASE_DIR, "VERSION.TXT"))
BUILD_NUMBER = load_versionfile(os.path.join(BASE_DIR, "BUILD.TXT"))

print('Version: ', VERSION)
print('Build: ', BUILD_NUMBER)
print('Python Version: ', BUILD_NUMBER)