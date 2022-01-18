# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-节点管理(BlueKing-BK-NODEMAN) available.
Copyright (C) 2017-2022 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import os
import platform
import stat
import subprocess

from django.conf import settings

from apps.backend.exceptions import GseEncryptedError
from apps.node_man import constants

BACKEND_PLATFORM = f"{platform.system().lower()}_{platform.machine().lower()}"

default_platform = f"{constants.OsType.LINUX.lower()}_{constants.CpuType.x86_64.lower()}"
grabbed_platform_path = os.path.join(
    settings.PROJECT_ROOT, "script_tools", "encryptedpasswd", BACKEND_PLATFORM, "encryptedpasswd"
)
platform_path = default_platform if not os.path.isfile(grabbed_platform_path) else BACKEND_PLATFORM
encrypted_tools_path = os.path.join(
    settings.PROJECT_ROOT, "script_tools", "encryptedpasswd", platform_path, "encryptedpasswd"
)

# 增加可执行权限
if not os.access(encrypted_tools_path, os.X_OK):
    os.chmod(encrypted_tools_path, os.stat(encrypted_tools_path).st_mode | stat.S_IXGRP)


class GseEncrypted(object):
    @classmethod
    def encrypted(cls, key, debug=False):
        command = [encrypted_tools_path, "-encrypt", key]
        if debug:
            command.extend("-v")
        result = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8")
        secret_key = result.stdout.read().strip()
        return_code = result.poll() == 0
        if return_code and secret_key:
            return secret_key
        else:
            raise GseEncryptedError(context=("GSE敏感信息加密失败: {}".format(result.stderr.read())))
