import copy
import itertools

import scripts.terminal as terminal
import tests.harness.harness as harness
import config

class CheckSuite(harness.Suite):

  def __init__(self):
    self.checks = []
    self.check_rows = []
    self.args = []
    self.params = []

  def add_checks(self, checks, params, ranges):
    for args in itertools.product(*ranges):
      check_row = copy.deepcopy(checks)
      self.check_rows.append(check_row)
      self.checks += check_row
      self.params.append(params)
      self.args.append(args)

  def setup(self, verbose = "false", **kwargs):
    self.verbose = verbose;
    for check_row, params, args in zip(self.check_rows, self.params, self.args):
      for check in check_row:
        check.setup(flagss = [terminal.flags(params, args)], verbose=verbose, **kwargs)

  def get_command_list(self):
    command_list = []
    for check in self.checks:
      command_list += check.get_command_list()
    return command_list

  def parse_output_list(self, output_list):
    i = 0
    for check in self.checks:
      check.parse_output_list(output_list[i:i+check.get_num_commands()])
      i += check.get_num_commands()

  def get_header(self):
    return ["Check", "Res"]

  def get_align(self):
    return ["l", "c"]

  def get_dtype(self):
    return ["t", "t"]

  def get_cols_width(self, max_width):
    return [max_width - 2 - 3 - 4 - 2, 4]

  def get_rows(self):
    passed = 0
    failed = 0
    na = 0
    rows = []
    for check in self.checks:
      if check.get_result() == 0:
        if self.verbose == "true":
          rows.append([check.get_name(), "Pass"])
        passed += 1
      elif check.get_result() == 125:
        rows.append([check.get_name() + "\n\n" + check.get_output() + "\n\n" + "\n".join(check.get_command_list()), "N/A"])
        na += 1
      else:
        rows.append([check.get_name() + "\n\n({})\n\n".format(check.get_result()) + check.get_output() + "\n\n" + "\n".join(check.get_command_list()), "Fail"])
        failed += 1
    emoticon = ":("
    if passed == len(self.checks):
      emoticon = ":D"
    rows.append(["Passed: {0}/{3} Failed: {1}/{3} N/A: {2}/{3}".format(passed, failed, na, len(self.checks)), emoticon])
    return rows

  def get_output(self):
    return "\n".join(self.get_rows)

  def get_result(self):
    return "\n".join(self.get_rows)

class CheckTest(harness.ExecutableTest):

  def get_name(self):
    """
    return the name of the test
    """
    return self.name

  def get_command_list(self):
    """
    return a list of commands that constitute the test to be run on the
    target architecture
    """
    return ["{} {} {}".format(self.executable_output, self.base_flags, self.flagss[0]), "{} {} {}".format(self.executable_output, self.base_flags, self.flagss[0] + " -p")]

  def get_num_commands(self):
    return 2

  def parse_output_list(self, output_list):
    """
    parse the output of the command set. The output will be given as a list of
    (return code, output)
    """
    assert len(output_list) == 2, "ReproBLAS error: unexpected test output"
    self.output = output_list[0][1]
    self.result = output_list[0][0]
    self.name = output_list[1][1]

  def get_output(self):
    """
    return all relevant output (mostly for debugging)
    """
    return self.output

  def get_result(self):
    """
    return test result
    """
    return self.result

class ValidateInternalUFPTest(CheckTest):
  executable = "tests/checks/validate_internal_ufp"
  name = "validate_internal_ufp"

class ValidateInternalUFPFTest(CheckTest):
  executable = "tests/checks/validate_internal_ufpf"
  name = "validate_internal_ufpf"

class ValidateInternalDAMAXTest(CheckTest):
  executable = "tests/checks/validate_internal_damax"
  name = "validate_internal_damax"

class ValidateInternalZAMAXTest(CheckTest):
  executable = "tests/checks/validate_internal_zamax"
  name = "validate_internal_zamax"

class ValidateInternalSAMAXTest(CheckTest):
  executable = "tests/checks/validate_internal_samax"
  name = "validate_internal_samax"

class ValidateInternalCAMAXTest(CheckTest):
  executable = "tests/checks/validate_internal_camax"
  name = "validate_internal_camax"

