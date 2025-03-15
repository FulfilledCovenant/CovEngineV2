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
    DWORD value = 4;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\SysMain", 
              "Start", REG_DWORD, &value, sizeof(value));
    
    s &= ED("sc stop SysMain");
    s &= ED("sc config SysMain start= disabled");
    
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

bool AK_DC(const json& params) {
    bool s = ED("cleanmgr /sageset:1");
    s &= ED("schtasks /create /tn \"Disk Cleanup\" /tr \"cleanmgr /sagerun:1\" /sc weekly /d SUN /st 00:00 /ru SYSTEM /f");
    
    DWORD value = 1;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Active Setup Temp Folders", 
              "StateFlags0001", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 1;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Downloaded Program Files", 
              "StateFlags0001", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 1;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Internet Cache Files", 
              "StateFlags0001", REG_DWORD, &value3, sizeof(value3));
    
    DWORD value4 = 1;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Temporary Files", 
              "StateFlags0001", REG_DWORD, &value4, sizeof(value4));
    
    return s;
}

bool AK_EP(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Control Panel\\Mouse", 
              "MouseSpeed", REG_SZ, "1", 2);
    
    s &= MY("HKCU\\Control Panel\\Mouse", 
              "MouseThreshold1", REG_SZ, "6", 2);
    
    s &= MY("HKCU\\Control Panel\\Mouse", 
              "MouseThreshold2", REG_SZ, "10", 2);
    
    return s;
}

bool AK_OG(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games", 
              "Affinity", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 2;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games", 
              "Background Only", REG_SZ, "False", 6);
    
    DWORD value3 = 1;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games", 
              "Clock Rate", REG_DWORD, &value3, sizeof(value3));
    
    DWORD value4 = 8;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games", 
              "GPU Priority", REG_DWORD, &value4, sizeof(value4));
    
    DWORD value5 = 6;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games", 
              "Priority", REG_DWORD, &value5, sizeof(value5));
    
    DWORD value6 = 1;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games", 
              "Scheduling Category", REG_SZ, "High", 5);
    
    DWORD value7 = 2;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", 
              "SystemResponsiveness", REG_DWORD, &value7, sizeof(value7));
    
    return s;
}

bool AK_OD(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\DirectX", 
              "ForceDirectDrawEmulation", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\DirectX", 
              "DisableMaximizedWindowedModeShim", REG_DWORD, &value2, sizeof(value2));
    
    return s;
}

bool AK_OV(const json& params) {
    DWORD value = 2;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects", 
              "VisualFXSetting", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKCU\\Control Panel\\Desktop", 
              "UserPreferencesMask", REG_BINARY, "\x90\x12\x01\x80", 4);
    
    DWORD value3 = 0;
    s &= MY("HKCU\\Control Panel\\Desktop\\WindowMetrics", 
              "MinAnimate", REG_SZ, "0", 2);
    
    DWORD value4 = 0;
    s &= MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "ListviewShadow", REG_DWORD, &value4, sizeof(value4));
    
    DWORD value5 = 0;
    s &= MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced", 
              "TaskbarAnimations", REG_DWORD, &value5, sizeof(value5));
    
    return s;
}

bool AK_OT(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "GlobalMaxTcpWindowSize", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "TcpTimedWaitDelay", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 1;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "DisableTaskOffload", REG_DWORD, &value3, sizeof(value3));
    
    DWORD value4 = 1;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "EnablePMTUDiscovery", REG_DWORD, &value4, sizeof(value4));
    
    DWORD value5 = 1;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "EnablePMTUBHDetect", REG_DWORD, &value5, sizeof(value5));
    
    return s;
}

bool AK_OU(const json& params) {
    DWORD value = 0xFFFFFFFF;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "MaxUserPort", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "SackOpts", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 1;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "DefaultTTL", REG_DWORD, &value3, sizeof(value3));
    
    return s;
}

bool AK_RL(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", 
              "NetworkThrottlingIndex", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 1;
    s &= MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched", 
              "NonBestEffortLimit", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 0;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", 
              "Tcp1323Opts", REG_DWORD, &value3, sizeof(value3));
    
    return s;
}

