# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Place:
    def custom_device_id(self) -> int: ...
    def custom_device_type(self) -> str: ...
    def gpu_device_id(self) -> int: ...
    def ipu_device_id(self) -> int: ...
    def is_cpu_place(self) -> bool: ...
    def is_cuda_pinned_place(self) -> bool: ...
    def is_custom_place(self) -> bool: ...
    def is_gpu_place(self) -> bool: ...
    def is_ipu_place(self) -> bool: ...
    def is_xpu_place(self) -> bool: ...
    def set_place(self, place: Place) -> None: ...
    def xpu_device_id(self) -> int: ...

class CPUPlace(Place): ...

class CUDAPlace(Place):
    def __init__(self, id: int, /) -> None: ...

class CUDAPinnedPlace(Place): ...

class NPUPlace(Place):
    def __init__(self, id: int, /) -> None: ...

class IPUPlace(Place): ...

class CustomPlace(Place):
    def __init__(self, name: str, id: int, /) -> None: ...

class MLUPlace(Place):
    def __init__(self, id: int, /) -> None: ...

class XPUPlace(Place):
    def __init__(self, id: int, /) -> None: ...