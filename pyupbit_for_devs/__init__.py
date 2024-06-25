"""
pyupbit-for-devs package:
   Copyright 2024 Sanghoon Lee (DSsoli). All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Modifications, Additions, and Deletions:
    - Additions: trade_utils.py for Robust API/Function Calls
    - Deletions: pyupbit's custom error handlings
    - Modifications: functions in quotation_api.py, request_api.py, and exchange_api.py,
        in order to show raw and detailed response from Upbit API directly for debugging purposes.

Base code for pyupbit-for-devs package (pyupbit):
   Copyright 2021 Jonghun Yoo, Brayden Jo, pystock/pyquant (sharebook-kr). All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


from .trade_utils import TradeUtils
from .exchange_api import *
from .quotation_api import *
from .request_api import *
from .websocket_api import WebSocketManager
from .websocket_api import WebSocketClient

# pyupbit PyPi (setup.py) __version__ = "0.2.34"

__version__ = "0.1.0"