class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        directories = path.split('/')
        for dir in directories:
            if dir == '.' or not dir :
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
            
