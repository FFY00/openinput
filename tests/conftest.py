# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Filipe Laíns <lains@riseup.net>

import unittest.mock

import pages
import pytest
import testsuite


@pytest.fixture()
def device(request):
    return testsuite.Device(
        name='test device',
        functions=request.param,
    )


@pytest.fixture()
def basic_device():
    device = testsuite.Device(
        name='basic test device',
        functions={
            pages.Info.VERSION,
            pages.Info.FW_INFO,
            pages.Info.SUPPORTED_FUNCTION_PAGES,
            pages.Info.SUPPORTED_FUNCTIONS,
        },
    )
    device.hid_send = unittest.mock.MagicMock()
    return device
