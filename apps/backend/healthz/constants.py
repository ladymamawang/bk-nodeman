# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-节点管理(BlueKing-BK-NODEMAN) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""


HEALTHZ_FIELD_NAMES = [
    "node_name",
    "description",
    "category",
    "collect_metric",
    "collect_args",
    "collect_type",
    "metric_alias",
    "solution",
]


class CheckerStatus(object):
    """
    指标检查状态码
    0：指标状态正常
    1：警告
    2：指标状态异常
    3：指标检查流程未找到
    4：检查流程报错
    """

    CHECKER_OK = 0
    CHECKER_WARN = 1
    CHECKER_FAILED = 2
    CHECKER_NOT_FOUND = 3
    CHECKER_ERROR = 4
