#include <reproBLAS.h>
#include <indexedBLAS.h>

#include "../../config.h"

double rdasum(const int N, const double* X, const int incX) {
  double_indexed *asumi = idxd_dialloc(DIDEFAULTFOLD);
  double asum;

  idxd_disetzero(DIDEFAULTFOLD, asumi);

  idxdBLAS_didasum(DIDEFAULTFOLD, N, X, incX, asumi);

  asum = idxd_ddiconv(DIDEFAULTFOLD, asumi);
  free(asumi);
  return asum;
}