bool AK_PG(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\QoS", 
              "Enabled", REG_DWORD, &value, sizeof(value));
    
    const char* value2 = "1";
    s &= MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\QoS", 
              "ApplicationDSCPMarkingEnabled", REG_SZ, value2, 2);
    
    return s;
}

bool AK_OS(const json& params) {
    bool s = ED("netsh interface ip set dns \"Ethernet\" static 1.1.1.1 primary");
    
    s &= ED("netsh interface ip add dns \"Ethernet\" 1.0.0.1 index=2");
    
    return s;
}

bool AK_HP(const json& params) {
    bool s = ED("bcdedit /deletevalue useplatformclock");
    s &= ED("bcdedit /set disabledynamictick yes");
    
    DWORD value = 0;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\TimeBrokerSvc", 
              "Start", REG_DWORD, &value, sizeof(value));
    
    return s;
}

bool AK_DO(const json& params) {
    bool force = false;
    
    if (params.contains("force") && params["force"].is_boolean()) {
        force = params["force"];
    }
    
    if (!force) {
        char onedrive_path[MAX_PATH];
        DWORD size = sizeof(onedrive_path);
        HKEY hKey;
        
        if (RegOpenKeyExA(HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\OneDrive", 0, KEY_READ, &hKey) == ERROR_SUCCESS) {
            if (RegQueryValueExA(hKey, "UserFolder", NULL, NULL, (LPBYTE)onedrive_path, &size) == ERROR_SUCCESS) {
                RegCloseKey(hKey);
                
                WIN32_FIND_DATAA findData;
                std::string search_path = std::string(onedrive_path) + "\\*";
                HANDLE hFind = FindFirstFileA(search_path.c_str(), &findData);
                
                if (hFind != INVALID_HANDLE_VALUE) {
                    int file_count = 0;
                    do {
                        if (strcmp(findData.cFileName, ".") != 0 && strcmp(findData.cFileName, "..") != 0) {
                            file_count++;
                            if (file_count > 5) {
                                FindClose(hFind);
                                std::cerr << "OneDrive folder contains files. Use force parameter to proceed anyway." << std::endl;
                                return false;
                            }
                        }
                    } while (FindNextFileA(hFind, &findData));
                    
                    FindClose(hFind);
                }
            } else {
                RegCloseKey(hKey);
            }
        }
    }
    
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\OneDrive", 
              "DisableFileSyncNGSC", REG_DWORD, &value, sizeof(value));
    
    s &= ED("taskkill /f /im OneDrive.exe");
    s &= ED("C:\\Windows\\SysWOW64\\OneDriveSetup.exe /uninstall");
    s &= ED("C:\\Windows\\System32\\OneDriveSetup.exe /uninstall");
    
    return s;
}

bool AK_HB(const json& params) {
    bool s = ED("powercfg -h off");
    
    DWORD value = 0;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power", 
              "HibernateEnabled", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power", 
              "HibernateEnabledDefault", REG_DWORD, &value2, sizeof(value2));
    
    return s;
}

bool AK_TR(const json& params) {
    bool s = ED("bcdedit /set useplatformtick yes");
    s &= ED("bcdedit /set disabledynamictick yes");
    
    DWORD value = 1;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", 
              "SystemResponsiveness", REG_DWORD, &value, sizeof(value));
    
    s &= ED("powershell -Command \"New-ItemProperty -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile' -Name 'SystemResponsiveness' -PropertyType DWORD -Value 0 -Force\"");
    
    return s;
}

bool AK_NT(const json& params) {
    DWORD value = 4;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\NvTelemetryContainer", 
              "Start", REG_DWORD, &value, sizeof(value));
    
    s &= ED("sc stop NvTelemetryContainer");
    s &= ED("sc config NvTelemetryContainer start= disabled");
    
    DWORD value2 = 0;
    s &= MY("HKLM\\SOFTWARE\\NVIDIA Corporation\\NvControlPanel2\\Client", 
              "OptInOrOutPreference", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 0;
    s &= MY("HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS", 
              "EnableRID", REG_DWORD, &value3, sizeof(value3));
    
    DWORD value4 = 0;
    s &= MY("HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS", 
              "EnableAppTelemetry", REG_DWORD, &value4, sizeof(value4));
    
    return s;
}

