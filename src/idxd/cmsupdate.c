#include <idxd.h>

/**
 * @internal
 * @brief Update manually specified indexed complex single precision with single precision (X -> Y)
 *
 * This method updates Y to an index suitable for adding numbers with absolute value less than X
 *
 * @param fold the fold of the indexed types
 * @param X scalar X
 * @param priY Y's primary vector
 * @param incpriY stride within Y's primary vector (use every incpriY'th element)
 * @param carY Y's carry vector
 * @param inccarY stride within Y's carry vector (use every inccarY'th element)
 *
 * @author Hong Diep Nguyen
 * @author Peter Ahrens
 * @date   27 Apr 2015
 */
void idxd_cmsupdate(const int fold, const float X, float* priY, const int incpriY, float* carY, const int inccarY) {
  idxd_smsupdate(fold, X, priY, 2 * incpriY, carY, 2 * inccarY);
  idxd_smsupdate(fold, X, priY + 1, 2 * incpriY, carY + 1, 2 * inccarY);
}
