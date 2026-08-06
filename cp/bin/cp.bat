@echo off
if /I "%~1"=="run" (
    python "%~dp0..\python\run.py" "%~2"
) else (
    python "%~dp0..\judge\cfjudge.py" %*
)