class ValidateInternalRDSUMTest(CheckTest):
  base_flags = "-w rdsum"
  executable = "tests/checks/validate_internal_daugsum"
  name = "validate_internal_rdsum"

class ValidateInternalRDASUMTest(CheckTest):
  base_flags = "-w rdasum"
  executable = "tests/checks/validate_internal_daugsum"
  name = "validate_internal_rdasum"

class ValidateInternalRDNRM2Test(CheckTest):
  base_flags = "-w rdnrm2"
  executable = "tests/checks/validate_internal_daugsum"
  name = "validate_internal_rdrnm2"

class ValidateInternalRDDOTTest(CheckTest):
  base_flags = "-w rddot"
  executable = "tests/checks/validate_internal_daugsum"
  name = "validate_internal_rddot"

class ValidateInternalDBDBADDTest(CheckTest):
  base_flags = "-w dbdbadd"
  executable = "tests/checks/validate_internal_daugsum"
  name = "validate_internal_dbdbadd"

class ValidateInternalDIDADDTest(CheckTest):
  base_flags = "-w dbdadd"
  executable = "tests/checks/validate_internal_daugsum"
  name = "validate_internal_dbdadd"

class ValidateInternalDIDDEPOSITTest(CheckTest):
  base_flags = "-w dbddeposit"
  executable = "tests/checks/validate_internal_daugsum"
  name = "validate_internal_dbddeposit"

class ValidateInternalRZSUMTest(CheckTest):
  base_flags = "-w rzsum"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_rzsum"

class ValidateInternalRDZASUMTest(CheckTest):
  base_flags = "-w rdzasum"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_rdzasum"

class ValidateInternalRDZNRM2Test(CheckTest):
  base_flags = "-w rdznrm2"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_rdzrnm2"

class ValidateInternalRZDOTUTest(CheckTest):
  base_flags = "-w rzdotu"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_rzdotu"

class ValidateInternalRZDOTCTest(CheckTest):
  base_flags = "-w rzdotc"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_rzdotc"

class ValidateInternalZBZBADDTest(CheckTest):
  base_flags = "-w zbzbadd"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_zbzbadd"

class ValidateInternalZIZADDTest(CheckTest):
  base_flags = "-w zbzadd"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_zbzadd"

class ValidateInternalZIZDEPOSITTest(CheckTest):
  base_flags = "-w zbzdeposit"
  executable = "tests/checks/validate_internal_zaugsum"
  name = "validate_internal_zbzdeposit"

class ValidateInternalRSSUMTest(CheckTest):
  base_flags = "-w rssum"
  executable = "tests/checks/validate_internal_saugsum"
  name = "validate_internal_rssum"

class ValidateInternalRSASUMTest(CheckTest):
  base_flags = "-w rsasum"
  executable = "tests/checks/validate_internal_saugsum"
  name = "validate_internal_rsasum"

class ValidateInternalRSNRM2Test(CheckTest):
  base_flags = "-w rsnrm2"
  executable = "tests/checks/validate_internal_saugsum"
  name = "validate_internal_rsrnm2"

class ValidateInternalRSDOTTest(CheckTest):
  base_flags = "-w rsdot"
  executable = "tests/checks/validate_internal_saugsum"
  name = "validate_internal_rsdot"

class ValidateInternalSBSBADDTest(CheckTest):
  base_flags = "-w sbsbadd"
  executable = "tests/checks/validate_internal_saugsum"
  name = "validate_internal_sbsbadd"

class ValidateInternalSISADDTest(CheckTest):
  base_flags = "-w sbsadd"
  executable = "tests/checks/validate_internal_saugsum"
  name = "validate_internal_sbsadd"

class ValidateInternalSISDEPOSITTest(CheckTest):
  base_flags = "-w sbsdeposit"
  executable = "tests/checks/validate_internal_saugsum"
  name = "validate_internal_sbsdeposit"

class ValidateInternalRCSUMTest(CheckTest):
  base_flags = "-w rcsum"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_rcsum"

class ValidateInternalRSCASUMTest(CheckTest):
  base_flags = "-w rscasum"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_rscasum"

class ValidateInternalRSCNRM2Test(CheckTest):
  base_flags = "-w rscnrm2"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_rscrnm2"

