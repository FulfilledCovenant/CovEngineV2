import os
import json
import logging
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, 
    QLabel, QPushButton, QLineEdit, QTextEdit, 
    QGroupBox, QGridLayout, QCheckBox, QComboBox,
    QFileDialog, QMessageBox, QSplitter, QSpinBox,
    QFormLayout
)
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QFont, QColor

from frontend.ui.gl_st import GS

class FF(QScrollArea):
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("FFlagsTab")
        self.ps = {}
        self.rs_path = None
        self.ui_ud = False
        self.init_ui()
        
    def init_ui(self):
        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.NoFrame)
        
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        header_layout = QHBoxLayout()
        layout.addLayout(header_layout)
        
        title = QLabel("Roblox FFlags Editor")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        desc = QLabel("A modular fast-flags editor and tool for Roblox")
        desc.setFont(QFont("Segoe UI", 11))
        desc.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']};")
        desc.setAlignment(Qt.AlignLeft)
        desc.setContentsMargins(0, 5, 0, 15)
        layout.addWidget(desc)
        
        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(8)
        splitter.setStyleSheet(f"""
            QSplitter::handle {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                margin: 1px 1px 1px 1px;
                border-radius: 4px;
            }}
        """)
        
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 10, 0)
        left_layout.setSpacing(15)
        
        status_group = QGroupBox("Status")
        status_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
        """)
        status_layout = QVBoxLayout()
        status_layout.setContentsMargins(15, 15, 15, 15)
        
        self.status_label = QLabel("Scanning for Roblox installation...")
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
        status_layout.addWidget(self.status_label)
        
        status_group.setLayout(status_layout)
        left_layout.addWidget(status_group)
        
        common_settings_group = QGroupBox("Common Settings")
        common_settings_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
            QComboBox, QSpinBox {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                color: {GS.DARK_THEME['text_primary']};
                border-radius: 6px;
                padding: 6px;
                min-height: 18px;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 20px;
            }}
            QCheckBox {{
                color: {GS.DARK_THEME['text_primary']};
                padding: 2px;
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                background-color: {GS.DARK_THEME['bg_tertiary']};
            }}
            QCheckBox::indicator:checked {{
                background-color: {GS.DARK_THEME['accent']};
                border: 1px solid {GS.DARK_THEME['accent']};
                image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
            }}
            QCheckBox::indicator:unchecked:hover {{
                border: 1px solid {GS.DARK_THEME['accent']};
            }}
            QSpinBox::up-button, QSpinBox::down-button {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                border-radius: 3px;
            }}
            QLabel {{
                color: {GS.DARK_THEME['text_primary']};
            }}
        """)
        
        common_settings_layout = QFormLayout()
        common_settings_layout.setContentsMargins(15, 15, 15, 15)
        common_settings_layout.setVerticalSpacing(12)
        common_settings_layout.setLabelAlignment(Qt.AlignLeft)
        
        msaa_label = QLabel("Anti-aliasing (MSAA):")
        self.msaa_combo = QComboBox()
        self.msaa_combo.addItem("Off", 0)
        self.msaa_combo.addItem("1x", 1)
        self.msaa_combo.addItem("2x", 2)
        self.msaa_combo.addItem("4x", 4)
        self.msaa_combo.currentIndexChanged.connect(self.cs_cd)
        common_settings_layout.addRow(msaa_label, self.msaa_combo)
        
        shadows_label = QLabel("Player shadows:")
        self.shadows_check = QCheckBox("")
        self.shadows_check.stateChanged.connect(self.cs_cd)
        self.shadows_check.stateChanged.connect(lambda state: self.ud_cb_tx(self.shadows_check, state))
        self.shadows_check.setText("Enabled" if self.shadows_check.isChecked() else "Disabled")
        common_settings_layout.addRow(shadows_label, self.shadows_check)
        
        postfx_label = QLabel("Post-processing effects:")
        self.postfx_check = QCheckBox("")
        self.postfx_check.stateChanged.connect(self.cs_cd)
        self.postfx_check.stateChanged.connect(lambda state: self.ud_cb_tx(self.postfx_check, state))
        self.postfx_check.setText("Enabled" if self.postfx_check.isChecked() else "Disabled")
        common_settings_layout.addRow(postfx_label, self.postfx_check)
        
        terrain_label = QLabel("Terrain textures:")
        self.terrain_check = QCheckBox("")
        self.terrain_check.stateChanged.connect(self.cs_cd)
        self.terrain_check.stateChanged.connect(lambda state: self.ud_cb_tx(self.terrain_check, state))
        self.terrain_check.setText("Enabled" if self.terrain_check.isChecked() else "Disabled")
        common_settings_layout.addRow(terrain_label, self.terrain_check)
        
        fps_label = QLabel("FPS limit:")
        self.fps_spin = QSpinBox()
        self.fps_spin.setRange(0, 9999)
        self.fps_spin.setValue(0)
        self.fps_spin.setSpecialValueText("Default")
        self.fps_spin.valueChanged.connect(self.cs_cd)
        common_settings_layout.addRow(fps_label, self.fps_spin)
        
        render_label = QLabel("Rendering mode:")
        self.render_combo = QComboBox()
        self.render_combo.addItem("Default", "default")
        self.render_combo.addItem("DirectX 11", "dx11")
        self.render_combo.addItem("DirectX 10", "dx10")
        self.render_combo.currentIndexChanged.connect(self.cs_cd)
        common_settings_layout.addRow(render_label, self.render_combo)
        
        texture_label = QLabel("Texture quality:")
        self.texture_combo = QComboBox()
        self.texture_combo.addItem("Low", 0)
        self.texture_combo.addItem("Medium", 1)
        self.texture_combo.addItem("High", 2)
        self.texture_combo.addItem("Ultra", 3)
        self.texture_combo.currentIndexChanged.connect(self.cs_cd)
        common_settings_layout.addRow(texture_label, self.texture_combo)
        
        dpi_label = QLabel("DPI Scaling:")
        self.dpi_check = QCheckBox("")
        self.dpi_check.stateChanged.connect(self.cs_cd)
        self.dpi_check.stateChanged.connect(lambda state: self.ud_cb_tx(self.dpi_check, state))
        self.dpi_check.setText("Disabled" if self.dpi_check.isChecked() else "Enabled")
        common_settings_layout.addRow(dpi_label, self.dpi_check)
        
        common_settings_group.setLayout(common_settings_layout)
        left_layout.addWidget(common_settings_group)
        
        preset_group = QGroupBox("Presets")
        preset_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
            QComboBox {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                color: {GS.DARK_THEME['text_primary']};
                border-radius: 6px;
                padding: 8px;
                min-height: 20px;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 24px;
            }}
            QPushButton {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                color: {GS.DARK_THEME['text_primary']};
                border-radius: 6px;
                padding: 8px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {GS.DARK_THEME['bg_hover']};
            }}
        """)
        preset_layout = QVBoxLayout()
        preset_layout.setContentsMargins(15, 15, 15, 15)
        preset_layout.setSpacing(10)
        
        self.preset_combo = QComboBox()
        self.preset_combo.addItem("Optimized Performance")
        self.preset_combo.addItem("Default Settings")
        preset_layout.addWidget(self.preset_combo)
        
        preset_buttons = QHBoxLayout()
        preset_buttons.setSpacing(10)
        
        load_preset_btn = QPushButton("Load Preset")
        load_preset_btn.clicked.connect(self.ld_pt)
        preset_buttons.addWidget(load_preset_btn)
        
        save_preset_btn = QPushButton("Save Current")
        save_preset_btn.clicked.connect(self.sv_pt)
        preset_buttons.addWidget(save_preset_btn)
        
        preset_layout.addLayout(preset_buttons)
        preset_group.setLayout(preset_layout)
        left_layout.addWidget(preset_group)
        
        actions_group = QGroupBox("Actions")
        actions_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
            QPushButton {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                color: {GS.DARK_THEME['text_primary']};
                border-radius: 6px;
                padding: 8px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {GS.DARK_THEME['bg_hover']};
            }}
        """)
        actions_layout = QVBoxLayout()
        actions_layout.setContentsMargins(15, 15, 15, 15)
        actions_layout.setSpacing(10)
        
        detect_btn = QPushButton("Detect Roblox Installation")
        detect_btn.clicked.connect(self.dt_rb)
        actions_layout.addWidget(detect_btn)
        
        apply_btn = QPushButton("Apply FFlags")
        apply_btn.clicked.connect(self.ap_ff)
        apply_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {GS.DARK_THEME['accent']};
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {GS.DARK_THEME['accent_hover']};
            }}
        """)
        actions_layout.addWidget(apply_btn)
        
        backup_actions = QHBoxLayout()
        backup_actions.setSpacing(10)
        
        backup_btn = QPushButton("Create Backup")
        backup_btn.clicked.connect(self.cr_bk)
        backup_actions.addWidget(backup_btn)
        
        restore_btn = QPushButton("Restore Backup")
        restore_btn.clicked.connect(self.rs_bk)
        backup_actions.addWidget(restore_btn)
        
        actions_layout.addLayout(backup_actions)
        actions_group.setLayout(actions_layout)
        left_layout.addWidget(actions_group)
        
        filter_group = QGroupBox("Filter")
        filter_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
            QLineEdit {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                color: {GS.DARK_THEME['text_primary']};
                border-radius: 6px;
                padding: 8px;
                selection-background-color: {GS.DARK_THEME['accent']};
            }}
        """)
        filter_layout = QVBoxLayout()
        filter_layout.setContentsMargins(15, 15, 15, 15)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search flags...")
        self.search_input.textChanged.connect(self.ft_fg)
        filter_layout.addWidget(self.search_input)
        
        filter_group.setLayout(filter_layout)
        left_layout.addWidget(filter_group)
        
        left_layout.addStretch()
        
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(10, 0, 0, 0)
        
        editor_group = QGroupBox("FFlags Editor")
        editor_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
            QTextEdit {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                color: {GS.DARK_THEME['text_primary']};
                border-radius: 6px;
                padding: 8px;
                selection-background-color: {GS.DARK_THEME['accent']};
            }}
        """)
        editor_layout = QVBoxLayout()
        editor_layout.setContentsMargins(15, 15, 15, 15)
        
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("// Edit JSON directly here or use the preset options, do not modify the preset options if you do not know what you are doing!")
        self.editor.setFont(QFont("Consolas", 10))
        self.editor.setLineWrapMode(QTextEdit.NoWrap)
        self.editor.textChanged.connect(self.ed_td)
        editor_layout.addWidget(self.editor)
        
        editor_group.setLayout(editor_layout)
        right_layout.addWidget(editor_group)
        
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([350, 650])
        
        layout.addWidget(splitter)
        
        self.setWidget(content)
        
        self.ld_df_cf()
        self.dt_rb()
    
    def cs_cd(self):
        if self.ui_ud:
            return
        
        try:
            config = json.loads(self.editor.toPlainText())
            
            msaa_value = self.msaa_combo.currentData()
            if msaa_value == 0:
                if "FIntDebugForceMSAASamples" in config:
                    del config["FIntDebugForceMSAASamples"]
            else:
                config["FIntDebugForceMSAASamples"] = str(msaa_value)
            
            shadows_enabled = "FIntRenderShadowIntensity" not in config or config["FIntRenderShadowIntensity"] != "0"
            if not shadows_enabled:
                config["FIntRenderShadowIntensity"] = "0"
            
            postfx_enabled = "FFlagDisablePostFx" not in config or config["FFlagDisablePostFx"] != "True"
            if not postfx_enabled:
                config["FFlagDisablePostFx"] = "True"
            
            terrain_enabled = "FIntTerrainArraySliceSize" not in config or config["FIntTerrainArraySliceSize"] != "0"
            if not terrain_enabled:
                config["FIntTerrainArraySliceSize"] = "0"
            
            fps_value = self.fps_spin.value()
            if fps_value == 0:
                if "DFIntTaskSchedulerTargetFps" in config:
                    del config["DFIntTaskSchedulerTargetFps"]
            else:
                config["DFIntTaskSchedulerTargetFps"] = str(fps_value)
            
            render_mode = self.render_combo.currentData()
            if render_mode == "default":
                if "FFlagDebugGraphicsPreferD3D11" in config:
                    del config["FFlagDebugGraphicsPreferD3D11"]
                if "FFlagDebugGraphicsPreferD3D11FL10" in config:
                    del config["FFlagDebugGraphicsPreferD3D11FL10"]
            elif render_mode == "dx11":
                config["FFlagDebugGraphicsPreferD3D11"] = "True"
                if "FFlagDebugGraphicsPreferD3D11FL10" in config:
                    del config["FFlagDebugGraphicsPreferD3D11FL10"]
            elif render_mode == "dx10":
                if "FFlagDebugGraphicsPreferD3D11" in config:
                    del config["FFlagDebugGraphicsPreferD3D11"]
                config["FFlagDebugGraphicsPreferD3D11FL10"] = "True"
            
            texture_value = self.texture_combo.currentData()
            if texture_value == 0:
                if texture_value == 0 and "DFIntTextureQualityOverride" not in config:
                    config["DFIntTextureQualityOverride"] = "0"
                    config["DFFlagTextureQualityOverrideEnabled"] = "True"
                else:
                    config["DFIntTextureQualityOverride"] = str(texture_value)
                    config["DFFlagTextureQualityOverrideEnabled"] = "True"
            else:
                config["DFIntTextureQualityOverride"] = str(texture_value)
                config["DFFlagTextureQualityOverrideEnabled"] = "True"
            
            dpi_disabled = "DFFlagDisableDPIScale" in config and config["DFFlagDisableDPIScale"] == "True"
            if not dpi_disabled:
                config["DFFlagDisableDPIScale"] = "True"
            else:
                if "DFFlagDisableDPIScale" in config:
                    del config["DFFlagDisableDPIScale"]
            
            self.ui_ud = True
            self.editor.setText(json.dumps(config, indent=2))
            self.ui_ud = False
            self.status_label.setText("Settings updated")
            
        except json.JSONDecodeError:
            pass
    
    def ed_td(self):
        if self.ui_ud:
            return
            
        try:
            config = json.loads(self.editor.toPlainText())
            self.ui_ud = True
            
            if "FIntDebugForceMSAASamples" in config:
                msaa_value = int(config["FIntDebugForceMSAASamples"])
                index = self.msaa_combo.findData(msaa_value)
                if index != -1:
                    self.msaa_combo.setCurrentIndex(index)
                else:
                    self.msaa_combo.setCurrentIndex(0)
            else:
                self.msaa_combo.setCurrentIndex(0)
            
            shadows_enabled = "FIntRenderShadowIntensity" not in config or config["FIntRenderShadowIntensity"] != "0"
            self.shadows_check.setChecked(shadows_enabled)
            self.ud_cb_tx(self.shadows_check, Qt.Checked if shadows_enabled else Qt.Unchecked)
            
            postfx_enabled = "FFlagDisablePostFx" not in config or config["FFlagDisablePostFx"] != "True"
            self.postfx_check.setChecked(postfx_enabled)
            self.ud_cb_tx(self.postfx_check, Qt.Checked if postfx_enabled else Qt.Unchecked)
            
            terrain_enabled = "FIntTerrainArraySliceSize" not in config or config["FIntTerrainArraySliceSize"] != "0"
            self.terrain_check.setChecked(terrain_enabled)
            self.ud_cb_tx(self.terrain_check, Qt.Checked if terrain_enabled else Qt.Unchecked)
            
            if "DFIntTaskSchedulerTargetFps" in config:
                self.fps_spin.setValue(int(config["DFIntTaskSchedulerTargetFps"]))
            else:
                self.fps_spin.setValue(0)
            
            if "FFlagDebugGraphicsPreferD3D11" in config and config["FFlagDebugGraphicsPreferD3D11"] == "True":
                self.render_combo.setCurrentIndex(self.render_combo.findData("dx11"))
            elif "FFlagDebugGraphicsPreferD3D11FL10" in config and config["FFlagDebugGraphicsPreferD3D11FL10"] == "True":
                self.render_combo.setCurrentIndex(self.render_combo.findData("dx10"))
            else:
                self.render_combo.setCurrentIndex(self.render_combo.findData("default"))
            
            if "DFFlagTextureQualityOverrideEnabled" in config and config["DFFlagTextureQualityOverrideEnabled"] == "True" and "DFIntTextureQualityOverride" in config:
                texture_value = int(config["DFIntTextureQualityOverride"])
                index = self.texture_combo.findData(texture_value)
                if index != -1:
                    self.texture_combo.setCurrentIndex(index)
                else:
                    self.texture_combo.setCurrentIndex(0)
            else:
                self.texture_combo.setCurrentIndex(0)
            
            dpi_disabled = "DFFlagDisableDPIScale" in config and config["DFFlagDisableDPIScale"] == "True"
            self.dpi_check.setChecked(dpi_disabled)
            self.ud_cb_tx(self.dpi_check, Qt.Checked if dpi_disabled else Qt.Unchecked)
            
            self.ui_ud = False
            
        except (json.JSONDecodeError, ValueError):
            self.ui_ud = False
    
    def ud_cb_tx(self, checkbox, state):
        if checkbox == self.dpi_check:
            checkbox.setText("Disabled" if state == Qt.Checked else "Enabled")
        else:
            checkbox.setText("Enabled" if state == Qt.Checked else "Disabled")
    
    def dt_rb(self):
        self.status_label.setText("Detecting Roblox installation...")
        
        username = os.getenv("USERNAME") or os.getenv("USER")
        base_path = f"C:\\Users\\{username}\\AppData\\Local\\Roblox\\Versions"
        
        if not os.path.exists(base_path):
            self.status_label.setText("Roblox installation not found at expected location")
            return
        
        versions = []
        for item in os.listdir(base_path):
            item_path = os.path.join(base_path, item)
            if os.path.isdir(item_path) and item.startswith("version-"):
                versions.append(item_path)
        
        if not versions:
            self.status_label.setText("No Roblox versions found")
            return
        
        latest_version = max(versions, key=os.path.getmtime)
        self.rs_path = latest_version
        
        self.status_label.setText(f"Found Roblox at: {latest_version}")
        
        client_settings_path = os.path.join(latest_version, "ClientSettings", "ClientAppSettings.json")
        if os.path.exists(client_settings_path):
            try:
                with open(client_settings_path, "r") as f:
                    config = json.load(f)
                    self.ui_ud = True
                    self.editor.setText(json.dumps(config, indent=2))
                    self.ui_ud = False
                    self.ed_td()
                    self.status_label.setText(f"Loaded existing configuration from {latest_version}")
            except:
                pass
    
    def ld_df_cf(self):
        optimized_config = {
            "FLogNetwork": "7",
            "FFlagHandleAltEnterFullscreenManually": "False",
            "FIntDebugForceMSAASamples": "0",
            "DFIntTaskSchedulerTargetFps": "9999",
            "FFlagDebugGraphicsPreferD3D11": "True",
            "DFFlagTextureQualityOverrideEnabled": "True",
            "DFIntTextureQualityOverride": "0",
            "FIntFullscreenTitleBarTriggerDelayMillis": "3600000",
            "FFlagGameBasicSettingsFramerateCap5": "False",
            "FFlagTaskSchedulerLimitTargetFpsTo2402": "False",
            "FFlagDebugDisplayFPS": "False",
            "FFlagDebugSkyGray": "True",
            "FFlagFixGraphicsQuality": "True",
            "FFlagVoiceBetaBadge": "False",
            "FFlagCoreGuiTypeSelfViewPresent": "False",
            "FFlagChatTranslationSettingEnabled3": "False",
            "FFlagDebugLightGridShowChunks": "False",
            "FIntRenderShadowmapBias": "0",
            "FIntFontSizePadding": "1",
            "FFlagAdServiceEnabled": "False",
            "DFFlagDebugRenderForceTechnologyVoxel": "True",
            "FStringTerrainMaterialTable2022": "",
            "FStringTerrainMaterialTablePre2022": "",
            "FStringPartTexturePackTable2022": "",
            "FFlagDebugRenderEnableUgcTintMask": "False",
            "FFlagDontRenderBillboardGuisThatAreOffscreen": "True",
            "FIntMsecBetweenTextureMemoryUsageArrayRefresh": "512",
            "FIntDebugTextRenderingMaxDistance": "0",
            "FFlagGlobalWindRendering": "False",
            "FFlagGlobalWindActivated": "False",
            "FFlagDebugRenderingSetDeterministic": "False",
            "DFIntDebugFRMQualityLevelOverride": "0",
            "FIntRenderLocalLightUpdatesMax": "1",
            "FIntRenderLocalLightUpdatesMin": "1",
            "FIntRenderLocalLightFadeInMs": "1",
            "DFFlagDisableDPIScale": "False",
            "DFFlagVoxelizerDisableTerrainSIMD": "True",
            "DFIntDebugRestrictGCDistance": "1",
            "FIntTerrainOTAMaxTextureSize": "4",
            "FIntUITextureMaxRenderTextureSize": "1024",
            "FIntMeshContentProviderForceCacheSize": "268435456",
            "FIntDefaultMeshCacheSizeMB": "256",
            "FIntRakNetDatagramMessageIdArrayLength": "1024",
            "FIntRakNetResendBufferArrayLength": "1024",
            "DFIntRakNetMtuValue1InBytes": "1280",
            "DFIntRakNetMtuValue2InBytes": "1240",
            "DFIntRakNetMtuValue3InBytes": "1100",
            "DFIntRakNetNakResendDelayMs": "10",
            "DFIntRakNetNakResendDelayMsMax": "100",
            "DFIntRakNetNakResendDelayRttPercent": "50",
            "DFFlagRakNetUseSlidingWindow4": "True",
            "FFlagCommitToGraphicsQualityFix": "True",
            "DFIntHttpCurlConnectionCacheSize": "134217728",
            "FIntEmotesAnimationsPerPlayerCacheSize": "16777216",
            "DFIntUserIdPlayerNameCacheSize": "33554432",
            "DFIntUserIdPlayerNameLifetimeSeconds": "86400",
            "FFlagEnableQuickGameLaunch": "False",
            "FFlagDisableNewIGMinDUA": "True",
            "FFlagLuaAppExitModal2": "False",
            "FFlagLuaAppExitModalDoNotShow": "True",
            "FFlagPreloadAllFonts": "True",
            "FFlagPreloadTextureItemsOption4": "True",
            "FFlagBatchAssetApi": "True",
            "DFFlagBatchAssetApiNoFallbackOnFail": "False",
            "DFFlagQueueDataPingFromSendData": "True",
            "FFlagDontCreatePingJob": "True",
            "FFlagFastGPULightCulling3": "True",
            "FFlagGpuGeometryManager7": "True",
            "FFlagRenderGpuTextureCompressor": "True",
            "FIntFRMMinGrassDistance": "0",
            "FIntFRMMaxGrassDistance": "0",
            "FIntRenderGrassDetailStrands": "0",
            "FIntRenderGrassHeightScaler": "0",
            "DFIntCSGLevelOfDetailSwitchingDistance": "0",
            "DFIntCSGLevelOfDetailSwitchingDistanceL12": "0",
            "DFIntCSGLevelOfDetailSwitchingDistanceL23": "0",
            "DFIntCSGLevelOfDetailSwitchingDistanceL34": "0",
            "DFIntReportOutputDeviceInfoRateHundredthsPercentage": "0",
            "DFIntReportRecordingDeviceInfoRateHundredthsPercentage": "0",
            "DFFlagGpuVsCpuBoundTelemetry": "False",
            "DFFlagSimReportCPUInfo": "False",
            "DFFlagEnableFmodErrorsTelemetry": "False",
            "FIntBootstrapperTelemetryReportingHundredthsPercentage": "0",
            "DFIntGoogleAnalyticsLoadPlayerHundredth": "0",
            "FIntLmsClientRollout2": "0",
            "DFFlagEnableGCapsHardwareTelemetry": "False",
            "DFFlagAudioDeviceTelemetry": "False",
            "FFlagEnableSoundTelemetry": "False",
            "DFFlagEnableHardwareTelemetry": "False",
            "DFIntHardwareTelemetryHundredthsPercent": "0",
            "DFFlagDebugAnalyticsSendUserId": "False",
            "DFFlagEnableLightstepReporting2": "False",
            "DFIntLightstepHTTPTransportHundredthsPercent2": "0",
            "FFlagDebugDisableTelemetryEphemeralCounter": "True",
            "FFlagDebugDisableTelemetryEphemeralStat": "True",
            "FFlagDebugDisableTelemetryEventIngest": "True",
            "FFlagDebugDisableTelemetryPoint": "True",
            "FFlagDebugDisableTelemetryV2Counter": "True",
            "FFlagDebugDisableTelemetryV2Event": "True",
            "FFlagDebugDisableTelemetryV2Stat": "True",
            "FStringPerformanceSendMeasurementAPISubdomain": "opt-out",
            "DFStringHttpPointsReporterUrl": "http://opt-out.roblox.com",
            "DFStringAnalyticsEventStreamUrlEndpoint": "opt-out",
            "DFStringAltHttpPointsReporterUrl": "http://opt-out.roblox.com",
            "DFStringAltTelegrafHTTPTransportUrl": "http://opt-out.roblox.com",
            "DFStringTelegrafHTTPTransportUrl": "http://opt-out.roblox.com",
            "DFStringCrashUploadToBacktraceBaseUrl": "http://opt-out.roblox.com",
            "FStringErrorUploadToBacktraceBaseUrl": "http://opt-out.roblox.com",
            "DFStringRobloxAnalyticsSubDomain": "opt-out",
            "DFStringRobloxAnalyticsURL": "http://opt-out.roblox.com",
            "FIntRenderShadowIntensity": "0",
            "FIntTerrainArraySliceSize": "64",
            "FFlagDisablePostFx": "True",
            "FFlagRenderOptimizeDecalTransparencyInvalidation": "True",
            "FFlagQuaternionPoseCorrection": "True",
            "FFlagSelfieViewEnabled": "True",
            "FFlagDebugForceGenerateHSR": "True",
            "FFlagEnableChildrenLockFromLua": "False",
            "FFlagEnableAudioEmitterDistanceAttenuation": "True",
            "FFlagUseNotificationServiceIsConnected": "False",
            "FFlagToastNotificationsResendDisplayOnInit": "False",
            "FIntCAP1209DataSharingTOSVersion": "0",
            "FFlagFRMRefactor": "False",
            "FFlagMigrateTextureManagerIsLocalAsset": "True",
            "FFlagToastNotificationsUpdateEventParams": "False",
            "FFlagFixParticleEmissionBias2": "False",
            "FFlagFixCountOfUnreadNotificationError": "False",
            "FFlagEnablePreferredTextSizeStyleFixesInPlayerList": "True",
            "DFFlagVoiceChatTurnOnMuteUnmuteNotificationHack": "False",
            "FFlagLoginPageOptimizedPngs": "True",
            "FFlagToastNotificationsProtocolEnabled2": "False",
            "FFlagLuauCodegen": "True",
            "FFlagAvatarChatIncludeSelfViewOnTelemetry": "False",
            "FFlagRenderShadowSkipHugeCulling": "True",
            "FFlagFixSelfViewPopin": "False",
            "DFIntDebugLimitMinTextureResolutionWhenSkipMips": "0",
            "FFlagControlBetaBadgeWithGuac": "False",
            "DFFlagTeleportClientAssetPreloadingEnabledIXP": "True",
            "FFlagEnablePreferredTextSizeStyleFixesInPurchasePrompt": "True",
            "FFlagAdaptiveScrollingFrameOnServer": "True",
            "FIntStudioWebView2TelemetryHundredthsPercent": "0",
            "FFlagNotificationsNoLongerRequireControllerState": "False",
            "FFlagRenderEnableGlobalInstancingD3D11": "True",
            "FIntFriendRequestNotificationThrottle": "0",
            "FFlagEnablePreferredTextSizeStyleFixesInAppShell3": "True",
            "FFlagShaderLightingRefactor": "True",
            "FFlagDebugDeterministicParticles": "False",
            "DFIntGraphicsOptimizationModeMaxFrameTimeTargetMs": "20",
            "FFlagDebugSSAOForce": "False",
            "DFFlagEnableMeshPreloading2": "True",
            "FIntTextureCompositorLowResFactor": "4",
            "FFlagAXAdaptiveScrollingItemResetFix2": "True",
            "FFlagTopBarUseNewBadge": "False",
            "FFlagAXAdaptiveScrollingSnapItemEditor": "True",
            "DFIntMacWebViewTelemetryThrottleHundredthsPercent": "0",
            "FFlagEnablePreferredTextSizeScalePerLayerCollector": "True",
            "DFIntTimestepArbiterThresholdCFLThou": "300",
            "FFlagRenderLegacyShadowsQualityRefactor": "True",
            "DFFlagOpenCloudV1CreateUserNotificationAsync": "False",
            "DFFlagAudioToggleVolumetricPanning": "True",
            "FFlagAXPortraitSplitAdaptiveScrollingFix2": "True",
            "DFIntHttpParallelLimit_RequestExperienceNotificationService": "0",
            "FIntOcclusionCullingBetaFeatureRolloutPercent": "100",
            "DFFlagDebugPerfMode": "True",
            "FFlagPreOptimizeNoCollisionPrimitive": "True",
            "FIntRuntimeMaxNumOfThreads": "2400",
            "FIntStudioResendDisconnectNotificationInterval": "0",
            "FFlagPreferredTextSizeStyleFixEventDescriptionExperienceTile": "True",
            "DFIntMicroProfilerDpiScaleOverride": "100",
            "FFlagFixParticleAttachmentCulling": "False",
            "DFIntAnimationLodFacsVisibilityDenominator": "0",
            "FFlagDeveloperToastNotificationsEnabled": "False",
            "FIntEnableCullableScene2HundredthPercent3": "100",
            "FIntFixForBulkPresenceNotifications": "0",
            "FFlagSettingsHubIndependentBackgroundVisibility": "True",
            "FFlagSelfViewFixes": "False",
            "FFlagSquadToastNotificationsEnabled": "False",
            "FFlagEnableCullableScene2OptimizeStep": "True",
            "FFlagCAP1209EnableDataSharingUI4": "False",
            "FFlagNewOptimizeNoCollisionPrimitiveInMidphase637": "True",
            "DFFlagTeleportPreloadingMetrics5": "True",
            "FFlagChatTranslationEnableSystemMessage": "False",
            "DFFlagAdsPreloadInteractivityAssets": "True",
            "FFlagDontRerenderForBadTexture": "True",
            "FFlagEnablePreferredTextSizeSettingInMenus2": "True",
            "DFFlagUseVisBugChecks": "True",
            "FFlagDebugEnableVRFTUXExperienceInStudio": "True",
            "DFFlagJointIrregularityOptimization": "True",
            "FFlagRenderCBRefactor2": "True",
            "FFlagAXAdaptiveScrollingImprovementIXPEnabled": "True",
            "DFFlagOptimizeNoCollisionPrimitiveInMidphaseCrash": "True",
            "FIntRenderMaxShadowAtlasUsageBeforeDownscale": "1",
            "FIntSelfViewTooltipLifetime": "0",
            "FFlagOcclusionCullingBetaFeature": "True",
            "FFlagLuaAppsEnableParentalControlsTab": "False",
            "DFFlagOptimizeClusterCacheAlloc": "True",
            "DFFlagSimRefactorCollisionGeometry2": "True",
            "DFIntMaxFrameBufferSize": "4",
            "FFlagDisableFeedbackSoothsayerCheck": "False",
            "FFlagInExperienceUpsellSelfViewFix": "False",
            "DFIntGraphicsOptimizationModeMinFrameTimeTargetMs": "25",
            "FFlagAssetPreloadingIXP": "True",
            "FFlagWindowsReportAbuseNotification": "False",
            "FFlagPreloadMinimalFonts": "True",
            "FFlagSelfViewRemoveVPFWhenClosed": "False",
            "DFFlagOptimizeInstanceQueries": "True",
            "FFlagFixEmotesMenuVR": "True",
            "FFlagPreferredTextSizeSettingBetaFeature": "True",
            "FFlagEnablePreferredTextSizeGuiService": "True",
            "FFlagVRMouseMoveOptimization": "True",
            "FIntGrassMovementReducedMotionFactor": "0",
            "FFlagUserShowGuiHideToggles": "True",
            "FFlagEnableChildrenLockFromLua2": "False",
            "FFlagEnablePreferredTextSizeStyleFixesInAppShell4": "True",
            "FFlagLuaAppGamesPagePreloadingDisabled": "False",
            "FStringVoiceBetaBadgeLearnMoreLink": "null",
            "FFlagSignalRNotificationManagerMaybeStart": "False",
            "FFlagNotificationButtonTypeVariantMappingEmphasis": "False",
            "FFlagBetaBadgeLearnMoreLinkFormview": "False",
            "DFFlagSimSkipVoxelCDECMerge": "True",
            "FFlagEnableInGameMenuChromeABTest4": "True",
            "DFFlagUnifyLegacyJointGeometry": "True",
            "FFlagRenderFixFog": "True",
            "FFlagSelfViewAvoidErrorOnWrongFaceControlsParenting": "False",
            "FIntDebugFRMOptionalMSAALevelOverride": "0",
            "FIntVRTouchControllerTransparency": "0",
            "DFIntConnectionMTUSize": "1396",
            "DFFlagSimOptimizeSetSize": "True",
            "DFFlagEnableExperienceNotificationOptInPrompt": "False",
            "DFIntTeleportClientAssetPreloadingHundredthsPercentage2": "100000",
            "DFFlagAssetPreloadingUrlVersionEnabled2": "True",
            "FStringInExperienceNotificationsLayer": "",
            "FFlagDebugSelfViewPerfBenchmark": "False",
            "FFlagSimEnableDCD16": "True",
            "FIntUnifiedLightingBlendZone": "1",
            "DFIntNumAssetsMaxToPreload": "2147483647",
            "FFlagSelfViewCameraDefaultButtonInViewPort": "False",
            "FFlagRenderLightGridEfficientTextureAtlasUpdate": "True",
            "FFlagUserFixLoadAnimationError": "True",
            "FFlagVRLaserPointerOptimization": "True",
            "FFlagDebugStudioForceSystemDeprecationNotification": "False",
            "FFlagViewCollisionFadeToBlackInVR": "False",
            "FFlagDisableChromeV3StaticSelfView": "False",
            "FFlagUpdateHTTPCookieStorageFromWKWebView": "False",
            "FIntRobloxGuiBlurIntensity": "0",
            "FFlagFixChunkLightingUpdate2": "True",
            "FFlagEnablePreferredTextSizeStyleFixesAddFriends": "True",
            "FFlagEngineAPICloudProcessingUseNotificationClient": "False",
            "FFlagSelfViewHumanoidNilCheck": "False",
            "FFlagFixExitDialogBlockVRView": "True",
            "FFlagUserEnableCameraToggleNotification": "False",
            "FFlagRenderTestEnableDistanceCulling": "True",
            "FFlagEnableIOSWebViewCookieSyncFix": "False",
            "DFFlagDebugSkipMeshVoxelizer": "True",
            "FFlagEnableAudioPannerFiltering": "True",
            "FIntTargetRefreshRate": "144",
            "FFlagEnableVRFTUXExperienceV2": "True",
            "FFlagSortKeyOptimization": "True",
            "FFlagToastNotificationsReceivedAndDismissedSignals": "False",
            "FFlagVisBugChecksThreadYield": "True",
            "FFlagFixReducedMotionStuckIGM2": "True",
            "FIntCameraMaxZoomDistance": "999999"
        }
        
        default_config = {}
        
        self.ps["Optimized Performance"] = optimized_config
        self.ps["Default Settings"] = default_config
        self.editor.setText(json.dumps(optimized_config, indent=2))
    
    def ld_pt(self):
        preset_name = self.preset_combo.currentText()
        if preset_name in self.ps:
            config = self.ps[preset_name]
            self.ui_ud = True
            self.editor.setText(json.dumps(config, indent=2))
            self.ui_ud = False
            self.ed_td()
            self.status_label.setText(f"Loaded preset: {preset_name}")
        else:
            QMessageBox.warning(self, "Error", f"Preset '{preset_name}' not found")
    
    def sv_pt(self):
        try:
            config = json.loads(self.editor.toPlainText())
            preset_name = self.preset_combo.currentText()
            self.ps[preset_name] = config
            self.status_label.setText(f"Saved current settings as '{preset_name}' preset")
            QMessageBox.information(self, "Success", f"Saved current settings as '{preset_name}' preset")
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "Error", f"Invalid JSON format: {str(e)}")
    
    def ap_ff(self):
        if not self.rs_path:
            QMessageBox.warning(self, "Error", "Roblox installation not detected")
            return
            
        try:
            config = json.loads(self.editor.toPlainText())
            
            client_settings_dir = os.path.join(self.rs_path, "ClientSettings")
            if not os.path.exists(client_settings_dir):
                os.makedirs(client_settings_dir)
                
            config_path = os.path.join(client_settings_dir, "ClientAppSettings.json")
            
            with open(config_path, "w") as f:
                json.dump(config, f, indent=2)
                
            self.status_label.setText(f"FFlags applied successfully to: {self.rs_path}")
            QMessageBox.information(self, "Success", "FFlags applied successfully")
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "Error", f"Invalid JSON format: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to apply FFlags: {str(e)}")
    
    def cr_bk(self):
        if not self.rs_path:
            QMessageBox.warning(self, "Error", "Roblox installation not detected")
            return
            
        config_path = os.path.join(self.rs_path, "ClientSettings", "ClientAppSettings.json")
        if not os.path.exists(config_path):
            QMessageBox.warning(self, "Error", "No configuration file to backup")
            return
            
        backup_path = os.path.join(self.rs_path, "ClientSettings", "ClientAppSettings.backup.json")
        
        try:
            with open(config_path, "r") as src:
                content = src.read()
                
            with open(backup_path, "w") as dst:
                dst.write(content)
                
            self.status_label.setText(f"Backup created at: {backup_path}")
            QMessageBox.information(self, "Success", f"Backup created at {backup_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create backup: {str(e)}")
    
    def rs_bk(self):
        if not self.rs_path:
            QMessageBox.warning(self, "Error", "Roblox installation not detected")
            return
            
        backup_path = os.path.join(self.rs_path, "ClientSettings", "ClientAppSettings.backup.json")
        if not os.path.exists(backup_path):
            QMessageBox.warning(self, "Error", "No backup file found")
            return
            
        config_path = os.path.join(self.rs_path, "ClientSettings", "ClientAppSettings.json")
        
        try:
            with open(backup_path, "r") as src:
                content = src.read()
                
            with open(config_path, "w") as dst:
                dst.write(content)
                
            self.status_label.setText("Backup restored successfully")
            QMessageBox.information(self, "Success", "Backup restored successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to restore backup: {str(e)}")
    
    def ft_fg(self):
        search_text = self.search_input.text().lower()
        if not search_text:
            try:
                config = json.loads(self.editor.toPlainText())
                self.editor.setText(json.dumps(config, indent=2))
                self.status_label.setText("Filter cleared")
            except:
                pass
            return
            
        try:
            config = json.loads(self.editor.toPlainText())
            filtered_config = {}
            
            for key, value in config.items():
                if search_text in key.lower():
                    filtered_config[key] = value
                    
            if filtered_config:
                self.editor.setText(json.dumps(filtered_config, indent=2))
                self.status_label.setText(f"Filtered: {len(filtered_config)} matching flags found")
            else:
                self.status_label.setText("No matching flags found")
                QMessageBox.information(self, "Filter", "No matching flags found")
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Error", "Invalid JSON format") 