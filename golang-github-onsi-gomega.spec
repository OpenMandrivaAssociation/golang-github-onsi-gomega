# http://github.com/onsi/gomega

%global goipath         github.com/onsi/gomega
%global commit          2152b45fa28a361beba9aab0885972323a444e28


%gometa -i

Name:           %{goname}
Version:        1.0
Release:        0.7%{?dist}
Summary:        Ginkgo's Preferred Matcher Library
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/golang/protobuf/proto)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0-0.6.git2152b45
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.5.git2152b45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.4.git2152b45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.3.git2152b45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.2.git2152b45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0-0.1.git2152b45
- Bump to upstream 2152b45fa28a361beba9aab0885972323a444e28
  related: #1248013

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.9.git8adf9e1
- Polish spec file, enable devel and unit-test for epel7
  related: #1248013

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git8adf9e1
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git8adf9e1
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git8adf9e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git8adf9e1
- internal packages are no longer provided
  related: #1248013

* Wed Jul 29 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.1.git8adf9e1
- Update of spec file to spec-2.0
  resolves: #1248013

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git8adf9e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git8adf9e1
- Bump to upstream 8adf9e1730c55cdc590de7d49766cb2acc88d8f2
  related: #1148452

* Mon Oct 13 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.gita0ee4df
- BuildArch to ExclusiveArch

* Wed Oct 01 2014 root - 0-0.1.git90d6a47
- First package for Fedora

