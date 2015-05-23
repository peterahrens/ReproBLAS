import os

import tests.checks.checks as checks
import tests.harness.harness as harness

check_dir = os.path.dirname(os.path.abspath(__file__))

check_suite = checks.CheckSuite()

check_suite.add_checks([checks.ValidateInternalUFPTest(),\
                        checks.ValidateInternalUFPFTest()],\
                       ["N", "incX"],\
                       [[10], [1, 2, 4]])

check_suite.add_checks([checks.VerifyDINDEXTest(),\
                        checks.VerifySINDEXTest(),\
                        checks.VerifyDMINDEXTest(),\
                        checks.VerifySMINDEXTest()],\
                       ["N", "incX"],\
                       [[4], [1]])

check_suite.add_checks([checks.ValidateInternalDAMAXTest(),\
                        checks.ValidateInternalZAMAXTest(),\
                        checks.ValidateInternalSAMAXTest(),\
                        checks.ValidateInternalCAMAXTest()],\
                       ["N", "incX"],\
                       [[4095], [1, 2, 4]])

check_suite.add_checks([checks.ValidateInternalRDBLAS1Test(),\
                        checks.ValidateInternalRZBLAS1Test(),\
                        checks.ValidateInternalRSBLAS1Test(),\
                        checks.ValidateInternalRCBLAS1Test()],\
                       ["N", "incX", "incY"],\
                       [[4095], [1, 4], [1, 4]])

check_suite.add_checks([checks.ValidateInternalRDSUMTest(),\
                        checks.ValidateInternalDIDIADDTest(),\
                        checks.ValidateInternalDIDADDTest(),\
                        checks.ValidateInternalDIDDEPOSITTest(),\
                        ],\
                       ["N", "incX", "scaleX", "f"],\
                       [[4095], [1, 4], [0.0, 1.0],\
                        ["constant",\
                         "+inf",\
                         "++inf",\
                         "+-inf",\
                         "nan",\
                         "+inf_nan",\
                         "++inf_nan",\
                         "+big",\
                         "++big",\
                         "+-big",\
                         "sine"]])

check_suite.add_checks([checks.ValidateInternalRDSUMTest(),\
                        checks.ValidateInternalDIDIADDTest(),\
                        checks.ValidateInternalDIDADDTest(),\
                        checks.ValidateInternalDIDDEPOSITTest(),\
                        ],\
                       ["N", "incX", "ScaleX", "f"],\
                       [[64], [1, 4], [0.75 * 2.0**1023],\
                        ["sine"]])

check_suite.add_checks([checks.ValidateInternalRDASUMTest(),\
                        ],\
                       ["N", "incX", "ScaleX", "f"],\
                       [[64], [1, 4], [(0.75 * 2.0**1017)],\
                        ["constant"]])

check_suite.add_checks([checks.ValidateInternalRDNRM2Test(),\
                        ],\
                       ["N", "incX", "ScaleX", "f"],\
                       [[64], [1, 4], [(0.75 * 2.0**1019)],\
                        ["constant", "sine"]])

check_suite.add_checks([checks.ValidateInternalRDDOTTest(),\
                        ],\
                       ["N", "incX", "ScaleX", "f", "g"],\
                       [[64], [1, 4], [(0.75 * 2.0**1019)],\
                        ["sine"],\
                        ["sine"]])

"""
check_suite.add_checks([checks.VerifyRDSUMTest(),\
                        checks.VerifyRDASUMTest(),\
                        checks.VerifyDIDIADDTest(),\
                        checks.VerifyDIDADDTest(),\
                        checks.VerifyDIDDEPOSITTest(),\
                        checks.VerifyRZSUMTest(),\
                        checks.VerifyRDZASUMTest(),\
                        checks.VerifyZIZIADDTest(),\
                        checks.VerifyZIZADDTest(),\
                        checks.VerifyZIZDEPOSITTest(),\
                        checks.VerifyRSSUMTest(),\
                        checks.VerifyRSASUMTest(),\
                        checks.VerifySISIADDTest(),\
                        checks.VerifySISADDTest(),\
                        checks.VerifySISDEPOSITTest(),\
                        checks.VerifyRCSUMTest(),\
                        checks.VerifyRSCASUMTest(),\
                        checks.VerifyCICIADDTest(),\
                        checks.VerifyCICADDTest(),\
                        checks.VerifyCICDEPOSITTest()],\
                       ["N", "B", "incX", "f"],\
                       [[4095], [256], [1, 4],\
                        ["rand",\
                         "rand+(rand-1)",\
                         "sine",\
                         "small+grow*big"]])

check_suite.add_checks([checks.VerifyRDNRM2Test(),\
                        checks.VerifyRDZNRM2Test(),\
                        checks.VerifyRSNRM2Test(),\
                        checks.VerifyRSCNRM2Test()],\
                       ["N", "B", "incX", "f"],\
                       [[4095], [1], [1, 4],\
                        ["rand",\
                         "rand+(rand-1)",\
                         "sine",\
                         "small+grow*big"]])

check_suite.add_checks([checks.VerifyRDDOTTest(),\
                        checks.VerifyRZDOTUTest(),\
                        checks.VerifyRZDOTCTest(),\
                        checks.VerifyRSDOTTest(),\
                        checks.VerifyRCDOTUTest(),\
                        checks.VerifyRCDOTCTest()],\
                       ["N", "incX", "incY", "f", "g"],\
                       [[4095], [1, 4], [1, 4],\
                        ["rand",\
                         "rand+(rand-1)",\
                         "sine",\
                         "small+grow*big"],\
                        ["rand",\
                         "rand+(rand-1)",\
                         "sine",\
                         "small+grow*big"]])
"""

#check_suite.add_checks([checks.VerifyRDGEMVTest()],\
#                       ["O", "T", "N", "M", "lda", "incX", "incY", "f", "g", "j"],\
#                       [["RowMajor", "ColMajor"], ["NoTrans", "Trans"], [1023], [1023], [1023, 1025], [1, 4], [1, 4],\
#                        ["rand",\
#                         "small+grow*big"],\
#                        ["rand",\
#                         "small+grow*big"],\
#                        ["rand",\
#                         "small+grow*big"]])

check_harness = harness.Harness("check")
check_harness.add_suite(check_suite)
check_harness.run()
