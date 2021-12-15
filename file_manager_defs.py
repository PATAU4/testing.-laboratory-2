import os
import shutil
import platform


main_path = '/users/aleksandrtulakov/documents'




def touch(n): # создает пустой файл
    open(main_path + '/' + n,'a').close()
    print(f'Готово!\nФайл {n} был создан')     

def remove(n): # удаляет файл
    os.remove(main_path + '/' +n)
    print(f'Готово!\nФайл {n} был удален')




def mkdir(n): # создает директорию
    os.mkdir(main_path + '/' + n)
    print(f'Готово!\nРепозиторий {n} был создан')     

def remove_dir(n): # удаляет директорию если пустая, если в директории есть файлы, то сначала удаляются файлы в ней, а потом она сама
    os.rmdir(main_path + '/' + n)
    print(f'Готово!\nРепозиторий {n} был удален')




def cd(n): # осуществляет перемещение между папками
    global main_path, tmp
    check_file_2 = os.path.exists(main_path + '/' + n) 
    if check_file_2 is True:
        tmp = main_path
        tmp = main_path + '/' + n #новый путь 
        print(f'Вы перешли в директорию {tmp}')




def rename(n, ger): # переименовывет файл/директорию
    os.rename(main_path+'/'+n, ger)
    print(f'Готово!\nНазвание было переименовано с {n} на {ger}')

def move(n, ger): # перемещает файл/директорию 
    shutil.move(main_path+'/'+n, main_path+'/'+ger)
    print(f'Готово!\nФайл {n} был перемещен в {ger}')

def cp(n, ger): # копирует файл
    shutil.copy(main_path+'/'+n, main_path+'/'+ger)
    print(f'Готово!\nСодержание файла {n} было копировано в файл {ger}')



def writing(n): # записыввает в файл
    f = open(main_path + '/'+ n, 'w')
    f.write('test message')
    f.close()
    print(f'Готово!\nФайл был перезаписан')

def reading(n): # читает содержимое файла
    f = open(main_path + '/' +n)
    for line in f:
        print(line)




