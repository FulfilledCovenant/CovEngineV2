#include <iostream>
#include <string>
#include <Windows.h>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

extern bool MY(const std::string& key_path, const std::string& value_name, DWORD value_type, const void* data, DWORD data_size);
extern bool ED(const std::string& command);


bool AK_LT(const json& params) {
    std::cout << "Disabling location tracking..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\lfsvc\\Service",
        "Start",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_TY(const json& params) {
    std::cout << "Disabling telemetry..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection",
        "AllowTelemetry",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\SQMClient\\Windows",
        "CEIPEnable",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; 
    bool success3 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat",
        "AITEnable",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2 && success3;
}

bool AK_AL(const json& params) {
    std::cout << "Disabling app access to location..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_FB(const json& params) {
    std::cout << "Disabling feedback..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Siuf\\Rules",
        "NumberOfSIUFInPeriod",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Siuf\\Rules",
        "PeriodInNanoSeconds",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_DD(const json& params) {
    std::cout << "Disabling diagnostic data..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Diagnostics\\DiagTrack",
        "ShowedToastAtLevel",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = ED("sc config DiagTrack start= disabled");
    
    bool success3 = ED("sc config dmwappushservice start= disabled");
    
    return success1 && success2 && success3;
}

bool AK_TE(const json& params) {
    std::cout << "Disabling tailored experiences..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Privacy",
        "TailoredExperiencesWithDiagnosticDataEnabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_AH(const json& params) {
    std::cout << "Disabling activity history..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
        "EnableActivityFeed",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
        "UploadUserActivities",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success3 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
        "PublishUserActivities",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2 && success3;
}

bool AK_SS(const json& params) {
    std::cout << "Disabling settings sync..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\SettingSync",
        "SyncPolicy",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\SettingSync\\Groups\\Personalization",
        "Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success3 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\SettingSync\\Groups\\BrowserSettings",
        "Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success4 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\SettingSync\\Groups\\Credentials",
        "Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success5 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\SettingSync\\Groups\\Language",
        "Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success6 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\SettingSync\\Groups\\Windows",
        "Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2 && success3 && success4 && success5 && success6;
}

bool AK_AD(const json& params) {
    std::cout << "Disabling advertising ID..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo",
        "Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\AdvertisingInfo",
        "DisabledByGroupPolicy",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_AI(const json& params) {
    std::cout << "Disabling app access to account info..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\userAccountInformation",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_AC(const json& params) {
    std::cout << "Disabling app access to contacts..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\contacts",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_CA(const json& params) {
    std::cout << "Disabling app access to calendar..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\appointments",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_CM(const json& params) {
    std::cout << "Disabling app access to call history..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\phoneCallHistory",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_EM(const json& params) {
    std::cout << "Disabling app access to email..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\email",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_MS(const json& params) {
    std::cout << "Disabling app access to messages..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\chat",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_PH(const json& params) {
    std::cout << "Disabling app access to phone..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\phoneCall",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_RA(const json& params) {
    std::cout << "Disabling app access to radios..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\radios",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_OA(const json& params) {
    std::cout << "Disabling app access to other devices..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\bluetoothSync",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_BG(const json& params) {
    std::cout << "Disabling background apps access..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications",
        "GlobalUserDisabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_DG(const json& params) {
    std::cout << "Disabling app diagnostics access..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\appDiagnostics",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_DT(const json& params) {
    std::cout << "Disabling app access to documents..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\documentsLibrary",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_PC(const json& params) {
    std::cout << "Disabling app access to pictures..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\picturesLibrary",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
}

bool AK_VD(const json& params) {
    std::cout << "Disabling app access to videos..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\videosLibrary",
        "Value",
        REG_SZ,
        "Deny",
        5
    );
    
    return success;
} 