bool AK_AT(const json& params) {
    DWORD value = 4;
    bool s = MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\AMD Crash Defender Service", 
              "Start", REG_DWORD, &value, sizeof(value));
    
    s &= ED("sc stop \"AMD Crash Defender Service\"");
    s &= ED("sc config \"AMD Crash Defender Service\" start= disabled");
    
    DWORD value2 = 4;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Services\\AMD Log Utility", 
              "Start", REG_DWORD, &value2, sizeof(value2));
    
    s &= ED("sc stop \"AMD Log Utility\"");
    s &= ED("sc config \"AMD Log Utility\" start= disabled");
    
    return s;
}

bool AK_SD(const json& params) {
    DWORD value = 0;
    bool s = MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Serialize", 
              "StartupDelayInMSec", REG_DWORD, &value, sizeof(value));
    return s;
}

bool AK_OP(const json& params) {
    bool s = ED("powercfg -setacvalueindex scheme_current sub_processor PERFINCPOL 2");
    s &= ED("powercfg -setacvalueindex scheme_current sub_processor PERFDECPOL 1");
    s &= ED("powercfg -setacvalueindex scheme_current sub_processor PERFINCTHRESHOLD 10");
    s &= ED("powercfg -setacvalueindex scheme_current sub_processor PERFDECTHRESHOLD 8");
    
    DWORD value = 100;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\be337238-0d82-4146-a960-4f3749d470c7", 
              "ACSettingIndex", REG_DWORD, &value, sizeof(value));
    
    return s;
}

bool AK_DA(const json& params) {
    DWORD value = 1;
    bool s = MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU", 
              "NoAutoUpdate", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU", 
              "AUOptions", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 0;
    s &= MY("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\DeliveryOptimization\\Config", 
              "DODownloadMode", REG_DWORD, &value3, sizeof(value3));
    
    return s;
}

bool AK_OI(const json& params) {
    bool s = ED("sc config WSearch start= disabled");
    s &= ED("sc stop WSearch");
    
    DWORD value = 0;
    s &= MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search", 
              "AllowCortana", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search", 
              "AllowSearchToUseLocation", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 0;
    s &= MY("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search", 
              "DisableWebSearch", REG_DWORD, &value3, sizeof(value3));
    
    return s;
}

bool AK_DE(const json& params) {
    DWORD value = 0;
    bool s = MY("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", 
              "EnableTransparency", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 0;
    s &= MY("HKCU\\Software\\Microsoft\\Windows\\DWM", 
              "ColorPrevalence", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 0;
    s &= MY("HKCU\\Software\\Microsoft\\Windows\\DWM", 
              "EnableAeroPeek", REG_DWORD, &value3, sizeof(value3));
    
    return s;
}

bool AK_VM(const json& params) {
    bool s = ED("wmic computersystem set AutomaticManagedPagefile=False");
    
    DWORD initialSize = 8192;  // 8 GB initial size
    DWORD maximumSize = 16384; // 16 GB maximum size
    
    std::string cmd = "wmic pagefileset where name=\"C:\\\\pagefile.sys\" set InitialSize=" + std::to_string(initialSize) + ",MaximumSize=" + std::to_string(maximumSize);
    s &= ED(cmd);
    
    DWORD value = 3;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", 
              "LargeSystemCache", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 1;
    s &= MY("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", 
              "IoPageLockLimit", REG_DWORD, &value2, sizeof(value2));
    
    return s;
}

bool AK_OC(const json& params) {
    DWORD value = 1;
    bool s = MY("HKCU\\Control Panel\\Accessibility\\Keyboard Response", 
              "AutoRepeatDelay", REG_DWORD, &value, sizeof(value));
    
    DWORD value2 = 1;
    s &= MY("HKCU\\Control Panel\\Accessibility\\Keyboard Response", 
              "AutoRepeatRate", REG_DWORD, &value2, sizeof(value2));
    
    DWORD value3 = 0;
    s &= MY("HKCU\\Control Panel\\Accessibility\\StickyKeys", 
              "Flags", REG_DWORD, &value3, sizeof(value3));
    
    return s;
} 