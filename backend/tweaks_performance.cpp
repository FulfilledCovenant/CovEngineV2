#include <iostream>
#include <string>
#include <Windows.h>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

extern bool MY(const std::string& key_path, const std::string& value_name, DWORD value_type, const void* data, DWORD data_size);
extern bool ED(const std::string& command);


bool AK_BD(const json& params) {
    std::cout << "Applying BCDEdit tweaks..." << std::endl;
    
    bool success1 = ED("bcdedit /timeout 3");
    
    bool success2 = ED("bcdedit /set disabledynamictick yes");
    
    bool success3 = ED("bcdedit /set useplatformtick yes");
    
    bool success4 = ED("bcdedit /set disabledynamictick yes");
    
    bool success5 = ED("bcdedit /set bootlog no");
    
    bool success6 = ED("bcdedit /set quietboot yes");
    
    return success1 && success2 && success3 && success4 && success5 && success6;
}

bool AK_BS(const json& params) {
    std::cout << "Disabling background apps..." << std::endl;
    
    DWORD value = 1; 
    bool success1 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications",
        "GlobalUserDisabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Search",
        "BackgroundAppGlobalToggle",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_MN(const json& params) {
    std::cout << "Disabling memory compression..." << std::endl;
    
    bool success = ED("powershell -Command \"Disable-MMAgent -MemoryCompression\"");
    
    return success;
}

bool AK_RH(const json& params) {
    std::cout << "Setting RAM usage to high..." << std::endl;
    
    DWORD value = 3; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
        "LargeSystemCache",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 1; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
        "IoPageLockLimit",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_PE(const json& params) {
    std::cout << "Disabling pagefile..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
        "PagingFiles",
        REG_MULTI_SZ,
        "",
        1
    );
    
    value = 0;
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
        "ClearPageFileAtShutdown",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_MM(const json& params) {
    std::cout << "Configuring MMCSS..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile",
        "NetworkThrottlingIndex",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; // 0 = Gaming/Streaming mode
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile",
        "SystemResponsiveness",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_AF(const json& params) {
    std::cout << "Disabling automatic folder discovery..." << std::endl;
    
    DWORD value = 1; 
    bool success = MY(
        "HKEY_CURRENT_USER\\Software\\Classes\\Local Settings\\Software\\Microsoft\\Windows\\Shell",
        "BagMRU Size",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_BT(const json& params) {
    std::cout << "Disabling boot tracing..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters",
        "EnableBootTrace",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    value = 0; 
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\BootControl",
        "AdvancedBootStatusPolicy",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_FT(const json& params) {
    std::cout << "Disabling fault tolerant heap..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\FTH",
        "Enabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_PS(const json& params) {
    std::cout << "Disabling paging settings..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
        "DisablePagingExecutive",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_PF(const json& params) {
    std::cout << "Disabling prefetch..." << std::endl;
    
    DWORD value = 0; 
    bool success1 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters",
        "EnablePrefetcher",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    bool success2 = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters",
        "EnableSuperfetch",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success1 && success2;
}

bool AK_HS(const json& params) {
    std::cout << "Disabling service host splitting..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control",
        "SvcHostSplitThresholdInKB",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_SS(const json& params) {
    std::cout << "Disabling sleep study..." << std::endl;
    
    DWORD value = 0; 
    bool success = MY(
        "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power",
        "SleepStudyEnabled",
        REG_DWORD,
        &value,
        sizeof(value)
    );
    
    return success;
}

bool AK_SM(const json& params) {
    std::cout << "Disabling Spectre and Meltdown mitigations..." << std::endl;
    
    bool success = ED("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v FeatureSettingsOverride /t REG_DWORD /d 3 /f");
    
    bool success2 = ED("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v FeatureSettingsOverrideMask /t REG_DWORD /d 3 /f");
    
    return success && success2;
} 