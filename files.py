'''
creating new files using classes program
'''

# know that a class is a blue print to create objects or further instances of a thing or item
# functions are called methods once defined in a class
class create_NewFile:
    def __init__(self) -> None:
      # what do we require to create our new file?(essentially the requirements of our constructor)
       self.label_line1 = ""
    #    self.label_line2 = ""
    #    self.label_line3 = ""
       self.new_file_name = ""

    def save_file(self):
        while True:
            try:
                self.file_name = input("Please type the name of your new file?.")
                self.extension_of_file =  input("Please enter the extension type of your new file.")
                self.new_file = self.file_name + '.' + self.extension_of_file
                return self.new_file
                break
            except Exception as e:
                print("An error has occured.")
                print("Please try again.")
                return None
            
    def address_input(self):
        while True:
            try:
                fn = input("Your first name: ")
                mi = input("Your middle name/initial: ")
                ln = input("Your last name: ")
                # street_add1 = input("First part of your street address: ")
                # street_add2 = input("Apartment # or secondary identifier if applicable otherwise hit enter: ")
                # city = input("Your city: ")
                # state = input("Your state: ")
                # zip_code = input("Your ZIP: ")
                phone_num = input("Your Phone number: ")

                self.label_line1 = f"{fn} {mi} {ln} - {phone_num}\n"
                # label_line2 = f"{street_add1} {street_add2}\n"
                # label_line3 = f"{city} {state} {zip_code}\n"
        
                return self.label_line1
                break
            except Exception as e:
                print("Information not collected, please try again")
                return None  
            
    def write_file(self):
        while True:
            try:
                with open(self.new_file, 'w') as file:
                    file.write(self.label_line1)
                    # file.write(label_line2)
                    # file.write(label_line3)
                    print(f" {self.new_file} was written succesfully.")
                    break
            except FileNotFoundError as e:
                print(f"File not found: {e}")
            except IOError as e:
                print(f"An error has occured, file not written. Please try again")

    def preview(self):
        print("Your address label preview: ")
        print(str(self.label_line1))
        # print(str(label_line2))
        # print(str(label_line3))

    def main(self):
        while True:
            self.new_file_name = self.save_file()
            if self.new_file_name is not None:
                self.label_line1 = self.address_input()
                # write_file(new_file_name, label_line1, label_line2, label_line3)
                self.preview()
                confirmation = input("Do you want to proceed with saving? (yes/no)").strip().lower()
                if confirmation == 'yes':
                    self.write_file()
                elif confirmation == 'no':
                    print('not saved')
                    break
                else:
                    print('not applicable')

                break

if __name__ == '__main__':
    new_File = create_NewFile()
    new_File.main()




















