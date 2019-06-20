rem dim currentpath = createobject("Scripting.FileSystemObject").GetFolder(".").Path
rem msgbox "current path: ", currentpath


set fs = createObject("scripting.fileSystemObject")

rem create folder and file

if (not fs.folderExists("test_fileOperations")) then
	fs.createFolder("test_fileOperations")
end if
if (not fs.fileExists("test_fileOperations/testFile.txt")) then
	fs.createTextFile("test_fileOperations/testFile.txt")
end if

msgbox("create finished")

rem write file

set file = fs.openTextFile("test_fileOperations/testFile.txt", 2, true)
file.writeLine("this is the first line")
file.writeLine("this is the second line")
file.writeBlankLines("5")
file.writeLine("there are 5 blank lines above")

file.close()
msgbox("write finished")


rem read file

set file = fs.openTextFile("test_fileOperations/testFile.txt", 1, false)
msgbox(file.readAll())
msgbox "Column: ", file.column
msgbox "Line: ", file.line

file.close()
msgbox("read finished")

rem move file