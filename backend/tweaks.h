#pragma once

#include <string>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

bool MY(const std::string& key_path, const std::string& value_name, DWORD value_type, const void* data, DWORD data_size);
bool ED(const std::string& command);
json PS(const json& tweaks);

bool AK_BD(const json& params); // ApplyTweak_BcDedit
bool AK_BS(const json& params); // ApplyTweak_BackgroundApps
bool AK_MN(const json& params); // ApplyTweak_MemoryCompression
bool AK_RH(const json& params); // ApplyTweak_RamUsageHigh
bool AK_PE(const json& params); // ApplyTweak_PageFile
bool AK_MM(const json& params); // ApplyTweak_MMCSS
bool AK_AF(const json& params); // ApplyTweak_AutomaticFolderDiscovery
bool AK_BT(const json& params); // ApplyTweak_BootTracing
bool AK_FT(const json& params); // ApplyTweak_FaultTolerantHeap
bool AK_PS(const json& params); // ApplyTweak_PagingSettings
bool AK_PF(const json& params); // ApplyTweak_Prefetch
bool AK_HS(const json& params); // ApplyTweak_HostSplitting
bool AK_SS(const json& params); // ApplyTweak_SleepStudy
bool AK_SM(const json& params); // ApplyTweak_SpectreAndMeltdown

bool AK_MA(const json& params); // ApplyTweak_MouseAcceleration
bool AK_VE(const json& params); // ApplyTweak_VisualEffects
bool AK_ST(const json& params); // ApplyTweak_ShutdownTime
bool AK_AR(const json& params); // ApplyTweak_AutorunAutoplay
bool AK_NS(const json& params); // ApplyTweak_NetworkSettings
bool AK_SB(const json& params); // ApplyTweak_SMBBandwidthThrottling
bool AK_LP(const json& params); // ApplyTweak_LLMNRProtocol
bool AK_UP(const json& params); // ApplyTweak_UltimatePerformancePowerPlan
bool AK_PT(const json& params); // ApplyTweak_PowerThrottling
bool AK_AO(const json& params); // ApplyTweak_AdvancedPowerOptions
bool AK_CP(const json& params); // ApplyTweak_CoreParking
bool AK_GR(const json& params); // ApplyTweak_GameBar
bool AK_GD(const json& params); // ApplyTweak_GameDVR
bool AK_GM(const json& params); // ApplyTweak_GameMode
bool AK_FS(const json& params); // ApplyTweak_FullscreenOptimizations

bool AK_LT(const json& params); // ApplyTweak_LocationTracking
bool AK_TY(const json& params); // ApplyTweak_Telemetry
bool AK_AL(const json& params); // ApplyTweak_AppLocation
bool AK_FB(const json& params); // ApplyTweak_Feedback
bool AK_DD(const json& params); // ApplyTweak_DiagnosticData
bool AK_TE(const json& params); // ApplyTweak_TailoredExperiences
bool AK_AH(const json& params); // ApplyTweak_ActivityHistory
bool AK_AD(const json& params); // ApplyTweak_AdvertisingID
bool AK_AI(const json& params); // ApplyTweak_AccountInfo
bool AK_AC(const json& params); // ApplyTweak_AppContacts
bool AK_CA(const json& params); // ApplyTweak_CalendarAccess
bool AK_CM(const json& params); // ApplyTweak_CallHistory
bool AK_EM(const json& params); // ApplyTweak_EmailAccess
bool AK_MS(const json& params); // ApplyTweak_MessagesAccess
bool AK_PH(const json& params); // ApplyTweak_PhoneAccess
bool AK_OA(const json& params); // ApplyTweak_OtherDevicesAccess
bool AK_BG(const json& params); // ApplyTweak_BackgroundAppsAccess
bool AK_DG(const json& params); // ApplyTweak_DiagnosticsAccess
bool AK_PC(const json& params); // ApplyTweak_PicturesAccess
bool AK_VD(const json& params); // ApplyTweak_VideosAccess

bool AK_RA(const json& params); // ApplyTweak_RestrictAnonymousAccess
bool AK_RS(const json& params); // ApplyTweak_RestrictAnonymousEnumerationOfShares
bool AK_SF(const json& params); // ApplyTweak_SmartScreenFilter
bool AK_AS(const json& params); // ApplyTweak_AutomaticSampleSubmission
bool AK_UC(const json& params); // ApplyTweak_UAC
bool AK_WI(const json& params); // ApplyTweak_WindowsInkWorkspace
bool AK_WU(const json& params); // ApplyTweak_WindowsUpdates
bool AK_PU(const json& params); // ApplyTweak_PauseWindowsUpdates
bool AK_DU(const json& params); // ApplyTweak_DriverUpdates
bool AK_TZ(const json& params); // ApplyTweak_TimeZoneUpdater
bool AK_CT(const json& params); // ApplyTweak_ConnectedUserExperiencesAndTelemetry
bool AK_DS(const json& params); // ApplyTweak_DataSharingService
bool AK_WS(const json& params); // ApplyTweak_WindowsSearchService
bool AK_TS(const json& params); // ApplyTweak_TrackingServices
bool AK_WD(const json& params); // ApplyTweak_WindowsDefender
bool AK_FW(const json& params); // ApplyTweak_Firewall
bool AK_S1(const json& params); // ApplyTweak_SMB1
bool AK_ES(const json& params); // ApplyTweak_EnhanceSmartscreen
bool AK_DP(const json& params); // ApplyTweak_DisablePreview
bool AK_DH(const json& params); // ApplyTweak_DisableHandleHistory
bool AK_DM(const json& params); // ApplyTweak_DisableMetadataRetrieval
bool AK_DT(const json& params); // ApplyTweak_DisableThumbnails
bool AK_DW(const json& params); // ApplyTweak_DisableWebSearch 