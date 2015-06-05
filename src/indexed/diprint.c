#include <indexed.h>

/**
 * @brief Print indexed double precision
 *
 * @param fold the fold of the indexed types
 * @param X indexed scalar X
 *
 * @author Hong Diep Nguyen
 * @author Peter Ahrens
 * @date   27 Apr 2015
 */
void diprint(const int fold, const double_indexed *X) {
  dmprint(fold, X, 1, X + fold, 1);
}
