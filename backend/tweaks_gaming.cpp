#include <iostream>
#include <string>
#include <Windows.h>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

extern bool MY(const std::string& key_path, const std::string& value_name, DWORD value_type, const void* data, DWORD data_size);
extern bool ED(const std::string& command);


bool AK_MA(const json& params) {
    std::cout << "Disabling mouse acceleration..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Control Panel\\Mouse",
        "MouseSpeed",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; 
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Control Panel\\Mouse",
        "MouseThreshold1",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; 
    bool success3 = MY(
        "HKEY_CURRENT_USER\\Control Panel\\Mouse",
        "MouseThreshold2",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success && success2 && success3;
}

bool AK_VE(const json& params) {
    std::cout << "Optimizing visual effects..." << std::endl;
    
    DWORD value = 2; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects",
        "VisualFXSetting",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; 
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Control Panel\\Desktop\\WindowMetrics",
        "MinAnimate",
        REG_SZ,
        "0",
        2
    );
    
    value = 0; 
    bool success3 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
        "EnableTransparency",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2 && success3;
}

bool AK_ST(const json& params) {
    std::cout << "Reducing shutdown time..." << std::endl;
    
    DWORD value = 1; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control",
        "WaitToKillServiceTimeout",
        REG_SZ,
        "1000",
        5
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Control Panel\\Desktop",
        "HungAppTimeout",
        REG_SZ,
        "1000",
        5
    );
    
    bool success3 = MY(
        "HKEY_CURRENT_USER\\Control Panel\\Desktop",
        "WaitToKillAppTimeout",
        REG_SZ,
        "2000",
        5
    );
    
    return success1 && success2 && success3;
}

bool AK_AR(const json& params) {
    std::cout << "Disabling autorun/autoplay..." << std::endl;
    
    DWORD value = 0xFF; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
        "NoDriveTypeAutoRun",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; 
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers",
        "DisableAutoplay",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_NS(const json& params) {
    std::cout << "Configuring network settings..." << std::endl;
    
    bool success1 = ED("netsh int tcp set global autotuninglevel=disabled");
    
    bool success2 = ED("netsh int tcp set global chimney=disabled");
    
    bool success3 = ED("netsh int tcp set global rss=disabled");
    
    bool success4 = ED("netsh int tcp set global netdma=disabled");
    
    bool success5 = ED("netsh int tcp set global ecncapability=disabled");
    
    return success1 && success2 && success3 && success4 && success5;
}

bool AK_SB(const json& params) {
    std::cout << "Disabling SMB bandwidth throttling..." << std::endl;
    
    DWORD value = 0xFFFFFFFF; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters",
        "SizReqBuf",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_LP(const json& params) {
    std::cout << "Disabling LLMNR protocol..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\DNSClient",
        "EnableMulticast",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_MN(const json& params) {
    std::cout << "Applying miscellaneous network settings..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched",
        "NonBestEffortLimit",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 1; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
        "TCPNoDelay",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 1; 
    bool success3 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
        "TcpAckFrequency",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2 && success3;
}

bool AK_UP(const json& params) {
    std::cout << "Setting ultimate performance power plan..." << std::endl;
    
    bool success1 = ED("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61");
    
    bool success2 = ED("powercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61");
    
    return success1 && success2;
}

bool AK_PT(const json& params) {
    std::cout << "Disabling power throttling..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling",
        "PowerThrottlingOff",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_AO(const json& params) {
    std::cout << "Unlocking all advanced power options..." << std::endl;
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings",
        "Attributes",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_CP(const json& params) {
    std::cout << "Disabling core parking..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\0cc5b647-c1df-4637-891a-dec35c318583",
        "ValueMax",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_GR(const json& params) {
    std::cout << "Disabling Game Bar..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
        "AppCaptureEnabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
        "GameDVR_Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success3 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar",
        "ShowStartupPanel",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success4 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar",
        "GamePanelStartupTipIndex",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2 && success3 && success4;
}

bool AK_GD(const json& params) {
    std::cout << "Disabling Game DVR..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR",
        "AllowGameDVR",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\System\\GameConfigStore",
        "GameDVR_Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_GM(const json& params) {
    std::cout << "Enabling Game Mode..." << std::endl;
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar",
        "AutoGameModeEnabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_FS(const json& params) {
    std::cout << "Disabling fullscreen optimizations..." << std::endl;
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_CURRENT_USER\\System\\GameConfigStore",
        "GameDVR_FSEBehaviorMode",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\System\\GameConfigStore",
        "GameDVR_HonorUserFSEBehaviorMode",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success3 = MY(
        "HKEY_CURRENT_USER\\System\\GameConfigStore",
        "GameDVR_DXGIHonorFSEWindowsCompatible",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success && success2 && success3;
} 