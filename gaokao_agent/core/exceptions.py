# Copyright 2025-2026 Gaokao Volunteer Agent Contributors
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

"""自定义异常"""


class GaokaoAgentError(Exception):
    """基础异常"""
    pass


class DataQualityError(GaokaoAgentError):
    """数据质量异常"""
    pass


class MissingFieldError(GaokaoAgentError):
    """缺失必要字段异常"""
    pass


class PolicyNotFoundError(GaokaoAgentError):
    """政策数据未找到异常"""
    pass


class RiskBlockingError(GaokaoAgentError):
    """风险审查阻断异常"""
    pass


class DataSourceError(GaokaoAgentError):
    """数据源异常"""
    pass


class ValidationError(GaokaoAgentError):
    """校验异常"""
    pass
