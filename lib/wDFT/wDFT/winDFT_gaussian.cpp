#include "pch.h"
#include "winDFT_Gaussian.h"
#include <cmath>
#include <iostream>
#include <vector>

#pragma warning(disable:6386)
using namespace std;


#pragma region Assist tools
double Rab(double* Ra, double* Rb) {
    double dx = Ra[0] - Rb[0];
    double dy = Ra[1] - Rb[1];
    double dz = Ra[2] - Rb[2];
    return sqrt(dx * dx + dy * dy + dz * dz);
}
void PR(double* a, int m) {
    for (int i = 0; i < m; i++) {
        cout << a[i] << endl;
    }
}
void PR(int* a, int m) {
    for (int i = 0; i < m; i++) {
        cout << a[i] << endl;
    }
}
#pragma endregion




#pragma region Gaussian Overlap Matrix

double* Sab(double* a,  double* pos, int* l, int* xyz, int m) {
    double rab;
    
    int num = m * m;
    double* Sab_Matrix = new double[num];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            
            rab = 0;
#pragma region Calculate overlap



            if (l[i] == 0 && l[j] == 0) {       //s to s
                Sab_Matrix[i * m + j] = S_ss(a[i], a[j], rab);
                continue;
            }
            if (l[i] == 0 && l[j] == 1) {       //s to p
                int direction = xyz[j];
                double rab_D = 0;
                Sab_Matrix[i * m + j] = S_sp(a[i], a[j], rab,rab_D);
                continue;
            }
            if (l[i] == 1 && l[j] == 0) {       //s to p
                int direction = xyz[i];
                double rab_D = 0;
                Sab_Matrix[i * m + j] = S_sp(a[j], a[i], rab, rab_D);
                continue;
            }
            if (l[i] == 1 && l[j] == 1) {       //p to p
                if (xyz[i] == xyz[j]) {         //same direction
                    int direction = xyz[i];
                    double rab_D = 0;
                    Sab_Matrix[i * m + j] = S_pxpx(a[j], a[i], rab, rab_D);
                    continue;
                }
                else
                {                               //diferenet direction
                    double rab_D1 = 0;
                    double rab_D2 = 0;
                    Sab_Matrix[i * m + j] = S_pxpy(a[j], a[i], rab, rab_D1, rab_D2);
                    continue;
                }
#pragma endregion
            }
        }
    }
    return Sab_Matrix;
    
}

double S_ss(double a, double b, double rab) {
    double p = a + b;
    double q = a * b;
    double result = 2.828427 * pow(q/(p * p),0.75)*exp((-q*rab*rab)/p);
    return result;
}//Function computing integration of Xa with s type and s type

double S_sp(double a, double b, double rab, double rab_D) {
    double p = a + b;
    double q = a * b;
    double a2 = a * a;
    double a4 = a2 * a2;
    double b2 = b * b;
    double b4 = b2 * b2;
    double result = 5.65685 * pow(a4*a2*a*b4*b, 0.25) * pow(p, -2.5)* rab_D * exp((-q * rab * rab) / p);
    return result;
}//Function computing integration of Xa with s type and p type

double S_pxpx(double a, double b, double rab, double rab_D) {
    double p = a + b;
    double q = a * b;
    double p2 = p * p;
    double p4 = p2 * p2;
    double p6 = p2 * p4;
    double q2 = q * q;
    double q4 = q2 * q2;
    
    double result = 11.3137 * pow(q*q4/(p6), 0.25) * (0.5/p+(q/p2) * rab_D * rab_D)* exp((-q * rab * rab) / p);
    return result;
}//Function computing integration of Xa with px type and px type

double S_pxpy(double a, double b, double rab, double rab_D1,double rab_D2) {
    double p = a + b;
    double q = a * b;
    double p2 = p * p;
    double p4 = p2 * p2;
    double p6 = p2 * p4;
    double q2 = q * q;
    double q4 = q2 * q2;

    double result = 11.3137 * pow(q * q4 / (p6), 0.25) * (q / p2) * rab_D1 * rab_D2 * exp((-q * rab * rab) / p);
    return result;
}//Function computing integration of Xa with px type and px type

#pragma endregion



