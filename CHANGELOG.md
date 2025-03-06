# Changelog

All notable changes to this project will be documented in this file.

## [v0.3.7] - 2023-11-11

### Added
- System restore point creation before applying tweaks for added safety
- Improved error handling for tweak application process
- Implemented comprehensive tweaks framework for applying system optimizations:
  - Created C++ backend module for registry modifications with ambiguous function names (AK, MY, ED)
  - Added support for both registry-based tweaks and command-line alternatives for maximum compatibility
  - Implemented fallback mechanisms to ensure tweaks can be applied even when primary methods fail
  - Added detailed progress tracking and result reporting for tweak application
  - Integrated restart detection and prompting for tweaks that require system restart
- Enhanced the tweaks UI with improved user experience:
  - Added confirmation dialogs before applying tweaks
  - Implemented progress dialog to show real-time tweak application status
  - Added detailed results summary with success/failure counts and specific error messages
  - Improved button styling and layout in the tweaks page

### Changed
- Enhanced progress dialog to show system restore point creation status
- Updated restart functionality to support both Windows and other operating systems
- All tweaks in the Tweaks page now start off deselected by default for better user control
- Improved overall UI aesthetics and consistency:
  - Enhanced dashboard layout with better spacing and container styling
  - Fixed text color issues in the tweaks section
  - Improved container styling with proper rounded corners and borders
  - Added better visual hierarchy with consistent spacing and padding
  - Enhanced button styling with improved hover and pressed states
  - Standardized color usage across the application using the global theme variables

## [v0.3.6] - 2023-11-10

### Changed
- All tweaks in the Tweaks page now start off deselected by default for better user control
- Various UI improvements:
  - Enhanced dashboard layout
  - Fixed text color issues
  - Improved container styling
  - Standardized color usage across the application

### Fixed
- Implemented functionality for "Go to Dashboard" button on Home page
- Added connections for "Scan System" and "Optimize Now" buttons
- Fixed main window reference in Home page to enable proper navigation

## [v0.3.5] - 2023-11-07

### Added
- Complete functionality for "Run System Analysis" button on the home page
  - System analysis with progress dialog and background processing
  - Comprehensive system evaluation including CPU, memory, storage, and process analysis
  - Gaming performance score calculation based on number of running processes
  - Results display with detailed recommendations
- Complete functionality for "System Information" button on the home page
  - Detailed system information dialog with tabbed interface
  - Hardware information including CPU, GPU, and battery details
  - Storage information with disk space analysis
  - Network information with interface details
- Added ability to navigate between pages from the home screen actions

## [v0.3.4] - 2023-11-06

### Changed
- Modified Performance Dashboard to show total system usage instead of individual metrics
- Added process count monitoring to dashboard 
- Implemented gaming score based on number of running processes
- Score criteria: below 120 processes = excellent, below 200 processes = good
- Added visual feedback with color-coded score indicators and descriptive messages

## [v0.3.3] - 2023-11-05

### Improved
- Enhanced hardware detection accuracy using platform-specific libraries (wmi on Windows)
- Added more detailed and accurate network information (using netifaces library)
- Added GPU detection for Windows and Linux systems
- Improved processor information with CPU speed display
- Better network interface identification and classification
- More reliable primary IP address detection
- Fixed storage detection with enhanced methods for Windows and Linux
- Added multiple fallback mechanisms for disk detection when primary methods fail
- Better formatting of storage sizes with appropriate units

## [v0.3.2] - 2023-11-03

### Changed
- Redesigned System Metrics page for improved stability
- Focus on static information instead of dynamic metrics
- Added static system information pages (System, Hardware, Storage, Network)
- Added battery status and system uptime information
- Simplified UI for better performance

## v0.3.1

- Fixed module import issue in the application:
  - Changed absolute import to use `__main__` module to avoid circular imports
  - Added frontend/__init__.py file to make the package structure proper
  - Made backend more robust in accessing the backend connector

- Enhanced the C++ backend with JSON support:
  - Added JSON handling using nlohmann/json library
  - Implemented command-line options for querying system metrics
  - Added simulated data for system metrics with ambiguous function names (GI, GO, GD, GN)
  - Updated CMakeLists.txt to properly handle the JSON library dependency

## v0.3

- Added theme support with dark and light mode:
  - Created TM (Theme Manager) with ambiguous methods (ap_te, ap_dk, ap_lt)
  - Added theme switching in SE (Settings) page
  - Integrated theme changes throughout the UI components
  - Made all components theme-aware with dynamic styling

- Added BE (Backend) integration for accurate system metrics:
  - Created BC (Backend Connector) with ambiguous methods (gt_sy, gt_cp, gt_mm, etc.)
  - Integrated backend connector with SM (System Metrics) page
  - Implemented robust fallback mechanisms using psutil when backend is unavailable
  - Modified SM page to use real system data from backend with ambiguous function names

- Ensured all files are under 500 lines of code with modular structure

## v0.2

- Created comprehensive FE (Frontend) with ambiguous function and class naming:
  - Implemented MN (Main) entry point
  - Created MW (Main Window) component
  - Added HR (Header) with project name and creator info
  - Implemented SR (Sidebar) navigation with 5 sections
  - Added all page components:
    - HE (Home) with quick action cards
    - DE (Dashboard) with performance metrics
    - SE (Settings) with app and performance configuration
    - SM (System Metrics) with detailed system information
    - TS (Tweaks) with categorized performance tweaks
  - Added requirements.txt for frontend dependencies
  - Used ambiguous method names throughout (stUI, ce_bn, te_cs, etc.)

## v0.1

- Created the project structure with two main components: FE (frontend) and BE (backend).
    - FE: Developed using Python Qt with ambiguous class and function names (e.g., MW, stUI, BE).
    - BE: Developed using C++ with ambiguous function names (e.g., LE) and a CMake build file.

- Added README.md for overall project description.
- Added docs/README.md for supporting documentation (DS).
- Added TweaksInfo file as a placeholder for future tweaks.

## v0.3.2 - System Metrics Redesign
- Redesigned the System Metrics page for improved stability
- Focused on static information rather than dynamic metrics
- Added static system information pages organized into four tabs: System, Hardware, Storage, and Network
- Added battery status and system uptime information
- Simplified UI for better performance

## v0.3.3 - Tweaks Module Implementation
- Completely restructured the Tweaks system with a modular approach
- Implemented a base tweaks class (BS) for consistent UI across all tweak categories
- Created specialized tweak modules for different categories:
  - Performance Tweaks (PE): Memory, CPU, Power, and Network optimizations
  - Gaming Tweaks (GE): Input latency, graphics performance, and gaming-specific settings
  - Privacy Tweaks (PY): Telemetry controls, location settings, and app permissions
  - Security Tweaks (SY): Windows security features, firewall settings, and browser safety
- Added detailed descriptions and safety ratings for all tweaks
- Improved the tweak application process with progress tracking
- Implemented confirmation dialogs and better user feedback 