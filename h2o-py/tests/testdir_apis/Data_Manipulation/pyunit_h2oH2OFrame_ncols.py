from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils

def h2o_H2OFrame_ncols():
    """
    Python API test: h2o.frame.H2OFrame.ncols
    """
    iris = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris_wheader_NA_2.csv"))
    assert iris.ncols==5, "h2o.H2OFrame.ncol command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_ncols())
else:
    h2o_H2OFrame_ncols()
