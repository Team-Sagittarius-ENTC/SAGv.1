import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, required=True)
parser.add_argument('--object', type=str, required=True)

args = parser.parse_args()



def process_lines(line_list):

    print('[!] Starting processing machine codes')

    new_data = []
    for line in line_list:
        line = "".join(line.split())
        
        comment_index = line.find('/')

        line = line[:comment_index]
        
        if(len(line) == 16):
            new_data.append(hex(int(line, 2))[2:])
    
    print('[+] Machine code conversion done')
    return new_data

def create_object_code(hex_codes, output_file):
    
    print('[!] Atempting file write operation')
    with open(output_file, 'w') as object_code:
        object_code.write("v2.0 raw")
        
        for counter, data in enumerate(hex_codes):
            
            if not (counter % 8):
                object_code.write("\n")
            else:
                object_code.write(" ")
                
            object_code.write(str(data))
    print('[+] Compilation done\n')

def main():
    
    print("[+] Compiler started")
    print("[!] Attempting file reading")
    try:
        with open (args.source, 'r') as sourse:
            content = sourse.readlines()

        print('[+] File reading successful')

    except FileNotFoundError:
        print("[-] Source file could not found!!")
    except IOError:
        print('[-] File could not opened')
    except Exception as err:
        print('[-] Error occured')
        print('[!] Err = {}'.format(err))

    
    content = process_lines(content)

    dotindex = args.object.find('.')

    if dotindex < 0:
        out_file_name = args.object
    else:
        out_file_name = args.object[:dotindex]

    create_object_code(content, out_file_name)

if __name__ == '__main__':
    main()