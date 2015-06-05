#include <indexed.h>

/**
 * @internal
 * @brief Renormalize manually specified indexed complex single precision
 *
 * Renormalization keeps the mantissa vector within the necessary bins by shifting over to the carry vector
 *
 * @param fold the fold of the indexed types
 * @param manX X's mantissa vector
 * @param incmanX stride within X's mantissa vector (use every incmanX'th element)
 * @param carX X's carry vector
 * @param inccarX stride within X's carry vector (use every inccarX'th element)
 *
 * @author Hong Diep Nguyen
 * @author Peter Ahrens
 * @date   27 Apr 2015
 */
void cmrenorm(const int fold, float* manX, const int incmanX, float* carX, const int inccarX) {
  smrenorm(fold, manX, 2 * incmanX, carX, 2 * inccarX);
  smrenorm(fold, manX + 1, 2 * incmanX, carX + 1, 2 * inccarX);
}
