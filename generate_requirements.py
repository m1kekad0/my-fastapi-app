import os

import toml


def generate_requirements():
    pyproject_path = "pyproject.toml"
    requirements_path = "requirements.txt"

    if not os.path.exists(pyproject_path):
        print(f"Error: {pyproject_path} not found.")
        return

    with open(pyproject_path) as f:
        data = toml.load(f)

    # project.dependencies を取得 (uv / PEP 621 形式)
    dependencies = data.get("project", {}).get("dependencies", [])

    with open(requirements_path, "w") as f:
        for dep in dependencies:
            # dep は "fastapi>=0.115.0" のような文字列
            f.write(f"{dep}\n")

    print(f"Successfully generated {requirements_path}")


if __name__ == "__main__":
    generate_requirements()
