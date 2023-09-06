# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/FSR_GUI/Flower_Status.py','C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/my_dataset.py','C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/FSR_GUI/main.py','C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/FSR_GUI/kid.py','C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/densenet/model.py','C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/densenet/utils.py','C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/densenet/predict.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Flower_Status',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
