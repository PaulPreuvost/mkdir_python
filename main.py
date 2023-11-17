import os
import platform

def clearTerminal() -> None:
    system: str = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def verification(user_verification: str) -> bool:
    if user_verification.lower() == "y":
        return True
    else:
        return False

def userVerification(to_verify: str) -> str:
    print(f"Is '{to_verify}' correct ? (y/n) ")
    user_verification: str = input()
    return user_verification

def askUserPath() -> str:
    clearTerminal()
    print("Where do you want to create your folder ? (Copy your path) ")
    origin_path: str = input()
    if not verification(userVerification(origin_path)):
        askUserPath()
    else:
        return origin_path

def askUserProjectName() -> str:
    clearTerminal()
    print("What name do you want to give to your project ?")
    project_name: str = input()
    if not verification(userVerification(project_name)):
        askUserProjectName()
    else:
        return project_name

def createProjectStructure(user_path: str, project_name: str) -> None:
    user_folder_path: str = os.path.join(user_path, project_name)

    if not os.path.exists(user_folder_path):
        os.makedirs(user_folder_path)

        sub_folders: List[str] = ['script', 'style', 'src']
        for sub_folder in sub_folders:
            sub_folder_path: str = os.path.join(user_folder_path, sub_folder)
            os.makedirs(sub_folder_path)

            if sub_folder == 'src':
                sub_sub_folders: List[str] = ['images', 'font']
                for sub_sub_folder in sub_sub_folders:
                    sub_sub_folder_path: str = os.path.join(sub_folder_path, sub_sub_folder)
                    os.makedirs(sub_sub_folder_path)

        print(f"The folder structure for the project '{project_name}' was created successfully.")
    else:
        print(f"The project folder '{project_name}' already exists.")

def main() -> None:
    user_path: str = askUserPath()
    project_name: str = askUserProjectName()
    createProjectStructure(user_path, project_name)

main()