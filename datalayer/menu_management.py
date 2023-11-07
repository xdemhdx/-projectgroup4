import json
class Test:
    @classmethod
    def import_file(cls,filepath):
        try:
            with open(filepath,"r") as file_pointer:
                data = json.load(file_pointer)
                return [True,data]
        except FileNotFoundError:
            print(f"The file {filepath} not found")
            return [False]
        except json.JSONDecodeError:
            print(f"The file {filepath} contains not valid JSON Structure")
            return False
        
                     
                  

