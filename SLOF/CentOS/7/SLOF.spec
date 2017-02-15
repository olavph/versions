%global commit          ba46a3f133c8532a517779cc3763e8ac2409d626
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gitcommittag    .git%{shortcommit}

Name:           SLOF
Version:        20161019
Release:        4%{gitcommittag}%{?dist}
Summary:        Slimline Open Firmware

License:        BSD
URL:            http://www.openfirmware.info/SLOF
BuildArch:      noarch

Source0:        %{name}.tar.gz

# LTC: building native; no need for xcompiler
BuildRequires:  perl(Data::Dumper)


%description
Slimline Open Firmware (SLOF) is initialization and boot source code
based on the IEEE-1275 (Open Firmware) standard, developed by
engineers of the IBM Corporation.

The SLOF source code provides illustrates what's needed to initialize
and boot Linux or a hypervisor on the industry Open Firmware boot
standard.

Note that you normally wouldn't need to install this package
separately.  It is a dependency of qemu-system-ppc64.


%prep
%setup -q -n %{name}

if test -r "gitlog" ; then
    echo "This is the first 50 lines of a gitlog taken at archive creation time:"
    head -50 gitlog
    echo "End of first 50 lines of gitlog."
fi

%build
export CROSS=""
make qemu %{?_smp_mflags} V=2


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/qemu
cp -a boot_rom.bin $RPM_BUILD_ROOT%{_datadir}/qemu/slof.bin


%files
%doc FlashingSLOF.pdf
%doc LICENSE
%doc README
%dir %{_datadir}/qemu
%{_datadir}/qemu/slof.bin


%changelog
* Wed Feb 15 2017 fabianorosas <farosas@linux.vnet.ibm.com> - 20161019-4.gitba46a3f
- ba46a3f133c8532a517779cc3763e8ac2409d626 Remove superfluous checkpoints in tree.fs
- a0b96fe66fcd991b407c1d67ca842921e477a6fd Provide write function in the disk-label package
- 264553932ba3cee4b7472838daaecfaaa61c91da virtio: Implement block write support
- eee0d12dc541dd345d7931976e352ea5a6494155 scsi: Add SCSI block write support
- abd21203aa27435e9e5248350dcaf14940de0947 deblocker: Add a write function
- 9290756ae1195b331373dbcfd3b37d978b3b71f4 virtio-scsi: Fix descriptor order for SCSI WRITE commands
- 9b8945ecbde65b06ea2ab9e28a6178024b0420fb board-qemu: Add a possibility to use hvterm input instead of USB keyboard
- 38bf852e73ce6f0ac801dfe8ef1545c4cd0b5ddb Do not try to use virtio-gpu in VGA mode
- b294381e48ed9c3300e7aea4c4ba7f17729ffd9f virtio: Fix stack comment of virtio-blk-read
- 7412f9e058132a9218827c23369b8cba33d756af envvar: Do not read default values for /options from the NVRAM anymore
- 32568e8e1119e3308b3c97d4a290fd5e8a273e11 envvar: Set properties in /options during (set-defaults)

* Wed Feb  8 2017 Nikunj A. Dadhania <nikunj@linux.vnet.ibm.com> - 20161019
- Pull upstream SLOF present in qemu 2.8

* Thu Nov 3 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 20160525-3
- Spec cleanup

* Tue Aug 30 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 20160525-2.1
- Build August, 24th, 2016

* Tue Sep 10 2013 baseuser@ibm.com
- Base-8.x spec file
