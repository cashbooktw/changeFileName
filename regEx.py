import os, re, sys
def t():
    print("I'm t")
def splitFileName(userInputVideoName, seasonNum, fileNameString):
    #get fileName and fileType
    fileNamePattern = r'(.+)(\..+)'
    fileName = re.search(fileNamePattern, fileNameString)
    if fileName is None:
        return None
    fileNameString = fileName.group(1)
    fileType = fileName.group(2)

    #get episode
    episodePattern = r'(\d+)(?!.*\d)'
    episode = re.search(episodePattern, fileNameString)
    if episode is None:
        return None
    episodeNum = episode.group(1)

    #concat season and episode
    seasonS = 'S0' + str(seasonNum) if (int(seasonNum) < 10) else 'S' + str(seasonNum)
    episodeNum = episodeNum.lstrip('0')
    episodeE = 'E0' + str(episodeNum) if (int(episodeNum) < 10) else 'E' + str(episodeNum)
    SXXEXX = seasonS + episodeE
    print(SXXEXX)
    #replace with SXXEXX
    #newFileNameString = re.sub(episodePattern, SXXEXX, fileNameString)

    #concat fileType
    #newFileNameString = newFileNameString + fileType
    newFileNameString = userInputVideoName + ' ' + SXXEXX + fileType
    print(newFileNameString)
    return newFileNameString