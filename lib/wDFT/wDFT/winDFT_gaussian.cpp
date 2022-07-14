#include "pch.h"
#include "winDFT_Gaussian.h"
#include <cmath>
#include <iostream>


#pragma region Gaussian


double Sab(double a, double b, double rab) {
    double p = a + b;
    double q = a * b;
    double result = 2.828427 * pow(q/(p * p),0.75)*exp((-q*rab*rab)/p);
    return result;
}//Function computing integration of Xa a



#pragma endregion

int gaussian() {
    return 1;
}




int hello() {
    return 2;
}

