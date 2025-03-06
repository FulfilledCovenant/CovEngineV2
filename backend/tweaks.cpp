#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <Windows.h>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

bool AK_BD(const json& params);
bool AK_BS(const json& params);
bool AK_MN(const json& params);
bool AK_RH(const json& params);
bool AK_PE(const json& params);
bool AK_MA(const json& params);
bool AK_GR(const json& params);
bool AK_TY(const json& params);

bool AK(const std::string& tweak_id, const json& params) {
    std::cout << "Applying tweak: " << tweak_id << std::endl;
    
    if (tweak_id == "configure_bcdedit") {
        return AK_BD(params);
    } else if (tweak_id == "disable_background_apps") {
        return AK_BS(params);
    } else if (tweak_id == "disable_memory_compression") {
        return AK_MN(params);
    } else if (tweak_id == "set_ram_usage_high") {
        return AK_RH(params);
    } else if (tweak_id == "disable_pagefile") {
        return AK_PE(params);
    } else if (tweak_id == "disable_mouse_acceleration") {
        return AK_MA(params);
    } else if (tweak_id == "disable_game_bar") {
        return AK_GR(params);
    } else if (tweak_id == "disable_telemetry") {
        return AK_TY(params);
    } else {
        std::cerr << "Unknown tweak ID: " << tweak_id << std::endl;
        return false;
    }
}

bool MY(const std::string& key_path, const std::string& value_name, DWORD value_type, const void* data, DWORD data_size) {
    std::string root_key_str = key_path.substr(0, key_path.find('\\'));
    std::string subkey = key_path.substr(key_path.find('\\') + 1);
    
    HKEY root_key = NULL;
    if (root_key_str == "HKEY_CURRENT_USER" || root_key_str == "HKCU") {
        root_key = HKEY_CURRENT_USER;
    } else if (root_key_str == "HKEY_LOCAL_MACHINE" || root_key_str == "HKLM") {
        root_key = HKEY_LOCAL_MACHINE;
    } else if (root_key_str == "HKEY_CLASSES_ROOT" || root_key_str == "HKCR") {
        root_key = HKEY_CLASSES_ROOT;
    } else if (root_key_str == "HKEY_USERS" || root_key_str == "HKU") {
        root_key = HKEY_USERS;
    } else {
        std::cerr << "Invalid root key: " << root_key_str << std::endl;
        return false;
    }
    
    HKEY hKey;
    LONG result = RegCreateKeyExA(
        root_key,
        subkey.c_str(),
        0,
        NULL,
        REG_OPTION_NON_VOLATILE,
        KEY_WRITE,
        NULL,
        &hKey,
        NULL
    );
    
    if (result != ERROR_SUCCESS) {
        std::cerr << "Failed to open registry key: " << key_path << " (Error: " << result << ")" << std::endl;
        return false;
    }
    
    result = RegSetValueExA(
        hKey,
        value_name.c_str(),
        0,
        value_type,
        static_cast<const BYTE*>(data),
        data_size
    );
    
    RegCloseKey(hKey);
    
    if (result != ERROR_SUCCESS) {
        std::cerr << "Failed to set registry value: " << value_name << " (Error: " << result << ")" << std::endl;
        return false;
    }
    
    return true;
}

bool ED(const std::string& command) {
    std::cout << "Executing command: " << command << std::endl;
    
    int result = system(command.c_str());
    
    if (result != 0) {
        std::cerr << "Command execution failed with code: " << result << std::endl;
        return false;
    }
    
    return true;
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
    DWORD value = 3; // 3 for Programs
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

json PS(const json& tweaks) {
    json results;
    results["successful"] = json::array();
    results["failed"] = json::array();
    
    for (const auto& tweak : tweaks) {
        std::string tweak_id = tweak["id"];
        json params = tweak.contains("params") ? tweak["params"] : json({});
        
        bool success = AK(tweak_id, params);
        
        if (success) {
            results["successful"].push_back(tweak_id);
        } else {
            results["failed"].push_back({{"id", tweak_id}, {"reason", "Failed to apply tweak"}});
        }
    }
    
    return results;
} 