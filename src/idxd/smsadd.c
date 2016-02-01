#include <idxd.h>

/**
 * @internal
 * @brief  Add single precision to manually specified indexed single precision (Y += X)
 *
 * Performs the operation Y += X on an indexed type Y
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
void idxd_smsadd(const int fold, const float X, float *priY, const int incpriY, float *carY, const int inccarY){
  idxd_smsupdate(fold, X, priY, incpriY, carY, inccarY);
  idxd_smsdeposit(fold, X, priY, incpriY);
  idxd_smrenorm(fold, priY, incpriY, carY, inccarY);
}
