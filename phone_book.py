import sys 
def print_result(x):
    for line in x:
        print(line)

def find_by_lastname(phone_book,last_name):
    for line in phone_book:
        if line.get('Фамилия')==last_name:
            print(line)

def find_by_number(phone_book,phone_number):
    for line in phone_book:
        if line.get('Телефон')==phone_number:
            print(line)

def write_new_abonent(phone_book,last_name,name,phone_number,discription):
    with open('phon.txt', 'a', encoding='utf-8') as data:
        data.write('\n')
        data.write(last_name)
        data.write(', ')
        data.write(name)
        data.write(', ')
        data.write(phone_number)
        data.write(', ')
        data.write(discription)
    print(print_result(phone_book))

def save_new_file(phone_book,new_file_name):
    
    with open(new_file_name, 'a', encoding='utf-8') as data: 
        data.write('Фамилия Имя Телефон Описание')
        for line in phone_book: 
            data.write(line)
                 
def copy_line_to_new_file(line,destination_file_name):
    open(destination_file_name, 'a', encoding='utf-8').write(str(line))

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    phone_base='phon.txt'
    while (choice<8):
        if choice==1:
            print(print_result(phone_book))
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            phone_number=input('phone number ')
            print(find_by_number(phone_book,phone_number))
        elif choice==4:
            lastname=input('lastname ')
            name=input('name ')
            phone=input('phone_number ')
            discription=input('discription ')
            write_new_abonent(phone_book,lastname,name,phone,discription)
        elif choice==5:
            new_file_name=input('New file name: ')
            old=open(phone_base, 'r', encoding='utf-8')
            save_new_file(old,new_file_name)
        elif choice==6:
            print('line number: ')
            line_number=int(input())
            with open(phone_base,'r',encoding='utf-8') as phb:
                for i in range(line_number):
                    line = phb.readline()
            destination_file_name=input('destination file name: ')
            copy_line_to_new_file(line,destination_file_name)
        elif choice==7:
            sys.exit(1)
    choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Перенести строчку в другой файл\n"
          "7. Закончить работу")
    choice = int(input())
    
    return choice

def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

           record = dict(zip(fields, line.split(',')))

			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
	     
           phone_book.append(record)
    return phone_book

work_with_phonebook()



