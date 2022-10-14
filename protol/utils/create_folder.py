import attrs
import os


@attrs.define
class CreateFolder:
    project_name: str = attrs.field()

    def create_folder(self):
        try:
            os.mkdir(self.project_name)
            os.chdir(self.project_name)
            with open("__init__.py", "w") as f:
                f.write("")
        except FileExistsError:
            print("Folder already exists")
        else:
            print("Folder created")

    def create_folder_structure(self) -> list:
        self.create_folder()
        os.chdir("..")
        os.chdir(self.project_name)
        folders = ["api", f"{self.project_name}_core"]
        for folder in folders:
            os.mkdir(folder)
        print("Folder structure created")

        return folders

    def create_files(self) -> None:
        folders = self.create_folder_structure()
        for folder in folders:
            os.chdir(folder)
            with open("__init__.py", "w") as f:
                f.write("")
            os.chdir("..")

    def create_folder_in_api(self) -> bool:
        folders = ['facades', 'router', 'schemas', 'scripts']
        files = ['__init__.py', 'app.py', 'config.py', 'db.py', 'exceptions.py']
        self.create_files()
        try:
            os.chdir('api')
            for file in files:
                with open(file, "w") as f:
                    f.write("")
            for folder in folders:
                os.mkdir(folder)
                os.chdir(folder)
                with open("__init__.py", "w") as f:
                    f.write("")
                os.chdir("..")

            os.chdir("...")
        except Exception as e:
            raise e

        return True


if __name__ == '__main__':
    t = CreateFolder('test')
    print(t.create_folder_in_api())
