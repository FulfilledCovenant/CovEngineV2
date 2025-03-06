#include <iostream>
#include <string>
#include <Windows.h>
#include <cstdlib>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

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
        std::cerr << "Command failed with exit code: " << result << std::endl;
        return false;
    }
    
    return true;
}

json PS(const json& tweaks) {
    json results;
    json successful = json::array();
    json failed = json::array();
    
    for (const auto& tweak : tweaks) {
        std::string tweak_id = tweak["id"];
        std::string category = tweak["category"];
        
        std::cout << "Processing tweak: " << tweak_id << " (Category: " << category << ")" << std::endl;
        
        bool success = false;
        
        if (tweak_id == "configure_bcdedit") {
            success = AK_BD(tweak);
        } else if (tweak_id == "disable_background_apps") {
            success = AK_BS(tweak);
        } else if (tweak_id == "disable_memory_compression") {
            success = AK_MN(tweak);
        } else if (tweak_id == "set_ram_usage_high") {
            success = AK_RH(tweak);
        } else if (tweak_id == "disable_pagefile") {
            success = AK_PE(tweak);
        } else if (tweak_id == "configure_mmcss") {
            success = AK_MM(tweak);
        } else if (tweak_id == "disable_automatic_folder_discovery") {
            success = AK_AF(tweak);
        } else if (tweak_id == "disable_boot_tracing") {
            success = AK_BT(tweak);
        } else if (tweak_id == "disable_fault_tolerant_heap") {
            success = AK_FT(tweak);
        } else if (tweak_id == "disable_paging_settings") {
            success = AK_PS(tweak);
        } else if (tweak_id == "disable_prefetch") {
            success = AK_PF(tweak);
        } else if (tweak_id == "disable_service_host_splitting") {
            success = AK_HS(tweak);
        } else if (tweak_id == "disable_sleep_study") {
            success = AK_SS(tweak);
        } else if (tweak_id == "disable_spectre_and_meltdown") {
            success = AK_SM(tweak);
        }
        else if (tweak_id == "disable_mouse_acceleration") {
            success = AK_MA(tweak);
        } else if (tweak_id == "optimize_visual_effects") {
            success = AK_VE(tweak);
        } else if (tweak_id == "reduce_shutdown_time") {
            success = AK_ST(tweak);
        } else if (tweak_id == "disable_autorun_autoplay") {
            success = AK_AR(tweak);
        } else if (tweak_id == "configure_network_settings") {
            success = AK_NS(tweak);
        } else if (tweak_id == "disable_smb_bandwidth_throttling") {
            success = AK_SB(tweak);
        } else if (tweak_id == "disable_llmnr_protocol") {
            success = AK_LP(tweak);
        } else if (tweak_id == "miscellaneous_network_settings") {
            success = AK_MN(tweak);
        } else if (tweak_id == "set_ultimate_performance_power_plan_once") {
            success = AK_UP(tweak);
        } else if (tweak_id == "disable_power_throttling") {
            success = AK_PT(tweak);
        } else if (tweak_id == "unlock_all_advanced_power_options") {
            success = AK_AO(tweak);
        } else if (tweak_id == "disable_core_parking") {
            success = AK_CP(tweak);
        } else if (tweak_id == "disable_game_bar") {
            success = AK_GR(tweak);
        } else if (tweak_id == "disable_game_dvr") {
            success = AK_GD(tweak);
        } else if (tweak_id == "enable_game_mode") {
            success = AK_GM(tweak);
        } else if (tweak_id == "disable_fullscreen_optimizations") {
            success = AK_FS(tweak);
        }
        else if (tweak_id == "disable_location_tracking") {
            success = AK_LT(tweak);
        } else if (tweak_id == "disable_telemetry") {
            success = AK_TY(tweak);
        } else if (tweak_id == "disable_app_access_to_location") {
            success = AK_AL(tweak);
        } else if (tweak_id == "disable_feedback") {
            success = AK_FB(tweak);
        } else if (tweak_id == "disable_diagnostic_data") {
            success = AK_DD(tweak);
        } else if (tweak_id == "disable_tailored_experiences") {
            success = AK_TE(tweak);
        } else if (tweak_id == "disable_activity_history") {
            success = AK_AH(tweak);
        } else if (tweak_id == "disable_settings_sync") {
            success = AK_SS(tweak);
        } else if (tweak_id == "disable_advertising_id") {
            success = AK_AD(tweak);
        } else if (tweak_id == "disable_app_access_to_account_info") {
            success = AK_AI(tweak);
        } else if (tweak_id == "disable_app_access_to_contacts") {
            success = AK_AC(tweak);
        } else if (tweak_id == "disable_app_access_to_calendar") {
            success = AK_CA(tweak);
        } else if (tweak_id == "disable_app_access_to_call_history") {
            success = AK_CM(tweak);
        } else if (tweak_id == "disable_app_access_to_email") {
            success = AK_EM(tweak);
        } else if (tweak_id == "disable_app_access_to_messages") {
            success = AK_MS(tweak);
        } else if (tweak_id == "disable_app_access_to_phone") {
            success = AK_PH(tweak);
        } else if (tweak_id == "disable_app_access_to_radios") {
            success = AK_RA(tweak);
        } else if (tweak_id == "disable_app_access_to_other_devices") {
            success = AK_OA(tweak);
        } else if (tweak_id == "disable_background_apps_access") {
            success = AK_BG(tweak);
        } else if (tweak_id == "disable_app_diagnostics_access") {
            success = AK_DG(tweak);
        } else if (tweak_id == "disable_app_access_to_documents") {
            success = AK_DT(tweak);
        } else if (tweak_id == "disable_app_access_to_pictures") {
            success = AK_PC(tweak);
        } else if (tweak_id == "disable_app_access_to_videos") {
            success = AK_VD(tweak);
        }
        else if (tweak_id == "restrict_anonymous_access") {
            success = AK_RA(tweak);
        } else if (tweak_id == "restrict_anonymous_enumeration_of_shares") {
            success = AK_RS(tweak);
        } else if (tweak_id == "disable_smartscreen_filter") {
            success = AK_SF(tweak);
        } else if (tweak_id == "disable_cloud_based_protection") {
            success = AK_CP(tweak);
        } else if (tweak_id == "disable_automatic_sample_submission") {
            success = AK_AS(tweak);
        } else if (tweak_id == "disable_uac") {
            success = AK_UC(tweak);
        } else if (tweak_id == "disable_windows_ink_workspace") {
            success = AK_WI(tweak);
        } else if (tweak_id == "disable_windows_updates") {
            success = AK_WU(tweak);
        } else if (tweak_id == "pause_windows_updates") {
            success = AK_PU(tweak);
        } else if (tweak_id == "disable_driver_updates") {
            success = AK_DU(tweak);
        } else if (tweak_id == "disable_auto_time_zone_updater_service") {
            success = AK_TZ(tweak);
        } else if (tweak_id == "disable_connected_user_experiences_and_telemetry_service") {
            success = AK_CT(tweak);
        } else if (tweak_id == "disable_data_sharing_service") {
            success = AK_DS(tweak);
        } else if (tweak_id == "disable_windows_search_service") {
            success = AK_WS(tweak);
        } else if (tweak_id == "disable_windows_biometric_service") {
            success = AK_BS(tweak);
        } else if (tweak_id == "disable_tracking_services") {
            success = AK_TS(tweak);
        } else if (tweak_id == "disable_windows_defender") {
            success = AK_WD(tweak);
        } else if (tweak_id == "disable_firewall") {
            success = AK_FW(tweak);
        } else if (tweak_id == "disable_smb1") {
            success = AK_S1(tweak);
        } else if (tweak_id == "enhance_smartscreen") {
            success = AK_ES(tweak);
        } else if (tweak_id == "disable_preview") {
            success = AK_DP(tweak);
        } else if (tweak_id == "disable_handle_history") {
            success = AK_DH(tweak);
        } else if (tweak_id == "disable_metadata_retrieval") {
            success = AK_DM(tweak);
        } else if (tweak_id == "disable_thumbnails") {
            success = AK_DT(tweak);
        } else if (tweak_id == "disable_web_search") {
            success = AK_DW(tweak);
        } else {
            std::cerr << "Unknown tweak ID: " << tweak_id << std::endl;
            json failed_tweak;
            failed_tweak["id"] = tweak_id;
            failed_tweak["reason"] = "Unknown tweak ID";
            failed.push_back(failed_tweak);
            continue;
        }
        
        if (success) {
            successful.push_back(tweak_id);
        } else {
            json failed_tweak;
            failed_tweak["id"] = tweak_id;
            failed_tweak["reason"] = "Failed to apply tweak";
            failed.push_back(failed_tweak);
        }
    }
    
    results["successful"] = successful;
    results["failed"] = failed;
    
    return results;
} 