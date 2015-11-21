%module ImgCmpLib

%include "std_string.i"
%include "std_vector.i"


%{
#include "ImgCmp.h"
%}


namespace std {
%template(vector_ImgDiff) vector<ImgDiff>;
}

%include "ImgCmp.h"
