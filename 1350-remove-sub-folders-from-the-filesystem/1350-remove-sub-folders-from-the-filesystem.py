class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        directory=set(folder)
        result=[]
        for x in folder:
            result.append(x)
            for i in range(len(x)):
                if x[i]=='/' and x[:i] in directory:
                    result.pop()
                    break
        return result

        