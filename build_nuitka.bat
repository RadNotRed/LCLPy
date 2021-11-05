@echo off
set Version="1.1.0.0"
python -m nuitka --onefile --follow-imports --include-plugin-files=modules\launch.py --include-plugin-files=modules\config.py main.py --output-dir="%TEMP%" -o "LCLPy.exe" --windows-icon-from-ico=icon.ico --windows-file-description="Lunar Client Lite Python" --windows-product-name="Lunar Client Lite Python" --windows-file-version=%Version% --windows-company-name=" "
timeout 5