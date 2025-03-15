#include <windows.h>
#include <wininet.h>
#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <tlhelp32.h>
#include <thread>
#include <chrono>
#include <shlwapi.h>
#include <stdio.h>

#pragma comment(lib, "wininet.lib")
#pragma comment(lib, "shlwapi.lib")

namespace fs = std::filesystem;

std::string wc_to_s(const wchar_t* wstr) {
    int size = WideCharToMultiByte(CP_UTF8, 0, wstr, -1, nullptr, 0, nullptr, nullptr);
    std::string result(size - 1, ' ');
    WideCharToMultiByte(CP_UTF8, 0, wstr, -1, &result[0], size, nullptr, nullptr);
    return result;
}

bool dl_fl(HINTERNET hInternet, const std::string& url, const std::string& filePath) {
    HINTERNET hFile = InternetOpenUrlA(hInternet, url.c_str(), NULL, 0, 
        INTERNET_FLAG_RELOAD | INTERNET_FLAG_NO_CACHE_WRITE | INTERNET_FLAG_SECURE | 
        INTERNET_FLAG_IGNORE_CERT_DATE_INVALID | INTERNET_FLAG_IGNORE_CERT_CN_INVALID, 0);
    
    if (hFile) {
        char buffer[4096];
        DWORD bytesRead;
        HANDLE hLocalFile = CreateFileA(filePath.c_str(), GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
        
        if (hLocalFile != INVALID_HANDLE_VALUE) {
            while (InternetReadFile(hFile, buffer, sizeof(buffer), &bytesRead) && bytesRead > 0) {
                WriteFile(hLocalFile, buffer, bytesRead, &bytesRead, NULL);
            }
            CloseHandle(hLocalFile);
            InternetCloseHandle(hFile);
            return true;
        } else {
            std::cerr << "Error creating local file. Error: " << GetLastError() << std::endl;
            InternetCloseHandle(hFile);
            return false;
        }
    } else {
        std::cerr << "Error opening URL. Error: " << GetLastError() << std::endl;
        return false;
    }
}

void rn_el_cmd(const std::string& command) {
    SHELLEXECUTEINFOA sei = { sizeof(sei) };
    sei.lpVerb = "runas";
    sei.lpFile = "cmd.exe";
    sei.lpParameters = ("/c " + command).c_str();
    sei.hwnd = NULL;
    sei.nShow = SW_HIDE;

    if (!ShellExecuteExA(&sei)) {
        DWORD errorCode = GetLastError();
        std::cerr << "ShellExecuteEx failed. Error: " << errorCode << std::endl;
    }
}

BOOL tm_ps(const std::string& processName) {
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot == INVALID_HANDLE_VALUE) {
        std::cerr << "CreateToolhelp32Snapshot failed. Error: " << GetLastError() << std::endl;
        return FALSE;
    }

    PROCESSENTRY32W pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32W);

    if (!Process32FirstW(hSnapshot, &pe32)) {
        std::cerr << "Process32First failed. Error: " << GetLastError() << std::endl;
        CloseHandle(hSnapshot);
        return FALSE;
    }

    BOOL result = FALSE;
    do {
        wchar_t wProcessName[MAX_PATH];
        mbstowcs(wProcessName, processName.c_str(), processName.length() + 1);
        
        if (_wcsicmp(pe32.szExeFile, wProcessName) == 0) {
            HANDLE hProcess = OpenProcess(PROCESS_TERMINATE, FALSE, pe32.th32ProcessID);
            if (hProcess != NULL) {
                if (TerminateProcess(hProcess, 1)) {
                    result = TRUE;
                }
                CloseHandle(hProcess);
            }
        }
    } while (Process32NextW(hSnapshot, &pe32));

    CloseHandle(hSnapshot);
    return result;
}

