import os

# Base project name (optional – remove if you want files directly in PWD)
BASE_DIR = os.getcwd()

structure = {
    "backend": {
        "__init__.py": "",
        "config.py": "",
        "extensions.py": "",
        "models": {
            "user_model.py": "",
            "product_model.py": "",
            "cart_model.py": "",
            "order_model.py": "",
        },
        "routes": {
            "auth_routes.py": "",
            "product_routes.py": "",
            "cart_routes.py": "",
            "order_routes.py": "",
            "admin_routes.py": "",
        },
        "services": {
            "auth_service.py": "",
            "product_service.py": "",
            "cart_service.py": "",
            "order_service.py": "",
        },
        "utils": {
            "jwt_utils.py": "",
            "response.py": "",
        },
    },
    "run.py": "",
    "requirements.txt": "",
}


def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)


if __name__ == "__main__":
    create_structure(BASE_DIR, structure)
    print("Project structure created successfully in:", BASE_DIR)