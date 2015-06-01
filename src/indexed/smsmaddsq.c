#include <indexed.h>

/**
 * @internal
 * @brief Add manually specified indexed single precision sacled sums of squares (Y += X)
 *
 * Performs the operation Y += X, where X and Y represent scaled sums of squares.
 *
 * @param fold the fold of the indexed types
 * @param manX X's mantissa vector
 * @param incmanX stride within X's mantissa vector (use every incmanX'th element)
 * @param carX X's carry vector
 * @param inccarX stride within X's carry vector (use every inccarX'th element)
 * @param scaleX scale of X (scaleX == sscale(Z) for some @c float Z)
 * @param manY Y's mantissa vector
 * @param incmanY stride within Y's mantissa vector (use every incmanY'th element)
 * @param carY Y's carry vector
 * @param inccarY stride within Y's carry vector (use every inccarY'th element)
 * @param scaleY scale of Y (scaleY == sscale(Z) for some @c double Z)
 *
 * @return updated scale of Y
 *
 * @author Peter Ahrens
 * @date   1 Jun 2015
 */
float smsmaddsq(const int fold, const float *manX, const int incmanX, const float *carX, const int inccarX, const float scaleX, float* manY, const int incmanY, float* carY, const int inccarY, const float scaleY) {
  if (scaleX > scaleY){
    smrescale(fold, scaleX, manY, incmanY, carY, inccarY, scaleY);
    smsmadd(fold, manX, incmanX, carX, inccarX, manY, incmanY, carY, inccarY);
    return scaleX;
  }else if(scaleX == scaleY){
    smsmadd(fold, manX, incmanX, carX, inccarX, manY, incmanY, carY, inccarY);
    return scaleX;
  }else{
    float_indexed tmp_X = sialloc(fold);
    smsmset(fold, manX, incmanX, carX, inccarX, tmp_X, 1, tmp_X + fold, 1);
    smrescale(fold, scaleY, tmpX, 1, tmpX + fold, 1, scaleX);
    smsmadd(fold, tmp_X, 1, tmp_X + fold, 1, manY, incmanY, carY, inccarY);
    return scaleY;
  }
}
