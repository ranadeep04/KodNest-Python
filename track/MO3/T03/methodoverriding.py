class Developer:
    def work(self):
        print("Developer is working")
    
    def attendMeeting(self):
        print("Developer is attending meeting")
    
class JavaDeveloper(Developer):
    def work(self):
        print("Java Developer is working on Java")
    
    def doJavaProject(self):
        print("Java Developer is working on Java Project")
    
class PythonDeveloper(Developer):
    def work(self):
        print("Python Developer is working on Python")
    
    def doPythonproject(self):
        print("Python Developer is working on python project")
    


jdev=JavaDeveloper()
jdev.work()
jdev.doJavaProject()

pdev=PythonDeveloper()
pdev.attendMeeting()
pdev.work()
pdev.doPythonproject()