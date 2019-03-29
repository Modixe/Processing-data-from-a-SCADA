from cx_Freeze import setup, Executable

executable = Executable(script="temp.py", targetName="OpcHda_to_sql_data_transfer.exe")

includes = ['win32com.client', 'win32timezone']

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
        'include_files': ['C:/Users/Администратор/Desktop/OleDbTest/DataAccessLayer',
                          'C:/Users/Администратор/Desktop/OleDbTest/Models',
                          'C:/Users/Администратор/Desktop/OleDbTest/Main/test.json',
                          'C:/Users/Администратор/AppData/Local/Programs/Python/Python37-32/python37.dll',
                          'C:/Users/Администратор/AppData/Local/Programs/Python/Python37-32/vcruntime140.dll'],
        'build_exe': 'build_windows',
    }
}

setup(
    name = "OpcHda_to_sql_data_transfer",
    version = "1.1",
    description = "test",
    options = options,
    executables = [executable]
)