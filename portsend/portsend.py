# Copyright (C) 2019 Jan Felix Langenbach
#
# This file is part of portsend.
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
# along with this program.  If not, see <http: //www.gnu.org/licenses/>.
"""The main library of portsend."""

from __future__ import annotations
from typing import List
import socket


def send(files: List[str], port: int = 1199):
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", port))  # TODO Port configurable
        sock.listen()
        print(f"Listening on {socket.gethostname()}:{sock.getsockname()[1]}")
        conn, addr = sock.accept()
        print(conn, addr)


def receive(host: str, port: int):
    pass
