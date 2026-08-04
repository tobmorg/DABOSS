#ifndef GENERATE_ORBIT_POINTS_H
#define GENERATE_ORBIT_POINTS_H

#include <vector>
#include <array>

std::vector<std::array<double, 5> > generate_orbit_points(
    int n, 
    double ecc, 
    double a, 
    double inc, 
    double peri, 
    double node);


#endif