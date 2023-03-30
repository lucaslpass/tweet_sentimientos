class path:
    def __init__(self,path=None,folder=None,name=None) :
        self.folder = folder
        self.name   = name
    
    def set_name(self,name):
        self.name = name
    
    def set_folder(self,folder):
         self.folder = folder   
    
    def get_path(self):
        return self.get_folder()+self.get_name()+".csv"
    
    def get_name(self):
        return self.name
    
    def get_folder(self):
        return self.folder
    