class ValidateInternalRCDOTUTest(CheckTest):
  base_flags = "-w rcdotu"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_rcdotu"

class ValidateInternalRCDOTCTest(CheckTest):
  base_flags = "-w rcdotc"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_rcdotc"

class ValidateInternalCBCBADDTest(CheckTest):
  base_flags = "-w cbcbadd"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_cbcbadd"

class ValidateInternalCICADDTest(CheckTest):
  base_flags = "-w cbcadd"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_cbcadd"

class ValidateInternalCICDEPOSITTest(CheckTest):
  base_flags = "-w cbcdeposit"
  executable = "tests/checks/validate_internal_caugsum"
  name = "validate_internal_cbcdeposit"

class ValidateExternalRDSUMTest(CheckTest):
  base_flags = "-w rdsum"
  executable = "tests/checks/validate_external_rdblas1"
  name = "validate_external_rdsum"

class ValidateExternalRDASUMTest(CheckTest):
  base_flags = "-w rdasum"
  executable = "tests/checks/validate_external_rdblas1"
  name = "validate_external_rdasum"

class ValidateExternalRDNRM2Test(CheckTest):
  base_flags = "-w rdnrm2"
  executable = "tests/checks/validate_external_rdblas1"
  name = "validate_external_rdnrm2"

class ValidateExternalRDDOTTest(CheckTest):
  base_flags = "-w rddot"
  executable = "tests/checks/validate_external_rdblas1"
  name = "validate_external_rddot"

class ValidateExternalRZSUMTest(CheckTest):
  base_flags = "-w rzsum"
  executable = "tests/checks/validate_external_rzblas1"
  name = "validate_external_rzsum"

class ValidateExternalRDZASUMTest(CheckTest):
  base_flags = "-w rdzasum"
  executable = "tests/checks/validate_external_rzblas1"
  name = "validate_external_rdzasum"

class ValidateExternalRDZNRM2Test(CheckTest):
  base_flags = "-w rdznrm2"
  executable = "tests/checks/validate_external_rzblas1"
  name = "validate_external_rdznrm2"

class ValidateExternalRZDOTUTest(CheckTest):
  base_flags = "-w rzdotu"
  executable = "tests/checks/validate_external_rzblas1"
  name = "validate_external_rzdotu"

class ValidateExternalRZDOTCTest(CheckTest):
  base_flags = "-w rzdotc"
  executable = "tests/checks/validate_external_rzblas1"
  name = "validate_external_rzdotc"

class ValidateExternalRSSUMTest(CheckTest):
  base_flags = "-w rssum"
  executable = "tests/checks/validate_external_rsblas1"
  name = "validate_external_rssum"

class ValidateExternalRSASUMTest(CheckTest):
  base_flags = "-w rsasum"
  executable = "tests/checks/validate_external_rsblas1"
  name = "validate_external_rsasum"

class ValidateExternalRSNRM2Test(CheckTest):
  base_flags = "-w rsnrm2"
  executable = "tests/checks/validate_external_rsblas1"
  name = "validate_external_rsnrm2"

class ValidateExternalRSDOTTest(CheckTest):
  base_flags = "-w rsdot"
  executable = "tests/checks/validate_external_rsblas1"
  name = "validate_external_rsdot"

class ValidateExternalRCSUMTest(CheckTest):
  base_flags = "-w rcsum"
  executable = "tests/checks/validate_external_rcblas1"
  name = "validate_external_rcsum"

class ValidateExternalRSCASUMTest(CheckTest):
  base_flags = "-w rscasum"
  executable = "tests/checks/validate_external_rcblas1"
  name = "validate_external_rscasum"

class ValidateExternalRSCNRM2Test(CheckTest):
  base_flags = "-w rscnrm2"
  executable = "tests/checks/validate_external_rcblas1"
  name = "validate_external_rscnrm2"

class ValidateExternalRCDOTUTest(CheckTest):
  base_flags = "-w rcdotu"
  executable = "tests/checks/validate_external_rcblas1"
  name = "validate_external_rcdotu"

class ValidateExternalRCDOTCTest(CheckTest):
  base_flags = "-w rcdotc"
  executable = "tests/checks/validate_external_rcblas1"
  name = "validate_external_rcdotc"

