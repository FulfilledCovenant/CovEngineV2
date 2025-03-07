#include <iostream>
#include <string>
#include <Windows.h>
#include "nlohmann/json.hpp"
#include "tweaks.h"

using json = nlohmann::json;

bool AK_MM(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", 
              "LargeSystemCache", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_AF(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\FileSystem", 
              "NtfsDisableLastAccessUpdate", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_BT(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 
              "DelayedDesktopSwitchTimeout", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_FT(const json& params) {
    const char* value = "0";
    bool s = MY("HKCU\\Control Panel\\Desktop", 
              "MenuShowDelay", REG_SZ, value, 2);
    return s;
}

bool AK_PS(const json& params) {
    bool s = ED("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c");
    return s;
}

bool AK_PF(const json& params) {
    DWORD value = 38;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl", 
              "Win32PrioritySeparation", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_HS(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", 
              "DisablePagingExecutive", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_SM(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", 
              "SystemPages", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_VE(const json& params) {
    DWORD value = 2;
    bool s = MY("HKCU\\Control Panel\\Desktop", 
              "VisualFXSetting", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_ST(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "Start_ShowRun", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_AR(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer", 
              "AltTabSettings", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_NS(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "NavPaneShowAllFolders", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_SB(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search", 
              "SearchboxTaskbarMode", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_LP(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "LaunchTo", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_UP(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", 
              "SystemResponsiveness", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_PT(const json& params) {
    DWORD value = 0xffffffff;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", 
              "NetworkThrottlingIndex", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_GD(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR", 
              "AppCaptureEnabled", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_GM(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Software\\Microsoft\\GameBar", 
              "AutoGameModeEnabled", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_FS(const json& params) {
    DWORD value = 2;
    bool s = MY("HKCU\\System\\GameConfigStore", 
              "GameDVR_FSEBehavior", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_LT(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_AL(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_FB(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Siuf\\Rules", 
              "NumberOfSIUFInPeriod", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_DD(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection", 
              "AllowTelemetry", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_TE(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Privacy", 
              "TailoredExperiencesWithDiagnosticDataEnabled", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_AH(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System", 
              "EnableActivityFeed", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_AD(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo", 
              "Enabled", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_AI(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\userAccountInformation", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_AC(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\contacts", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_CA(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\appointments", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_CM(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\phoneCallHistory", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_EM(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\email", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_MS(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\chat", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_PH(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\phoneCall", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_OA(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\bluetoothSync", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_BG(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications", 
              "GlobalUserDisabled", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_DG(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\appDiagnostics", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_PC(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\picturesLibrary", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_VD(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\videosLibrary", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_RS(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa", 
              "RestrictAnonymous", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_SF(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System", 
              "EnableSmartScreen", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_AS(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet", 
              "SubmitSamplesConsent", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_UC(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 
              "EnableLUA", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_WI(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\TabletPC", 
              "EnableWindowsInkWorkspace", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_WU(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU", 
              "NoAutoUpdate", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_PU(const json& params) {
    DWORD value = 0xFFFFFFFF;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings", 
              "PauseUpdatesExpiryTime", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_DU(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate", 
              "ExcludeWUDriversInQualityUpdate", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_TZ(const json& params) {
    bool s = ED("sc config tzautoupdate start= disabled");
    return s;
}

bool AK_CT(const json& params) {
    bool s = ED("sc config DiagTrack start= disabled");
    return s;
}

bool AK_DS(const json& params) {
    bool s = ED("sc config DsSvc start= disabled");
    return s;
}

bool AK_WS(const json& params) {
    bool s = ED("sc config WSearch start= disabled");
    return s;
}

bool AK_TS(const json& params) {
    bool s = ED("sc config dmwappushservice start= disabled");
    return s;
}

bool AK_WD(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender", 
              "DisableAntiSpyware", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_FW(const json& params) {
    bool s = ED("netsh advfirewall set allprofiles state off");
    return s;
}

bool AK_S1(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters", 
              "SMB1", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_ES(const json& params) {
    DWORD value = 2;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System", 
              "EnableSmartScreen", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_DP(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "ShowPreviewHandlers", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_DH(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "Start_TrackProgs", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_DM(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "ShowInfoTip", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_DW(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search", 
              "BingSearchEnabled", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_AO(const json& params) {
    DWORD value = 8;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games", 
              "GPU Priority", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_CP(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\0cc5b647-c1df-4637-891a-dec35c318583", 
              "ValueMax", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_SS(const json& params) {
    DWORD value = 2;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\SettingSync", 
              "DisableSettingSync", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_RA(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\radios", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_DT(const json& params) {
    const char* value = "Deny";
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\documentsLibrary", 
              "Value", REG_SZ, value, 5);
    return s;
}

bool AK_BD(const json& params) {
    bool registry_success = true;
    
    std::string cmd = "bcdedit /set useplatformclock false";
    bool cmd_success = ED(cmd);
    
    cmd = "bcdedit /set disabledynamictick yes";
    cmd_success = cmd_success && ED(cmd);
    
    return registry_success || cmd_success;
}

bool AK_BS(const json& params) {
    DWORD value = 1; 
    bool registry_success = MY(
        "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications",
        "GlobalUserDisabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    std::string cmd = "powershell -Command \"Get-AppxPackage | ForEach {Add-AppxPackage -DisableDevelopmentMode -Register '$($_.InstallLocation)\\AppxManifest.xml'}\"";
    bool cmd_success = ED(cmd);
    
    return registry_success || cmd_success;
}

bool AK_MN(const json& params) {
    bool registry_success = false;
    
    std::string cmd = "powershell -Command \"Disable-MMAgent -MemoryCompression\"";
    bool cmd_success = ED(cmd);
    
    return registry_success || cmd_success;
}

bool AK_RH(const json& params) {
    DWORD value = 3; 
    bool registry_success = MY(
        "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl",
        "Win32PrioritySeparation",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool cmd_success = false;
    
    return registry_success || cmd_success;
}

bool AK_PE(const json& params) {
    DWORD value = 0; 
    bool registry_success = MY(
        "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
        "PagingFiles",
        REG_MULTI_SZ,
        "",
        1
    );
    
    std::string cmd = "wmic computersystem set AutomaticManagedPagefile=False";
    bool cmd_success = ED(cmd);
    
    cmd = "wmic pagefileset delete";
    cmd_success = cmd_success && ED(cmd);
    
    return registry_success || cmd_success;
}

bool AK_MA(const json& params) {
    DWORD value = 0; 
    bool registry_success = MY(
        "HKCU\\Control Panel\\Mouse",
        "MouseSpeed",
        REG_SZ,
        "0",
        2
    );
    
    registry_success = registry_success && MY(
        "HKCU\\Control Panel\\Mouse",
        "MouseThreshold1",
        REG_SZ,
        "0",
        2
    );
    
    registry_success = registry_success && MY(
        "HKCU\\Control Panel\\Mouse",
        "MouseThreshold2",
        REG_SZ,
        "0",
        2
    );
    
    bool cmd_success = false;
    
    return registry_success || cmd_success;
}

bool AK_GR(const json& params) {
    DWORD value = 0; 
    bool registry_success = MY(
        "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
        "AppCaptureEnabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    registry_success = registry_success && MY(
        "HKCU\\System\\GameConfigStore",
        "GameDVR_Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    std::string cmd = "powershell -Command \"New-ItemProperty -Path 'HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR' -Name AppCaptureEnabled -PropertyType DWORD -Value 0 -Force\"";
    bool cmd_success = ED(cmd);
    
    return registry_success || cmd_success;
}

bool AK_TY(const json& params) {
    DWORD value = 0; 
    bool registry_success = MY(
        "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection",
        "AllowTelemetry",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    std::string cmd = "sc config DiagTrack start= disabled";
    bool cmd_success = ED(cmd);
    
    cmd = "sc config dmwappushservice start= disabled";
    cmd_success = cmd_success && ED(cmd);
    
    return registry_success || cmd_success;
} 