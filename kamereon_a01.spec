# -*- mode: python -*-

from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['kamereon_a01.py'],
             pathex=['C:\\Kamereon'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='kamereon_a01',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='srcs\\kamereon_icon.ico')
coll = COLLECT(exe,Tree('_srcs'),
	       Tree('props'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='kamereon_a01')
