#pragma once

#include <string>
#include <Windows.h>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

using json = nlohmann::json;


bool MY(const std::string& key_path, const std::string& value_name, DWORD value_type, const void* data, DWORD data_size);
bool ED(const std::string& command);
json PS(const json& tweaks);


bool AK_BD(const json& params); 
bool AK_BS(const json& params); 
bool AK_MN(const json& params); 
bool AK_RH(const json& params); 
bool AK_PE(const json& params); 
bool AK_MM(const json& params); 
bool AK_AF(const json& params); 
bool AK_BT(const json& params); 
bool AK_FT(const json& params); 
bool AK_PS(const json& params); 
bool AK_PF(const json& params); 
bool AK_HS(const json& params); 
bool AK_SS(const json& params); 
bool AK_SM(const json& params); 


bool AK_MA(const json& params); 
bool AK_VE(const json& params); 
bool AK_ST(const json& params); 
bool AK_AR(const json& params); 
bool AK_NS(const json& params); 
bool AK_SB(const json& params); 
bool AK_LP(const json& params); 

bool AK_UP(const json& params); 
bool AK_PT(const json& params); 
bool AK_AO(const json& params); 
bool AK_CP(const json& params); 
bool AK_GR(const json& params); 
bool AK_GD(const json& params); 
bool AK_GM(const json& params); 
bool AK_FS(const json& params); 

bool AK_OC(const json& params);
bool AK_EP(const json& params);
bool AK_OG(const json& params);
bool AK_OD(const json& params);
bool AK_OV(const json& params);
bool AK_OT(const json& params);
bool AK_OU(const json& params);
bool AK_RL(const json& params);
bool AK_PG(const json& params);
bool AK_OS(const json& params);

bool AK_HP(const json& params);
bool AK_DO(const json& params);
bool AK_SF(const json& params);
bool AK_HB(const json& params);
bool AK_TR(const json& params);
bool AK_DT(const json& params);
bool AK_NT(const json& params);
bool AK_AT(const json& params);

bool AK_LT(const json& params); 
bool AK_TY(const json& params); 
bool AK_AL(const json& params); 
bool AK_FB(const json& params); 
bool AK_DD(const json& params); 
bool AK_TE(const json& params); 
bool AK_AH(const json& params); 

bool AK_AD(const json& params); 
bool AK_AI(const json& params); 
bool AK_AC(const json& params); 
bool AK_CA(const json& params); 
bool AK_CM(const json& params); 
bool AK_EM(const json& params); 
bool AK_MS(const json& params); 
bool AK_PH(const json& params); 

bool AK_OA(const json& params); 
bool AK_BG(const json& params); 
bool AK_DG(const json& params); 

bool AK_PC(const json& params); 
bool AK_VD(const json& params); 


bool AK_RA(const json& params); 
bool AK_RS(const json& params); 
bool AK_SF(const json& params); 

bool AK_AS(const json& params); 
bool AK_UC(const json& params); 
bool AK_WI(const json& params); 
bool AK_WU(const json& params); 
bool AK_PU(const json& params); 
bool AK_DU(const json& params); 
bool AK_TZ(const json& params); 
bool AK_CT(const json& params); 
bool AK_DS(const json& params); 
bool AK_WS(const json& params); 

bool AK_TS(const json& params); 
bool AK_WD(const json& params); 
bool AK_FW(const json& params); 
bool AK_S1(const json& params); 
bool AK_ES(const json& params); 
bool AK_DP(const json& params); 
bool AK_DH(const json& params); 
bool AK_DM(const json& params); 
bool AK_DT(const json& params); 
bool AK_DW(const json& params); 