def paths_appender(root, path=[], paths=[]):
    if not root:
        return 0
    path.append(root.data)
    paths.append(path)
    if root.left:
        paths_appender(root.left, path+[root.data], paths)
    if root.right:
        paths_appender(root.right, path+[root.data], paths)

def paths_finder(root):
    paths = []
    paths_appender(root, [], paths)
    print('paths', paths)