/*
 *  Created   13/10/25   H.D. Nguyen
 */

#include "indexedBLAS.h"

void idxdBLAS_cicdotc(const int fold, const int N, const void *X, const int incX, const void *Y, const int incY, float_complex_indexed *Z){
  idxdBLAS_cmcdotc(fold, N, X, incX, Y, incY, Z, 1, Z + 2 * fold, 1);
}
