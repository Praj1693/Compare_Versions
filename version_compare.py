class VersionCompare:
    def compareVersions(self, version1, version2):
        if version1 !="" and version2 != "":
            ver1 = [(v) for v in version1.split(".")]
            ver2 = [(v) for v in version2.split(".")]
            ver1_len = len(ver1)
            ver2_len = len(ver2)
            for i in range(max(ver1_len,ver2_len)):
                if  ver1_len > i :
                    v1 = ver1[i]
                else : 0 
                if ver2_len > i:
                    v2 = ver2[i]
                else : 0

                if v1 > v2:
                    print('Version 1 is greater than Version 2')
                    return 1
                elif v1 < v2:
                    print('Version 1 is less than Version 2')
                    return -1
            print('Version 1 is equal to Version 2')
            return 0
        else:
            print('Invalid inputs of Version 1 and Version 2')
            return -2

compareCheck = VersionCompare()
result = compareCheck.compareVersions("1.1.1.2","1.1.1.2")
print('Result: ', result)