%global packname  kinship2
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.3.7
Release:          2
Summary:          Pedigree functions
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/kinship2_1.3.7.tar.gz
Requires:         R-Matrix R-quadprog 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-Matrix R-quadprog

%description
Routines to handle family data with a pedigree object. The initial purpose
was to create correlation structures that describe family relationships
such as kinship and identity-by-descent, which can be used to model family
data in mixed effects models, such as in the coxme function.  Also
includes a tool for pedigree drawing which is focused on producing compact
layouts without intervention.  Recent additions include utilities to trim
the pedigree object with various criteria.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/GPL2.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