class ValidateXBLASRDDOTTest(CheckTest):
  base_flags = "-w rddot"
  executable = "tests/checks/validate_xblas_ddot"
  name = "validate_xblas_rddot"

class ValidateXBLASRZDOTUTest(CheckTest):
  base_flags = "-w rzdotu"
  executable = "tests/checks/validate_xblas_zdot"
  name = "validate_xblas_rzdotu"

class ValidateXBLASRZDOTCTest(CheckTest):
  base_flags = "-w rzdotc"
  executable = "tests/checks/validate_xblas_zdot"
  name = "validate_xblas_rzdotc"

class ValidateXBLASRSDOTTest(CheckTest):
  base_flags = "-w rsdot"
  executable = "tests/checks/validate_xblas_sdot"
  name = "validate_xblas_rsdot"

class ValidateXBLASRCDOTUTest(CheckTest):
  base_flags = "-w rcdotu"
  executable = "tests/checks/validate_xblas_cdot"
  name = "validate_xblas_rcdotu"

class ValidateXBLASRCDOTCTest(CheckTest):
  base_flags = "-w rcdotc"
  executable = "tests/checks/validate_xblas_cdot"
  name = "validate_xblas_rcdotc"

class VerifyDBDBADDTest(CheckTest):
  base_flags = "-w dbdbadd"
  executable = "tests/checks/verify_daugsum"
  name = "verify_dbdbadd"

class VerifyDIDADDTest(CheckTest):
  base_flags = "-w dbdadd"
  executable = "tests/checks/verify_daugsum"
  name = "verify_dbdadd"

class VerifyDIDDEPOSITTest(CheckTest):
  base_flags = "-w dbddeposit"
  executable = "tests/checks/verify_daugsum"
  name = "verify_dbddeposit"

class VerifyRDSUMTest(CheckTest):
  base_flags = "-w rdsum"
  executable = "tests/checks/verify_daugsum"
  name = "verify_rdsum"

class VerifyRDASUMTest(CheckTest):
  base_flags = "-w rdasum"
  executable = "tests/checks/verify_daugsum"
  name = "verify_rdasum"

class VerifyRDNRM2Test(CheckTest):
  base_flags = "-w rdnrm2"
  executable = "tests/checks/verify_daugsum"
  name = "verify_rdnrm2"

class VerifyRDDOTTest(CheckTest):
  base_flags = "-w rddot"
  executable = "tests/checks/verify_daugsum"
  name = "verify_rddot"

class VerifyZBZBADDTest(CheckTest):
  base_flags = "-w zbzbadd"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_zbzbadd"

class VerifyZIZADDTest(CheckTest):
  base_flags = "-w zbzadd"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_zbzadd"

class VerifyZIZDEPOSITTest(CheckTest):
  base_flags = "-w zbzdeposit"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_zbzdeposit"

class VerifyRZSUMTest(CheckTest):
  base_flags = "-w rzsum"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_rzsum"

class VerifyRDZASUMTest(CheckTest):
  base_flags = "-w rdzasum"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_rdzasum"

class VerifyRDZNRM2Test(CheckTest):
  base_flags = "-w rdznrm2"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_rdznrm2"

class VerifyRZDOTUTest(CheckTest):
  base_flags = "-w rzdotu"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_rzdotu"

class VerifyRZDOTCTest(CheckTest):
  base_flags = "-w rzdotc"
  executable = "tests/checks/verify_zaugsum"
  name = "verify_rzdotc"

class VerifySBSBADDTest(CheckTest):
  base_flags = "-w sbsbadd"
  executable = "tests/checks/verify_saugsum"
  name = "verify_sbsbadd"

class VerifySISADDTest(CheckTest):
  base_flags = "-w sbsadd"
  executable = "tests/checks/verify_saugsum"
  name = "verify_sbsadd"

class VerifySISDEPOSITTest(CheckTest):
  base_flags = "-w sbsdeposit"
  executable = "tests/checks/verify_saugsum"
  name = "verify_sbsdeposit"

class VerifyRSSUMTest(CheckTest):
  base_flags = "-w rssum"
  executable = "tests/checks/verify_saugsum"
  name = "verify_rssum"

