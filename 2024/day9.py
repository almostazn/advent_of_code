sample = '2333133121414131402'

def process_2(line):
    files = [int(n) for n in list(line)[::2]]
    spaces = [int(n) for n in list(line)[1::2]]
    spacesIdx = []
    filesIdx = []

    fileSystem = []
    for id, file in enumerate(files):
       filesIdx.append(len(fileSystem))
       for i in range(file):
           fileSystem.append(id)
        
       if id < len(spaces):
           spacesIdx.append(len(fileSystem))
           for i in range(spaces[id]):     
               fileSystem.append('.')


    for id in range(len(files)-1, 0, -1):
        file = files[id]
        for j, space in enumerate(spaces):
            if space < file:
                continue
            spaces[j] = space - file

            #write to filesystem
            spaceIdx = spacesIdx[j]
            fileIdx = filesIdx[id]
            for i in range(file):
                #print(fileSystem)
                fileSystem[spaceIdx + i] = id
                fileSystem[fileIdx + i] ='.'
                spacesIdx[j] += 1
            break
    
    print(fileSystem)
    
    sum = 0
    for i, file in enumerate(fileSystem):
        if file == '.':
            continue
        sum += (i * file)
    print(sum)

def process_1(line):
    files = [int(n) for n in list(line)[::2]]
    spaces = [int(n) for n in list(line)[1::2]]

    fileSystem = []
    for id, file in enumerate(files):
        for i in range(file):
            fileSystem.append(id)
        
        if id < len(spaces):
            for i in range(spaces[id]):
                fileSystem.append('.')

    freeSpaceIdx = 0
    for i in range(len(fileSystem)-1, -1, -1):
        file = fileSystem[i]
        if (freeSpaceIdx == len(fileSystem)):
            break
        if (file == '.'):
            continue

        if fileSystem[freeSpaceIdx] != '.':
            while True:
                freeSpaceIdx += 1
                if ( freeSpaceIdx == len(fileSystem) or fileSystem[freeSpaceIdx] == '.'):
                    break
        
        if freeSpaceIdx == len(fileSystem):
            break

        fileSystem[freeSpaceIdx] = file
        fileSystem[i] = '.'
        if i < freeSpaceIdx:
            freeSpaceIdx = i
    
    sum = 0
    for i, file in enumerate(fileSystem[1:]):
        if file == '.':
            continue
        sum += (i * file)
    print(sum)

def main():
    with open('./inputs/2024/day9.txt') as f:
        lines = [l.strip() for l in f.readlines()]
        process_2(lines[0])
        #process_2(sample)

if __name__ == '__main__':
    main()
