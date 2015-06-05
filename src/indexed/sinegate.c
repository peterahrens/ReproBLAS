#include <indexed.h>

/**
 * @brief Negate indexed single precision (X = -X)
 *
 * Performs the operation X = -X
 *
 * @param fold the fold of the indexed types
 * @param X indexed scalar X
 *
 * @author Hong Diep Nguyen
 * @author Peter Ahrens
 * @date   27 Apr 2015
 */
void sinegate(const int fold, float_indexed* X){
  smnegate(fold, X, 1, X + fold, 1);
}