bool ck_ps(const std::string& processName) {
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot == INVALID_HANDLE_VALUE) {
        return false;
    }

    PROCESSENTRY32W pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32W);

    if (!Process32FirstW(hSnapshot, &pe32)) {
        CloseHandle(hSnapshot);
        return false;
    }

    do {
        wchar_t wProcessName[MAX_PATH];
        mbstowcs(wProcessName, processName.c_str(), processName.length() + 1);
        
        if (_wcsicmp(pe32.szExeFile, wProcessName) == 0) {
            CloseHandle(hSnapshot);
            return true;
        }
    } while (Process32NextW(hSnapshot, &pe32));

    CloseHandle(hSnapshot);
    return false;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: SPF.exe check|spoof|udspoof" << std::endl;
        return 1;
    }

    std::string command = argv[1];

    if (command == "check") {
        std::vector<std::string> gamesToCheck = {"Fortnite.exe", "VALORANT.exe", "RainbowSix.exe"};
        for (const auto& game : gamesToCheck) {
            if (ck_ps(game)) {
                std::cout << "Running: " << game << std::endl;
                return 0;
            }
        }
        std::cout << "No blocked games running" << std::endl;
        return 0;
    } 
    else if (command == "spoof") {
        char buffer[MAX_PATH];
        GetModuleFileNameA(NULL, buffer, MAX_PATH);
        std::string::size_type pos = std::string(buffer).find_last_of("\\/");
        std::string directory = std::string(buffer).substr(0, pos);

        HINTERNET hInternet = InternetOpenA("SpoofAgent", INTERNET_OPEN_TYPE_DIRECT, NULL, 0, INTERNET_FLAG_RELOAD);
        if (!hInternet) {
            std::cerr << "Error initializing WinINet. Error: " << GetLastError() << std::endl;
            return 1;
        }

        std::string driverPath = directory + "\\qg94sa.sys";
        std::string mapperPath = directory + "\\mapper.exe";

        std::cout << "Downloading driver..." << std::endl;
        if (!dl_fl(hInternet, "REPLACE WITH YOUR DRIVER", driverPath)) {
            std::cerr << "Error downloading driver." << std::endl;
            InternetCloseHandle(hInternet);
            return 1;
        }

        std::cout << "Downloading mapper..." << std::endl;
        if (!dl_fl(hInternet, "REPLACE WITH YOUR MAPPER", mapperPath)) {
            std::cerr << "Error downloading mapper." << std::endl;
            DeleteFileA(driverPath.c_str());
            InternetCloseHandle(hInternet);
            return 1;
        }

        std::cout << "Mapping driver..." << std::endl;
        std::string mapCommand = "powershell -Command \"Start-Process '" + mapperPath + "' -ArgumentList '" + driverPath + "' -Verb RunAs -Wait\"";
        system(mapCommand.c_str());

        std::this_thread::sleep_for(std::chrono::seconds(5));

        std::cout << "Stopping WMI service..." << std::endl;
        rn_el_cmd("net stop winmgmt /y");

        std::this_thread::sleep_for(std::chrono::seconds(2));

        std::cout << "Cleaning up..." << std::endl;
        DeleteFileA(driverPath.c_str());
        DeleteFileA(mapperPath.c_str());

        InternetCloseHandle(hInternet);

        std::cout << "Spoof completed successfully" << std::endl;
        return 0;
    }
    else if (command == "udspoof") {
        char buffer[MAX_PATH];
        GetModuleFileNameA(NULL, buffer, MAX_PATH);
        std::string::size_type pos = std::string(buffer).find_last_of("\\/");
        std::string directory = std::string(buffer).substr(0, pos);

        HINTERNET hInternet = InternetOpenA("SpoofAgent", INTERNET_OPEN_TYPE_DIRECT, NULL, 0, INTERNET_FLAG_RELOAD);
        if (!hInternet) {
            std::cerr << "Error initializing WinINet. Error: " << GetLastError() << std::endl;
            return 1;
        }

        std::string driverPath = directory + "\\pwbvm3.sys";
        std::string mapperPath = directory + "\\mapper2.exe";

        std::cout << "Downloading UD driver..." << std::endl;
        if (!dl_fl(hInternet, "REPLACE WITH YOUR UD DRIVER", driverPath)) {
            std::cerr << "Error downloading UD driver." << std::endl;
            InternetCloseHandle(hInternet);
            return 1;
        }

        std::cout << "Downloading UD mapper..." << std::endl;
        if (!dl_fl(hInternet, "REPLACE WITH YOUR MAPPER", mapperPath)) {
            std::cerr << "Error downloading UD mapper." << std::endl;
            DeleteFileA(driverPath.c_str());
            InternetCloseHandle(hInternet);
            return 1;
        }

        std::cout << "Mapping UD driver..." << std::endl;
        std::string mapCommand = "powershell -Command \"Start-Process '" + mapperPath + "' -ArgumentList '" + driverPath + "' -Verb RunAs -Wait\"";
        system(mapCommand.c_str());

        std::this_thread::sleep_for(std::chrono::seconds(5));

        std::cout << "Stopping WMI service..." << std::endl;
        rn_el_cmd("net stop winmgmt /y");

        std::this_thread::sleep_for(std::chrono::seconds(2));

        std::cout << "Cleaning up UD files..." << std::endl;
        DeleteFileA(driverPath.c_str());
        DeleteFileA(mapperPath.c_str());

        InternetCloseHandle(hInternet);

        std::cout << "UD Spoof completed successfully" << std::endl;
        return 0;
    }
    else {
        std::cerr << "Unknown command: " << command << std::endl;
        return 1;
    }
} 