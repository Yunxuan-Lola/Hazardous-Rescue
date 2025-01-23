# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gui.py','D:\\python_code\\tph-yolov5-main\\detect.py'],
    pathex=['D:\python_code\tph-yolov5-main'],
    binaries=[],
    datas=[],
    hiddenimports=['shutil', 'os', 'sys', 'time', 'cv2', 'torch', 'numpy',
    'yaml','tkinker','PIL','Flask','torch',
    'models.experimental','utils.datasets','utils.general','utils.plots','utils.torch_utils'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    onedir=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='gui',
)
