#pragma once
#include <iostream>
#ifdef MATHLIBRARY_EXPORTS
#define MATHLIBRARY_API __declspec(dllexport)
#else
#define MATHLIBRARY_API __declspec(dllimport)

#endif


extern "C" MATHLIBRARY_API int hello();