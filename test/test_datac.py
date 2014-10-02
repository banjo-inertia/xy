# -*- coding: utf-8 -*-
import datac
import numpy as np
import os

params = {"temp_sun": 6000.}
bandgaps = np.linspace(0, 3.25, 100)

abscissae = datac.generate_abscissae(bandgaps, "bandgap", params)
pwd = os.getcwd()
testdir = "test"
filename = "data.dat"

fqpn = os.path.join(pwd, testdir, filename)
datac.write_json(fqpn, abscissae)
