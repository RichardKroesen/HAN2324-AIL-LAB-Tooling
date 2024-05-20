typedef enum
{
    not_recomended_low_fp_correct_force = 0,
    not_recomended_too_little_force_correct_fp = 1,
    optimal = 2,
    suboptimal_high_finger_placement = 3,
    suboptimal_left_centered = 4,
    suboptimal_too_much_force = 5,
    undetermined = 6,
}dtc_t;

/*
 * \brief Decision tree classifier
 * 
 * Decision tree classifier based on the following input characteristics:
 *   BLOCK_SIZE: 10
 *   BLOCK_TYPE: SLIDING
 * 
 * \return dtc_t
 *   0  not_recomended_low_fp_correct_force
 *   1  not_recomended_too_little_force_correct_fp
 *   2  optimal
 *   3  suboptimal_high_finger_placement 
 *   4  suboptimal_left_centered
 *   5  suboptimal_too_much_force
 *   6  undetermined
 */
dtc_t dtc(const float FP5_variance, const float FP1_raw, const float FP4_mean, const float FP8_raw, const float FP6_raw, const float ToF_mean, const float FP7_mean, const float FP7_raw, const float FP8_mean, const float FP6_mean, const float FP2_raw, const float FP1_mean, const float FP3_mean, const float FP5_mean, const float FP3_variance)
{
    dtc_t ret;

    if(FP1_mean <= 184.500000f)
    {
        if(FP4_mean <= 171.699997f)
        {
             ret = undetermined;
        }
        else // FP4_mean > 171.699997f
        {
            if(FP8_mean <= 294.099991f)
            {
                if(FP7_raw <= 180.500000f)
                {
                    if(FP1_mean <= 174.849998f)
                    {
                        if(FP5_variance <= 0.270000f)
                        {
                            if(FP3_mean <= 171.199997f)
                            {
                                 ret = not_recomended_too_little_force_correct_fp;
                            }
                            else // FP3_mean > 171.199997f
                            {
                                 ret = optimal;
                            }
                        }
                        else // FP5_variance > 0.270000f
                        {
                            if(FP8_raw <= 180.500000f)
                            {
                                if(FP7_raw <= 179.500000f)
                                {
                                    if(FP8_raw <= 179.500000f)
                                    {
                                         ret = optimal;
                                    }
                                    else // FP8_raw > 179.500000f
                                    {
                                        if(FP7_raw <= 176.500000f)
                                        {
                                             ret = suboptimal_high_finger_placement ;
                                        }
                                        else // FP7_raw > 176.500000f
                                        {
                                             ret = optimal;
                                        }
                                    }
                                }
                                else // FP7_raw > 179.500000f
                                {
                                    if(FP1_mean <= 174.349998f)
                                    {
                                         ret = optimal;
                                    }
                                    else // FP1_mean > 174.349998f
                                    {
                                         ret = not_recomended_too_little_force_correct_fp;
                                    }
                                }
                            }
                            else // FP8_raw > 180.500000f
                            {
                                if(FP1_mean <= 174.300003f)
                                {
                                     ret = optimal;
                                }
                                else // FP1_mean > 174.300003f
                                {
                                     ret = suboptimal_high_finger_placement ;
                                }
                            }
                        }
                    }
                    else // FP1_mean > 174.849998f
                    {
                        if(FP6_mean <= 3733.649902f)
                        {
                            if(FP2_raw <= 179.500000f)
                            {
                                if(FP3_mean <= 169.949997f)
                                {
                                     ret = suboptimal_too_much_force;
                                }
                                else // FP3_mean > 169.949997f
                                {
                                     ret = suboptimal_high_finger_placement ;
                                }
                            }
                            else // FP2_raw > 179.500000f
                            {
                                 ret = suboptimal_too_much_force;
                            }
                        }
                        else // FP6_mean > 3733.649902f
                        {
                            if(FP6_raw <= 3705.500000f)
                            {
                                if(ToF_mean <= 49.150000f)
                                {
                                     ret = suboptimal_high_finger_placement ;
                                }
                                else // ToF_mean > 49.150000f
                                {
                                     ret = suboptimal_too_much_force;
                                }
                            }
                            else // FP6_raw > 3705.500000f
                            {
                                if(FP1_mean <= 175.399994f)
                                {
                                    if(FP3_variance <= 773242.407494f)
                                    {
                                         ret = optimal;
                                    }
                                    else // FP3_variance > 773242.407494f
                                    {
                                         ret = not_recomended_too_little_force_correct_fp;
                                    }
                                }
                                else // FP1_mean > 175.399994f
                                {
                                    if(FP6_mean <= 3760.599976f)
                                    {
                                        if(FP8_mean <= 178.849998f)
                                        {
                                             ret = suboptimal_too_much_force;
                                        }
                                        else // FP8_mean > 178.849998f
                                        {
                                             ret = suboptimal_high_finger_placement ;
                                        }
                                    }
                                    else // FP6_mean > 3760.599976f
                                    {
                                        if(FP7_mean <= 175.050003f)
                                        {
                                             ret = suboptimal_too_much_force;
                                        }
                                        else // FP7_mean > 175.050003f
                                        {
                                            if(FP5_variance <= 26.024996f)
                                            {
                                                //  #warning truncated branch of depth 2
                                            }
                                            else // FP5_variance > 26.024996f
                                            {
                                                 ret = suboptimal_too_much_force;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                else // FP7_raw > 180.500000f
                {
                    if(FP5_mean <= 3212.050049f)
                    {
                        if(FP1_mean <= 175.699997f)
                        {
                            if(FP4_mean <= 178.349998f)
                            {
                                 ret = optimal;
                            }
                            else // FP4_mean > 178.349998f
                            {
                                if(ToF_mean <= 44.750000f)
                                {
                                     ret = suboptimal_high_finger_placement ;
                                }
                                else // ToF_mean > 44.750000f
                                {
                                     ret = not_recomended_too_little_force_correct_fp;
                                }
                            }
                        }
                        else // FP1_mean > 175.699997f
                        {
                            if(FP1_mean <= 176.099998f)
                            {
                                 ret = suboptimal_too_much_force;
                            }
                            else // FP1_mean > 176.099998f
                            {
                                if(FP4_mean <= 3448.500000f)
                                {
                                     ret = suboptimal_left_centered;
                                }
                                else // FP4_mean > 3448.500000f
                                {
                                     ret = suboptimal_too_much_force;
                                }
                            }
                        }
                    }
                    else // FP5_mean > 3212.050049f
                    {
                        if(FP1_raw <= 175.000000f)
                        {
                             ret = optimal;
                        }
                        else // FP1_raw > 175.000000f
                        {
                             ret = suboptimal_too_much_force;
                        }
                    }
                }
            }
            else // FP8_mean > 294.099991f
            {
                if(FP1_mean <= 175.949997f)
                {
                    if(FP7_mean <= 197.500000f)
                    {
                        if(FP6_raw <= 3347.000000f)
                        {
                             ret = suboptimal_high_finger_placement ;
                        }
                        else // FP6_raw > 3347.000000f
                        {
                             ret = suboptimal_too_much_force;
                        }
                    }
                    else // FP7_mean > 197.500000f
                    {
                         ret = optimal;
                    }
                }
                else // FP1_mean > 175.949997f
                {
                    if(FP7_raw <= 221.000000f)
                    {
                        if(FP5_variance <= 338.905029f)
                        {
                             ret = suboptimal_high_finger_placement ;
                        }
                        else // FP5_variance > 338.905029f
                        {
                             ret = suboptimal_too_much_force;
                        }
                    }
                    else // FP7_raw > 221.000000f
                    {
                         ret = suboptimal_left_centered;
                    }
                }
            }
        }
    }
    else // FP1_mean > 184.500000f
    {
         ret = not_recomended_low_fp_correct_force;
    }

    return ret;
}
