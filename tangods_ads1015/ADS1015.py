#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-


# Copyright (C) 2020  MBI-Division-B
# MIT License, refer to LICENSE file
# Author: Martin Hennecke / Email: hennecke@mbi-berlin.de

from tango.server import run, Device
from tango.server import attribute, command
from tango import DevState, AttrWriteType

from ads1015 import ADS1015 as ads1015


class ADS1015(Device):
    ADC0 = attribute(
        label="ADC0",
        dtype="float",
        access=AttrWriteType.READ,
        unit="V",
        format="%8.4f",
    )

    ADC1 = attribute(
        label="ADC1",
        dtype="float",
        access=AttrWriteType.READ,
        unit="V",
        format="%8.4f",
    )

    def init_device(self):
        Device.init_device(self)

        self.__ads1015 = ads1015()
        self.__ads1015.set_mode("single")
        self.__ads1015.set_programmable_gain(2.048)
        self.__ads1015.set_sample_rate(1600)

        self.__reference = self.__ads1015.get_reference_voltage()

        self.set_state(DevState.ON)

    @command(dtype_out="float")
    def read_ADC0(self):
        return self.__ads1015.get_compensated_voltage(
            channel="in0/in3", reference_voltage=self.__reference
        )

    @command(dtype_out="float")
    def read_ADC1(self):
        return self.__ads1015.get_compensated_voltage(
            channel="in1/in3", reference_voltage=self.__reference
        )
