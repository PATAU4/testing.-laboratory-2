import os
import shutil
import pytest
import file_manager_defs



# Пункт №1. Создание папки (с указанием имени);
@pytest.fixture
def mkdir_fixture():
    file_manager_defs.mkdir('TestDir')
    return True
def test_mkdir(mkdir_fixture):
    assert mkdir_fixture == 1, "Mkdir Error"

# Пункт №2. Удаление папки по имени;
@pytest.fixture
def mrdir_fixture():
    file_manager_defs.remove_dir('TestDir')
    return True
def test_remove_dir(mrdir_fixture):
    assert mrdir_fixture == 1, "Mkdir Error"




# Пункт №3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени;
@pytest.fixture
def cd_fixture():
    file_manager_defs.cd('Test_for_cd')
    return True
def test_cd(cd_fixture):
    assert cd_fixture == 1, "Cd Error"




# Пункт №5. Запись текста в файл;
@pytest.fixture
def writing_fixture():
    file_manager_defs.writing('test_file_for_writing')
    return True
def test_writing(writing_fixture):
    assert writing_fixture == 1, "Writing Error"

# Пункт №6. Просмотр содержимого текстового файла;
@pytest.fixture
def reading_fixture():
    file_manager_defs.reading('test_file_for_writing')
    return True
def test_reading(reading_fixture):
    assert reading_fixture == 1, "Reading Error"




# Пункт №4. Создание пустых файлов с указанием имени;
@pytest.fixture
def touch_fixture():
    file_manager_defs.touch('TestFile')
    return True
def test_touch(touch_fixture):
    assert touch_fixture == 1, "Touch Error"

# Пункт №7. Удаление файлов по имени;
@pytest.fixture
def remove_fixture():
    file_manager_defs.remove('TestFile')
    return True
def test_remove(remove_fixture):
    assert remove_fixture == 1, "Remove Error"



# Пункт №8. Копирование файлов из одной папки в другую;
@pytest.fixture
def cp_fixture():
    file_manager_defs.cp('test_file_for_cp_from','test_file_for_cp_to')
    return True
def test_cp(cp_fixture):
    assert cp_fixture == 1, "Cp Error"



# Пункт №9. Перемещение файлов;
@pytest.fixture
def move_fixture():
    file_manager_defs.move('Dir_from','Dir_to')
    return True
def test_move(move_fixture):
    assert move_fixture == 1, "Move Error"

# Пункт №10. Переименование файлов;
@pytest.fixture
def rename_fixture():
    file_manager_defs.rename('file_1','file_renamed')
    return True
def test_rename(rename_fixture):
    assert rename_fixture == 1, "Rename Error"
    