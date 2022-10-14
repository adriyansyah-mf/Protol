from protol.utils.create_folder import CreateFolder
import sys



if __name__ == '__main__':
    try:
        if sys.argv[1] == 'h':
            print("Usage: protol [project_name]")
        else:
            project_name = sys.argv[1]
            create_folder = CreateFolder(project_name)
            create_folder.create_folder_in_api()
    except IndexError:
        print("Please provide a project name")