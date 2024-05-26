typedef enum
{
    not_recomended_low_fp_correct_force = 0,
    optimal = 1,
    suboptimal-high-finger-placement = 2,
    suboptimal-left-centered = 3,
    undetermined = 4,
}dtc_t;

/*
 * \brief Decision tree classifier
 * 
 * Decision tree classifier based on the following input characteristics:
 *   BLOCK_SIZE: 100
 *   BLOCK_TYPE: SLIDING
 * 
 * \return dtc_t
 *   0  not_recomended_low_fp_correct_force
 *   1  optimal
 *   2  suboptimal-high-finger-placement
 *   3  suboptimal-left-centered
 *   4  undetermined
 */
dtc_t dtc(const float FP3_max, const float FP5_min, const float FP2_variance, const float FP8_max)
{
    dtc_t ret;

    if(FP8_max <= 3361.500000f)
    {
        if(FP3_max <= 172.000000f)
        {
             ret = undetermined;
        }
        else // FP3_max > 172.000000f
        {
            if(FP5_min <= 188.500000f)
            {
                if(FP2_variance <= 0.983150f)
                {
                     ret = suboptimal-high-finger-placement;
                }
                else // FP2_variance > 0.983150f
                {
                     ret = not_recomended_low_fp_correct_force;
                }
            }
            else // FP5_min > 188.500000f
            {
                 ret = optimal;
            }
        }
    }
    else // FP8_max > 3361.500000f
    {
         ret = suboptimal-left-centered;
    }

    return ret;
}
