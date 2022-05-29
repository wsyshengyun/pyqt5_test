# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:\\_python\\xdkj_test\\project\\ipOnline\\main_check_ip_online.py'],
             pathex=['D:\\_python\\xdkj_test'],
             binaries=[],
             datas=[
                ('D:\\_python\\xdkj_test\\project\\ipOnline\\pack\\app.ini','.\\project\\ipOnline\\pack'),
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
             
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='SearchIP',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
          
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='SearchIP')
