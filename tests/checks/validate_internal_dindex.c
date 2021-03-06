#include <binnedBLAS.h>
#include <binned.h>
#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <math.h>

#include "../common/test_vecvec_header.h"
#include "../common/test_util.h"


int vecvec_show_help(void){
  return 0;
}

const char* vecvec_name(int argc, char** argv) {
  (void)argc;
  (void)argv;
  return "Verify dindex";
}

int vecvec_test(int argc, char** argv, int N, int incX, int incY) {
  (void)argc;
  (void)argv;
  (void)incY;
  int i;
  int index;

  util_random_seed();

  //allocate vector
  double *X = util_dvec_alloc(N*(DBL_MAX_EXP - DBL_MIN_EXP) + 1, incX);

  //check
  for (i = 0; i < (DBL_MAX_EXP - DBL_MIN_EXP) * N; i++) {
    X[i * incX] = ldexp(0.5 + 0.5 * util_drand(), (i/N) + DBL_MIN_EXP);
  }
  X[i * incX] = 0.0;
  for (i = 0; i < N * (DBL_MAX_EXP - DBL_MIN_EXP) + 1; i++) {
    index = binned_dindex(X[i * incX]);
    if (index == 0){
      X[i * incX] *= binned_DMCOMPRESSION;
    }
    if (X[i * incX] != 0.0 && *binned_dmbins(index) / ldexp(0.75, DBL_MANT_DIG) > 2 * fabs(X[i * incX])){
      printf("2 * |X| !>= 2^(i * W)\n");
      printf("2 * %g !>= %g\n", fabs(X[i * incX]), *binned_dmbins(index + 1)/ldexp(0.75, DBL_MANT_DIG - DBWIDTH));
      return 1;
    }
    if (*binned_dmbins(index) / ldexp(0.75, DBL_MANT_DIG - DBWIDTH) <= 2 * fabs(X[i * incX])){
      printf("2 * |X| !< 2^((i + 1) * W)\n");
      printf("2 * %g !< %g\n", fabs(X[i * incX]), *binned_dmbins(index)/ldexp(0.75, DBL_MANT_DIG - DBWIDTH));
      return 1;
    }
  }
  free(X);
  return 0;
}
