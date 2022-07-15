#pragma once
#ifndef GAUSSIAN_H
#define GAUSSIAN_H
#ifndef EXPORT_FUNC
#define EXPORT_FUNC  _declspec(dllexport)
#endif // !EXPORT_FUNC
#include <vector>
using namespace std;
#pragma region GAUSSIAN
extern "C" EXPORT_FUNC double* Sab(double* a, double* pos, int* l, int* xyz, int m);
double S_ss(double a, double b, double rab);
double S_sp(double a, double b, double rab, double rab_D);
double S_pxpx(double a, double b, double rab, double rab_D);
double S_pxpy(double a, double b, double rab, double rab_D1, double rab_D2);
class STO_NG {

    public:
        STO_NG(int n, double* para, double* standard_alpha, double coeff);
        int n;
        vector<double> para;
        vector<double> alpha;
};
#pragma endregion










#endif // !GAUSSIAN_H
