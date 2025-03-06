#include <iostream>
#include <string>
#include <Windows.h>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

extern bool MY(const std::string& key_path, const std::string& value_name, DWORD value_type, const void* data, DWORD data_size);
extern bool ED(const std::string& command);


bool AK_RA(const json& params) {
    std::cout << "Restricting anonymous access..." << std::endl;
    
    DWORD value = 1; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa",
        "RestrictAnonymous",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa",
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
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\MicrosoftEdge\\PhishingFilter",
        "EnabledV9",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_CP(const json& params) {
    std::cout << "Disabling cloud-based protection..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet",
        "SpynetReporting",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_AS(const json& params) {
    std::cout << "Disabling automatic sample submission..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet",
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
    std::cout << "Disabling Windows Ink Workspace..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\WindowsInkWorkspace",
        "AllowWindowsInkWorkspace",
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
    
    bool success2 = ED("sc config wuauserv start= disabled");
    
    return success1 && success2;
}

bool AK_PU(const json& params) {
    std::cout << "Pausing Windows Updates..." << std::endl;
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings",
        "PausedFeatureStatus",
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
    std::cout << "Disabling Auto Time Zone Updater Service..." << std::endl;
    
    bool success = ED("sc config tzautoupdate start= disabled");
    
    return success;
}

bool AK_CT(const json& params) {
    std::cout << "Disabling Connected User Experiences and Telemetry Service..." << std::endl;
    
    bool success = ED("sc config DiagTrack start= disabled");
    
    return success;
}

bool AK_DS(const json& params) {
    std::cout << "Disabling Data Sharing Service..." << std::endl;
    
    bool success = ED("sc config dmwappushservice start= disabled");
    
    return success;
}

bool AK_WS(const json& params) {
    std::cout << "Disabling Windows Search Service..." << std::endl;
    
    bool success = ED("sc config WSearch start= disabled");
    
    return success;
}

bool AK_BS(const json& params) {
    std::cout << "Disabling Windows Biometric Service..." << std::endl;
    
    bool success = ED("sc config WbioSrvc start= disabled");
    
    return success;
}

bool AK_TS(const json& params) {
    std::cout << "Disabling tracking services..." << std::endl;
    
    bool success1 = ED("sc config diagtrack start= disabled");
    bool success2 = ED("sc config dmwappushservice start= disabled");
    bool success3 = ED("sc config RetailDemo start= disabled");
    
    return success1 && success2 && success3;
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
    std::cout << "Disabling SMB1..." << std::endl;
    
    bool success = ED("dism /online /Disable-Feature /FeatureName:SMB1Protocol /NoRestart");
    
    return success;
}

bool AK_ES(const json& params) {
    std::cout << "Enhancing SmartScreen..." << std::endl;
    
    DWORD value = 1; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
        "EnableSmartScreen",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 1; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
        "ShellSmartScreenLevel",
        REG_SZ,
        "Block",
        6
    );
    
    return success1 && success2;
}

bool AK_DP(const json& params) {
    std::cout << "Disabling file preview..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
        "ShowPreviewHandlers",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_DH(const json& params) {
    std::cout << "Disabling handle history..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Kernel",
        "ObCaseInsensitive",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_DM(const json& params) {
    std::cout << "Disabling metadata retrieval..." << std::endl;
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer",
        "DisableMetaDataRetrieval",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_DT(const json& params) {
    std::cout << "Disabling thumbnails..." << std::endl;
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
        "IconsOnly",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_DW(const json& params) {
    std::cout << "Disabling web search..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Search",
        "BingSearchEnabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Search",
        "CortanaConsent",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
} 