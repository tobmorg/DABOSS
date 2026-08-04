#ifndef DEBIASING_H
#define DEBIASING_H

#include <vector>
#include <string>

struct body_data {
    std::string des;
    double a;
    double ecc;
    double inc;
    double peri;
    double node;
    double mag;
};

struct survey_data {
    double alpha_centre;
    double delta_centre;
    double D_alpha;
    double D_delta;
    double m_50;

    bool use_vitense_method;
};

struct probabilities {
    std::vector<double> probs_in_surveys;
    std::vector<std::vector<double> > prob_matrix;
};


probabilities debias (
    double acc_fac,
    const std::vector<double>& a_list,
    const std::vector<double>& ecc_list,
    const std::vector<double>& inc_list,
    const std::vector<double>& peri_list,
    const std::vector<double>& node_list,
    const std::vector<double>& mag_list,
    const std::vector<double>& alpha_centre_list,
    const std::vector<double>& delta_centre_list,
    const std::vector<double>& D_alpha_list,
    const std::vector<double>& D_delta_list,
    const std::vector<double>& m_50_list,
    const std::vector<bool>& check_vitense_list
);


std::vector<body_data> read_all_bodies (const std::string& filename, const char sep);
std::vector<survey_data> read_all_surveys (const std::string& filename, const char sep);



#endif
