#ifndef CALC_OBS_PROB_H
#define CALC_OBS_PROB_H 

#include <vector>

struct ra_dec_coords {
    std::vector<double> r;
    std::vector<double> ra;
    std::vector<double> dec;
};

ra_dec_coords calc_ra_dec(
    const std::vector< std::array<double, 3> >& coords);



double calc_obs_prob(   int n,
                        const ra_dec_coords& ra_dec,
                        double d_alpha,
                        double d_delta,
                        double ra_centre,
                        double dec_centre,
                        double mag,
                        double m50);



#endif