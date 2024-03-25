def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact changed'
@input_error
def show_phone(args, contacts):
    return f'name {args[0]} phone {contacts[args[0]]}'

@input_error
def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    commands = ["hello", "add", "change", "phone", "all", "close", "exit"]
    while True:
        user_input = input(f"Enter a command ({commands}): \n>>> ")
        cmd, *args = parse_input(user_input)
            
        if cmd in ['exit', 'close']:
            print('Good bye!')
            break
        elif cmd == 'hello':
            print('Can i help you?')
        elif cmd == 'add':
            print(add_contact(args, contacts))
        elif cmd == 'change':
            print(change_contact(args, contacts))
        elif cmd == 'phone':
            print(show_phone(args, contacts))
        elif cmd == 'all':
            print(show_all(contacts))
        else:
            print("Invalide command.")


if __name__ == "__main__":
    main()
