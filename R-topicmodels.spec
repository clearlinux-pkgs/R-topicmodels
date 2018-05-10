#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-topicmodels
Version  : 0.2.7
Release  : 8
URL      : https://cran.r-project.org/src/contrib/topicmodels_0.2-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/topicmodels_0.2-7.tar.gz
Summary  : Topic Models
Group    : Development/Tools
License  : GPL-2.0
Requires: R-topicmodels-lib
Requires: R-modeltools
Requires: R-slam
Requires: R-tm
BuildRequires : R-modeltools
BuildRequires : R-slam
BuildRequires : R-tm
BuildRequires : clr-R-helpers
BuildRequires : gsl-dev

%description
Allocation (LDA) models and Correlated Topics Models
	     (CTM) by David M. Blei and co-authors and the C++ code
	     for fitting LDA models using Gibbs sampling by Xuan-Hieu
	     Phan and co-authors.

%package lib
Summary: lib components for the R-topicmodels package.
Group: Libraries

%description lib
lib components for the R-topicmodels package.


%prep
%setup -q -c -n topicmodels

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521269610

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521269610
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library topicmodels
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library topicmodels
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library topicmodels
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library topicmodels|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/topicmodels/CITATION
/usr/lib64/R/library/topicmodels/DESCRIPTION
/usr/lib64/R/library/topicmodels/INDEX
/usr/lib64/R/library/topicmodels/Meta/Rd.rds
/usr/lib64/R/library/topicmodels/Meta/data.rds
/usr/lib64/R/library/topicmodels/Meta/features.rds
/usr/lib64/R/library/topicmodels/Meta/hsearch.rds
/usr/lib64/R/library/topicmodels/Meta/links.rds
/usr/lib64/R/library/topicmodels/Meta/nsInfo.rds
/usr/lib64/R/library/topicmodels/Meta/package.rds
/usr/lib64/R/library/topicmodels/Meta/vignette.rds
/usr/lib64/R/library/topicmodels/NAMESPACE
/usr/lib64/R/library/topicmodels/NEWS.Rd
/usr/lib64/R/library/topicmodels/R/topicmodels
/usr/lib64/R/library/topicmodels/R/topicmodels.rdb
/usr/lib64/R/library/topicmodels/R/topicmodels.rdx
/usr/lib64/R/library/topicmodels/data/AssociatedPress.rda
/usr/lib64/R/library/topicmodels/doc/index.html
/usr/lib64/R/library/topicmodels/doc/topicmodels.R
/usr/lib64/R/library/topicmodels/doc/topicmodels.Rnw
/usr/lib64/R/library/topicmodels/doc/topicmodels.pdf
/usr/lib64/R/library/topicmodels/help/AnIndex
/usr/lib64/R/library/topicmodels/help/aliases.rds
/usr/lib64/R/library/topicmodels/help/paths.rds
/usr/lib64/R/library/topicmodels/help/topicmodels.rdb
/usr/lib64/R/library/topicmodels/help/topicmodels.rdx
/usr/lib64/R/library/topicmodels/html/00Index.html
/usr/lib64/R/library/topicmodels/html/R.css
/usr/lib64/R/library/topicmodels/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/topicmodels/libs/topicmodels.so
/usr/lib64/R/library/topicmodels/libs/topicmodels.so.avx2
/usr/lib64/R/library/topicmodels/libs/topicmodels.so.avx512
