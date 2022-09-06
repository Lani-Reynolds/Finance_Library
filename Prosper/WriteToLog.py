def Write_To_Log(FileHandle, Data):
    with open(FileHandle, "w+") as DataFile:
        DataFile.write(Data)

    return FileHandle, Data