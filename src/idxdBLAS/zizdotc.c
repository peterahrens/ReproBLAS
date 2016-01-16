/*
 *  Created   13/10/25   H.D. Nguyen
 */

#include "idxdBLAS.h"

/**
 * @brief Compute indexed complex double precision conjugated dot product Z of complex double precision vectors X and Y
 *
 * Set Z to the indexed sum of the pairwise products of X and conjugated Y.
 *
 * @param N vector length
 * @param X complex double precision vector
 * @param incX X vector stride (use every incX'th element)
 * @param Y complex double precision vector
 * @param incY Y vector stride (use every incX'th element)
 * @param scalar return Z
 *
 * @author Peter Ahrens
 * @date   15 Jan 2016
 */
void idxdBLAS_zizdotc(const int fold, const int N, const void *X, const int incX, const void *Y, const int incY, double_complex_indexed *Z){
  idxdBLAS_zmzdotc(fold, N, X, incX, Y, incY, Z, 1, Z + 2 * fold, 1);
}
