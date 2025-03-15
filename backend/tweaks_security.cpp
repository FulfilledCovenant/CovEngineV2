#include <iostream>
#include <string>
#include <Windows.h>
#include "nlohmann/json.hpp"
#include "tweaks.h"

using json = nlohmann::json;

bool AK_RA(const json& params) {
    std::cout << "Restricting anonymous access..." << std::endl;
    
    DWORD value = 1;
    bool success1 = MY(
        "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa",
        "RestrictAnonymous",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 1;
    bool success2 = MY(
        "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa",
        "RestrictAnonymousSAM",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_RS(const json& params) {
    std::cout << "Restricting anonymous enumeration of shares..." << std::endl;
    
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa",
        "RestrictAnonymous",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_SF(const json& params) {
    std::cout << "Disabling SmartScreen Filter..." << std::endl;
    
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
        "EnableSmartScreen",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer",
        "SmartScreenEnabled",
        REG_SZ,
        "Off",
        4
    );
    
    return success1 && success2;
}

#ifndef AK_CP_DEFINED
#define AK_CP_DEFINED
bool AK_CP(const json& params) {
    std::cout << "Disabling cloud-based protection..." << std::endl;
    
    DWORD value = 0;
    bool success1 = MY(
        "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet",
        "SpynetReporting",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0;
    bool success2 = MY(
        "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet",
        "SubmitSamplesConsent",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}
#endif

bool AK_AS(const json& params) {
    std::cout << "Disabling automatic sample submission..." << std::endl;
    
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows Defender\\Spynet",
        "SubmitSamplesConsent",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_UC(const json& params) {
    std::cout << "Disabling UAC..." << std::endl;
    
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
        "EnableLUA",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_WI(const json& params) {
    std::cout << "Disabling Windows Installer..." << std::endl;
    
    
    DWORD value = 3; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\msiserver",
        "Start",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_WU(const json& params) {
    std::cout << "Disabling Windows Updates..." << std::endl;
    
    
    DWORD value = 1; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU",
        "NoAutoUpdate",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    
    value = 0; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU",
        "AUOptions",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_PU(const json& params) {
    std::cout << "Disabling P2P updates..." << std::endl;
    
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\DeliveryOptimization\\Config",
        "DODownloadMode",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_DU(const json& params) {
    std::cout << "Disabling driver updates..." << std::endl;
    
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate",
        "ExcludeWUDriversInQualityUpdate",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_TZ(const json& params) {
    std::cout << "Disabling time zone updates..." << std::endl;
    
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\CurrentVersion\\Time Zone",
        "DisableAutoDaylightTimeSet",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_CT(const json& params) {
    std::cout << "Disabling cloud content..." << std::endl;
    
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\CloudContent",
        "DisableWindowsConsumerFeatures",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_DS(const json& params) {
    std::cout << "Disabling delivery optimization..." << std::endl;
    
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\DoSvc",
        "Start",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_WS(const json& params) {
    std::cout << "Disabling Windows Search..." << std::endl;
    
    
    DWORD value = 4; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\WSearch",
        "Start",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

#ifndef AK_BS_DEFINED
#define AK_BS_DEFINED
bool AK_BS(const json& params) {
    std::cout << "Disabling biometric service..." << std::endl;
    
    bool success = ED("sc config WbioSrvc start= disabled");
    
    if (success) {
        success = ED("sc stop WbioSrvc");
    }
    
    return success;
}
#endif

bool AK_TS(const json& params) {
    std::cout << "Disabling touch screen..." << std::endl;
    
    
    bool success = ED("sc config TabletInputService start= disabled");
    
    return success;
}

bool AK_WD(const json& params) {
    std::cout << "Disabling Windows Defender..." << std::endl;
    
    
    DWORD value = 1; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender",
        "DisableAntiSpyware",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    
    value = 1; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection",
        "DisableRealtimeMonitoring",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}


bool AK_FW(const json& params) {
    std::cout << "Disabling Windows Firewall..." << std::endl;
    
    
    bool success1 = ED("netsh advfirewall set allprofiles state off");
    
    
    DWORD value = 0; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
        "EnableFirewall",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    
    bool success3 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile",
        "EnableFirewall",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    
    bool success4 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile",
        "EnableFirewall",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2 && success3 && success4;
}


bool AK_S1(const json& params) {
    std::cout << "Disabling security 1..." << std::endl;
    
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
        "EnableSecureUIAPaths",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}


bool AK_ES(const json& params) {
    std::cout << "Disabling error reporting..." << std::endl;
    
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting",
        "Disabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}


bool AK_DP(const json& params) {
    std::cout << "Disabling data collection..." << std::endl;
    
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection",
        "AllowTelemetry",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}


bool AK_DH(const json& params) {
    std::cout << "Disabling hibernation..." << std::endl;
    
    
    bool success = ED("powercfg -h off");
    
    return success;
}


bool AK_DM(const json& params) {
    std::cout << "Disabling memory dumps..." << std::endl;
    
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\CrashControl",
        "CrashDumpEnabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}


bool AK_DT(const json& params) {
    std::cout << "Disabling task scheduler..." << std::endl;
    
    
    bool success = ED("sc config Schedule start= disabled");
    
    return success;
}


bool AK_DW(const json& params) {
    std::cout << "Disabling Windows Media Player..." << std::endl;
    
    
    bool success = ED("sc config WMPNetworkSvc start= disabled");
    
    return success;
} 