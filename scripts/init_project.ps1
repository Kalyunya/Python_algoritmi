# ===== базова папка для Python-проєктів =====
$BaseProjectsPath = "C:\Users\kolya\Desktop\Neo\Python_algoritmi\projects"

# ===== запит назви проєкту =====
$ProjectName = Read-Host "Enter project name"

if ([string]::IsNullOrWhiteSpace($ProjectName)) {
    Write-Host "❌ Project name cannot be empty"
    exit 1
}

$ProjectPath = Join-Path $BaseProjectsPath $ProjectName

if (Test-Path $ProjectPath) {
    Write-Host "❌ Project '$ProjectName' already exists"
    exit 1
}

# ===== створення структури =====
New-Item -ItemType Directory -Path "$ProjectPath\.vscode" -Force | Out-Null
Set-Location $ProjectPath

# ===== створення virtual environment =====
py -m venv env

# ===== requirements.txt =====
New-Item -ItemType File -Name "requirements.txt" -Force | Out-Null

# ===== .gitignore =====
@'
# Virtual environment
env/

# Python cache
__pycache__/
*.pyc

# VS Code
.vscode/

# Tests / tools
.pytest_cache/
'@ | Set-Content ".gitignore" -Encoding UTF8

# ===== VS Code auto-env =====
@'
{
  "python.defaultInterpreterPath": ".\\env\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true
}
'@ | Set-Content ".vscode\settings.json" -Encoding UTF8

# ===== базовий файл =====
@"
print("Project $ProjectName is ready")
"@ | Set-Content "main.py" -Encoding UTF8

Write-Host "✅ Project '$ProjectName' created in $ProjectPath"
Write-Host "👉 Open folder: $ProjectPath"