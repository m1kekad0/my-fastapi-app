import toml
import os

def generate_requirements():
    pyproject_path = "pyproject.toml"
    requirements_path = "requirements.txt"

    if not os.path.exists(pyproject_path):
        print(f"Error: {pyproject_path} not found.")
        return

    with open(pyproject_path, "r") as f:
        data = toml.load(f)

    # project.dependencies を取得
    dependencies = data.get("project", {}).get("dependencies", [])
    
    with open(requirements_path, "w") as f:
        for dep in dependencies:
            # Vercelでのトラブルを避けるため、必要なものだけを書き出す
            f.write(f"{dep}\n")
        # uvicornはVercel環境では不要ですが、ローカル起動でも使う場合は含めてもOK
        # 今回はエラー回避のため最小限にします

    print(f"Successfully generated {requirements_path}")

if __name__ == "__main__":
    generate_requirements()
