#include <iostream>
#include <string>
#include <vector>
#include <map>
#include "nlohmann/json.hpp"  
#include "tweaks.h"

using json = nlohmann::json;

json PS(const json& tweaks);

void LE() {
    std::cout << "Optimizing PC for gaming..." << std::endl;
    
}


json GI() {
    json result;
    
    
    result["os"] = "Windows 10";
    result["version"] = "10.0.19045";
    result["hostname"] = "DESKTOP-PC";
    result["processor"] = "AMD Ryzen 7 5800X 8-Core Processor";
    result["architecture"] = "x64";
    result["boot_time"] = "2023-06-15 08:22:45";
    
    return result;
}


json GI_CPU() {
    json result;
    json cpu;
    
    
    cpu["name"] = "AMD Ryzen 7 5800X";
    cpu["physical_cores"] = 8;
    cpu["logical_cores"] = 16;
    cpu["max_frequency"] = "3.8 GHz";
    cpu["current_frequency"] = "4.2 GHz";
    cpu["usage"] = 25;
    cpu["temperature"] = 45;
    
    
    std::vector<json> cores;
    for (int i = 0; i < 16; i++) {
        json core;
        core["id"] = i;
        core["usage"] = 10 + (i * 5) % 90; 
        core["frequency"] = "4." + std::to_string(i % 7) + " GHz";
        cores.push_back(core);
    }
    
    cpu["cores"] = cores;
    result["cpu"] = cpu;
    
    return result;
}


json GO() {
    json result;
    
    
    json memory;
    memory["total"] = 32 * 1024 * 1024 * 1024LL; 
    memory["available"] = 24 * 1024 * 1024 * 1024LL; 
    memory["used"] = 8 * 1024 * 1024 * 1024LL; 
    memory["percent"] = 25; 
    
    json swap;
    swap["total"] = 16 * 1024 * 1024 * 1024LL; 
    swap["used"] = 2 * 1024 * 1024 * 1024LL; 
    swap["free"] = 14 * 1024 * 1024 * 1024LL; 
    swap["percent"] = 12; 
    
    result["memory"] = memory;
    result["swap"] = swap;
    
    return result;
}


json GD() {
    json result;
    std::vector<json> disks;
    
    
    json disk1;
    disk1["device"] = "C:";
    disk1["mount"] = "C:";
    disk1["fs_type"] = "NTFS";
    disk1["total"] = 500 * 1024 * 1024 * 1024LL; 
    disk1["used"] = 300 * 1024 * 1024 * 1024LL; 
    disk1["free"] = 200 * 1024 * 1024 * 1024LL; 
    disk1["percent"] = 60; 
    disks.push_back(disk1);
    
    json disk2;
    disk2["device"] = "D:";
    disk2["mount"] = "D:";
    disk2["fs_type"] = "NTFS";
    disk2["total"] = 1000 * 1024 * 1024 * 1024LL; 
    disk2["used"] = 500 * 1024 * 1024 * 1024LL; 
    disk2["free"] = 500 * 1024 * 1024 * 1024LL; 
    disk2["percent"] = 50; 
    disks.push_back(disk2);
    
    result["disks"] = disks;
    
    return result;
}


json GN() {
    json result;
    std::vector<json> interfaces;
    
    
    json interface1;
    interface1["name"] = "Ethernet";
    interface1["address"] = "192.168.1.100";
    interface1["netmask"] = "255.255.255.0";
    interface1["gateway"] = "192.168.1.1";
    interface1["dns"] = std::vector<std::string>{"8.8.8.8", "8.8.4.4"};
    interface1["bytes_sent"] = 1024 * 1024 * 10; 
    interface1["bytes_recv"] = 1024 * 1024 * 100; 
    interfaces.push_back(interface1);
    
    json interface2;
    interface2["name"] = "Wi-Fi";
    interface2["address"] = "192.168.1.101";
    interface2["netmask"] = "255.255.255.0";
    interface2["gateway"] = "192.168.1.1";
    interface2["dns"] = std::vector<std::string>{"8.8.8.8", "8.8.4.4"};
    interface2["bytes_sent"] = 1024 * 1024 * 5; 
    interface2["bytes_recv"] = 1024 * 1024 * 50; 
    interfaces.push_back(interface2);
    
    result["interfaces"] = interfaces;
    
    return result;
}


json HD(const std::string& command, const json& params) {
    if (command == "system_info") {
        return GI();
    } else if (command == "cpu_info") {
        return GI_CPU();
    } else if (command == "memory_info") {
        return GO();
    } else if (command == "disk_info") {
        return GD();
    } else if (command == "network_info") {
        return GN();
    } else if (command == "apply_tweaks") {
        return PS(params);
    } else {
        json error;
        error["error"] = "Unknown command: " + command;
        return error;
    }
}


int main(int argc, char* argv[]) {
    
    if (argc > 1) {
        std::string arg = argv[1];
        
        if (arg == "test") {
            
            std::cout << "CovEngineV2 Backend Test Mode" << std::endl;
            std::cout << "System Info: " << GI().dump(4) << std::endl;
            std::cout << "CPU Info: " << GI_CPU().dump(4) << std::endl;
            std::cout << "Memory Info: " << GO().dump(4) << std::endl;
            std::cout << "Disk Info: " << GD().dump(4) << std::endl;
            std::cout << "Network Info: " << GN().dump(4) << std::endl;
            return 0;
        } else if (arg == "command" && argc > 2) {
            
            std::string command = argv[2];
            json params;
            
            
            if (argc > 3) {
                try {
                    params = json::parse(argv[3]);
                } catch (const std::exception& e) {
                    std::cerr << "Error parsing JSON: " << e.what() << std::endl;
                    return 1;
                }
            }
            
            
            json result = HD(command, params);
            
            
            std::cout << result.dump() << std::endl;
            
            return 0;
        }
    }
    
    
    std::cout << "CovEngineV2 Backend Interactive Mode" << std::endl;
    std::cout << "Enter commands (type 'exit' to quit):" << std::endl;
    
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line == "exit") {
            break;
        }
        
        
        std::string command;
        json params;
        
        size_t space_pos = line.find(' ');
        if (space_pos != std::string::npos) {
            command = line.substr(0, space_pos);
            std::string params_str = line.substr(space_pos + 1);
            
            try {
                params = json::parse(params_str);
            } catch (const std::exception& e) {
                std::cerr << "Error parsing JSON: " << e.what() << std::endl;
                continue;
            }
        } else {
            command = line;
        }
        
        
        json result = HD(command, params);
        
        
        std::cout << result.dump(4) << std::endl;
    }
    
    return 0;
} 