class VerifyRSASUMTest(CheckTest):
  base_flags = "-w rsasum"
  executable = "tests/checks/verify_saugsum"
  name = "verify_rsasum"

class VerifyRSNRM2Test(CheckTest):
  base_flags = "-w rsnrm2"
  executable = "tests/checks/verify_saugsum"
  name = "verify_rsnrm2"

class VerifyRSDOTTest(CheckTest):
  base_flags = "-w rsdot"
  executable = "tests/checks/verify_saugsum"
  name = "verify_rsdot"

class VerifyCBCBADDTest(CheckTest):
  base_flags = "-w cbcbadd"
  executable = "tests/checks/verify_caugsum"
  name = "verify_cbcbadd"

class VerifyCICADDTest(CheckTest):
  base_flags = "-w cbcadd"
  executable = "tests/checks/verify_caugsum"
  name = "verify_cbcadd"

class VerifyCICDEPOSITTest(CheckTest):
  base_flags = "-w cbcdeposit"
  executable = "tests/checks/verify_caugsum"
  name = "verify_cbcdeposit"

class VerifyRCSUMTest(CheckTest):
  base_flags = "-w rcsum"
  executable = "tests/checks/verify_caugsum"
  name = "verify_rcsum"

class VerifyRSCASUMTest(CheckTest):
  base_flags = "-w rscasum"
  executable = "tests/checks/verify_caugsum"
  name = "verify_rscasum"

class VerifyRSCNRM2Test(CheckTest):
  base_flags = "-w rscnrm2"
  executable = "tests/checks/verify_caugsum"
  name = "verify_rscnrm2"

class VerifyRCDOTUTest(CheckTest):
  base_flags = "-w rcdotu"
  executable = "tests/checks/verify_caugsum"
  name = "verify_rcdotu"

class VerifyRCDOTCTest(CheckTest):
  base_flags = "-w rcdotc"
  executable = "tests/checks/verify_caugsum"
  name = "verify_rcdotc"

class VerifyDIDSSQTest(CheckTest):
  executable = "tests/checks/verify_dbdssq"
  name = "verify_dbdssq"

class VerifyDIZSSQTest(CheckTest):
  executable = "tests/checks/verify_dbzssq"
  name = "verify_dbzssq"

class VerifySISSSQTest(CheckTest):
  executable = "tests/checks/verify_sbsssq"
  name = "verify_sbsssq"

class VerifySICSSQTest(CheckTest):
  executable = "tests/checks/verify_sbcssq"
  name = "verify_sbcssq"

class CorroborateRDGEMVTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rdgemv"
  name = "corroborate_rdgemv"

class CorroborateRZGEMVTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rzgemv"
  name = "corroborate_rzgemv"

class CorroborateRSGEMVTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rsgemv"
  name = "corroborate_rsgemv"

class CorroborateRCGEMVTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rcgemv"
  name = "corroborate_rcgemv"

class CorroborateRDGEMMTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rdgemm"
  name = "corroborate_rdgemm"

class CorroborateRZGEMMTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rzgemm"
  name = "corroborate_rzgemm"

class CorroborateRSGEMMTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rsgemm"
  name = "corroborate_rsgemm"

class CorroborateRCGEMMTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/corroborate_rcgemm"
  name = "corroborate_rcgemm"

class ValidateInternalDSCALETest(CheckTest):
  base_flags = ""
  executable = "tests/checks/validate_internal_dscale"
  name = "validate_internal_dscale"

class ValidateInternalSSCALETest(CheckTest):
  base_flags = ""
  executable = "tests/checks/validate_internal_sscale"
  name = "validate_internal_sscale"

class ValidateInternalDINDEXTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/validate_internal_dindex"
  name = "validate_internal_dindex"

class ValidateInternalSINDEXTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/validate_internal_sindex"
  name = "validate_internal_sindex"

class ValidateInternalDMINDEXTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/validate_internal_dmindex"
  name = "validate_internal_dmindex"

class ValidateInternalSMINDEXTest(CheckTest):
  base_flags = ""
  executable = "tests/checks/validate_internal_smindex"
  name = "validate_internal_smindex"
